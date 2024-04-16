import io
import traceback
import logging
import tempfile
from time import perf_counter

import grpc
from concurrent import futures
from services.audio2video import audio2video_pb2
from services.audio2video import audio2video_pb2_grpc
# import video_generator


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
# logger.setLevel(INFO)


class VideoFromAudioGeneratorServicer(audio2video_pb2_grpc.VideoFromAudioGeneratorServicer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Warm up models
        from preconfigured_audio_processing import get_models, get_args
        get_models(get_args())

        self.time_spent = 0
        self.processed_n = 0

    def VideoFromAudio(self, request, context):  # noqa
        import io
        from preconfigured_audio_processing import generate, get_args

        audio_file = None
        temp_dir = None

        try:
            st = perf_counter()

            args = get_args()
            # Create Input Audio File
            audio_file = tempfile.NamedTemporaryFile(mode='ab+', suffix='.wav', delete=True)
            audio_file.write(request.audio_data)
            audio_file.flush()
            audio_file.seek(0, 0)
            args.driven_audio = audio_file.name
            # Output Video File
            if not args.result_dir:
                temp_dir = tempfile.TemporaryDirectory(prefix='audio2vid-temp-')
                args.result_dir = temp_dir.name

            video_path = generate(args)
            with open(video_path, 'rb') as f:
                response = audio2video_pb2.VideoResponse(video_data=f.read())

            self.time_spent += perf_counter() - st
            self.processed_n += 1
            logger.info(f'Mean time taken: {int(self.time_spent / self.processed_n)} sec.')

            return response

        except Exception as e:
            traceback.print_exc()
            logger.error(e)

        finally:
            if isinstance(audio_file, io.BytesIO):
                audio_file.close()
            if isinstance(temp_dir, tempfile.TemporaryDirectory):
                temp_dir.cleanup()

    def CheckHealth(self, request, context):
        try:
            from preconfigured_audio_processing import get_models, get_args
            print(f'{get_models(get_args())=}', flush=True)
            logger.info('CheckHealth: Service is alive')
            return audio2video_pb2.HealthCheckResponse(status='Service is alive')
        except Exception as e:
            traceback.print_exc()
            logger.error(e)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    audio2video_pb2_grpc.add_VideoFromAudioGeneratorServicer_to_server(VideoFromAudioGeneratorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
