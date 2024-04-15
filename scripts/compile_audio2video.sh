#!/bin/bash

set -e

# Get the full path of the current script
script_path=$(realpath "$0")

# Extract the directory from the full path
base_dir="$(dirname "$script_path")/.."

cd "$base_dir"

python -m grpc_tools.protoc -I./proto --python_out=./services/audio2video --pyi_out=./services/audio2video --grpc_python_out=./services/audio2video ./proto/audio2video.proto
