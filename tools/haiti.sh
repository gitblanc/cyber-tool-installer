#!/bin/bash
apt install ruby-paint
mkdir -p "$HOME/tools/haiti"
wget "https://github.com/noraj/haiti/archive/refs/tags/v2.1.0.zip" -O "$HOME/tools/haiti/haiti.zip"
unzip "$HOME/tools/haiti/haiti.zip" -d "$HOME/tools/haiti"
dpkg -i "$HOME/tools/haiti/haiti/packages/debian/ruby-docopt_0.6.1_all_debian11.deb"
dpkg -i "$HOME/tools/haiti/haiti/packages/debian/haiti_1.5.0_all_debian11.deb"
rm -rf "$HOME/tools/haiti/"


