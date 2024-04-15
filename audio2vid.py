import traceback
import logging

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
        from preconfigured_audio_processing import models
        print(f'{models()=}', flush=True)
        super().__init__(*args, **kwargs)

    def VideoFromAudio(self, request, context):  # noqa
        try:
            # video_data = video_generator.convert_audio_to_video(request.audio_data)
            video_data = b'hello world'
            logger.info('VideoFromAudio: success')
            return audio2video_pb2.VideoResponse(video_data=video_data)
        except Exception as e:
            traceback.print_exc()
            logger.error(e)

    def CheckHealth(self, request, context):
        try:
            from preconfigured_audio_processing import models
            print(f'{models()=}', flush=True)
            logger.info('CheckHealth: Service is alive')
            return audio2video_pb2.HealthCheckResponse(status='Service is alive')
        except Exception as e:
            traceback.print_exc()
            logger.error(e)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    audio2video_pb2_grpc.add_VideoFromAudioGeneratorServicer_to_server(VideoFromAudioGeneratorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
