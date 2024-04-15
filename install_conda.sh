#!/bin/bash

set -e

#!/bin/bash

# Check if 'conda' command is available
if command -v conda &> /dev/null
then
    echo "Miniforge is already installed."
else
    echo "Miniforge is not installed. Installing Miniforge..."

    # Define the installer path and URL for Miniforge
    INSTALLER_PATH="$HOME/miniforge_installer.sh"
    MINIFORGE_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh"

    # Download the installer
    curl -L $MINIFORGE_URL -o $INSTALLER_PATH

    # Make the installer executable
    chmod +x $INSTALLER_PATH

    # Run the installer
    sh $INSTALLER_PATH -b

    # Remove the installer
    rm $INSTALLER_PATH

    # Add Miniforge to the PATH (modify .bashrc or appropriate file according to your shell)
    echo 'export PATH="$HOME/miniforge3/bin:$PATH"' >> $HOME/.bashrc
    source $HOME/.bashrc

    echo "Miniforge installed successfully."
fi
