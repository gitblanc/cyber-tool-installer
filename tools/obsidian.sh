#!/bin/bash
wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.5.8/obsidian_1.5.8_amd64.deb -O /tmp/obsidian.deb
dpkg -i /tmp/obsidian.deb
rm -f /tmp/obsidian.deb