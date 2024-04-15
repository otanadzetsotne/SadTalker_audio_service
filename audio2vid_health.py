import grpc
from services.audio2video import audio2video_pb2
from services.audio2video import audio2video_pb2_grpc


def run_health_check():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = audio2video_pb2_grpc.VideoFromAudioGeneratorStub(channel)
        response = stub.CheckHealth(audio2video_pb2.HealthCheckRequest())
        print("Health Check Status: ", response.status)


if __name__ == '__main__':
    run_health_check()
