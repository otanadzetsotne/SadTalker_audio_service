import grpc
from services.audio2video import audio2video_pb2
from services.audio2video import audio2video_pb2_grpc


def run_health_check():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = audio2video_pb2_grpc.VideoFromAudioGeneratorStub(channel)
        response = stub.CheckHealth(audio2video_pb2.HealthCheckRequest())
        print("Health Check Status: ", response.status)


def run_audio2vid():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = audio2video_pb2_grpc.VideoFromAudioGeneratorStub(channel)

        with open('./tmp/voice.wav', 'rb') as f:
            audio_data = f.read()

        response = stub.VideoFromAudio(audio2video_pb2.AudioRequest(audio_data=audio_data))

        with open('./tmp/result.mp4', 'wb') as f:
            f.write(response.video_data)

        print("Video From Audio Status: ", response.status)


if __name__ == '__main__':
    run_health_check()
