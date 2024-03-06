#!/bin/bash
apt install ruby-paint
latest_release_tag=$(curl -s https://api.github.com/repos/noraj/haiti/releases/latest | jq -r '.tag_name')
download_url="https://github.com/noraj/haiti/archive/refs/tags/${latest_release_tag}.zip"
mkdir -p "$HOME/tools/haiti"
wget "$download_url" -O "$HOME/tools/haiti/haiti-${latest_release_tag}.zip"
unzip "$HOME/tools/haiti/haiti-${latest_release_tag}.zip" -d "$HOME/tools/haiti"
dpkg -i "$HOME/tools/haiti/haiti-${latest_release_tag}/packages/debian/ruby-docopt_0.6.1_all_debian11.deb"
dpkg -i "$HOME/tools/haiti/haiti-${latest_release_tag}/packages/debian/haiti_1.5.0_all_debian11.deb"
rm -rf "$HOME/tools/haiti/"


