#!/bin/bash

set -e

# Get the full path of the current script
script_path=$(realpath "$0")

# Extract the directory from the full path
base_dir="$(dirname "$script_path")/.."

echo "Project directory: $base_dir"
cd $base_dir

echo "Installing PyTorch and dependencies..."
pip install torch torchaudio
pip install -U torchvision==0.16.0

echo "Installing ffmpeg via conda..."
conda install ffmpeg -y

echo "Installing Python packages from requirements.txt..."
pip install -r requirements.txt

echo "Installing dlib..."
pip install dlib # Note: macOS might need additional steps for dlib.

./scripts/download_models.sh
