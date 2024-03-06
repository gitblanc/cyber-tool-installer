#!/bin/bash
mkdir -p "$HOME/tools"
git clone https://github.com/sherlock-project/sherlock.git "$HOME/tools/sherlock"
python3 -m pip install -r "$HOME/tools/sherlock/requirements.txt"