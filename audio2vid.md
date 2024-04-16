# audio2vid

## Installation

This installation guide is working on `Linux` and successfully was tested on `WSL`.

1. Create virtual environment
    ```
    python -m venv venv
    ```
2. Activate it
    ```
    source ./venv/bin/activate
    ```
3. Install torch libraries
    ```
    pip3 install torch torchvision==0.16.0 
    ```
4. Install ffmpeg
    ```
    sudo apt update && sudo apt install ffmpeg
    ```
5. Install required dependencies
    ```
    pip3 install -r requirements.txt
    ```
6. Download models
    ```
    ./scripts/download_models.sh
    ```

## Compile server

Proto for this service is stored in `./proto/audio2video.proto`.
Service may recompiled with `./scripts/compile_audio2video.sh` script, but **it is not recommended**
to recompile it without special need.

## Running server

Audio to Video gRPC server initializing with predefined `--source_image` parameter
and receives audio data to generate video output.

While generating output video, program uses file system for each step.
You can pass directory to use with `--result_dir` parameter of service will create
temporary directory.
Service will also store resulting videos to this directory.

Running server script:
```
python audio2vid.py --source_image=/path/to/source/image.jpg --still --preprocess=full
```
Server will run on `localhost` on `50051` port.

## Health check

To check if server is running properly, you can run:
```
python audio2vid_client_check.py
```
