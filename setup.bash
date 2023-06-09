#!/usr/bin/env bash

echo "Installing venv support if needed."
sudo apt install -y python3-venv

echo "\r\nCreating and activating Virtual Env."
python3 -m venv venv
source venv/bin/activate

echo "\r\nInstalling requirements."
pip install -r requirements.txt

deactivate
