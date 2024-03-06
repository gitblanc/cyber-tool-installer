#!/bin/bash
pip3 install pycurl bs4 pygeoip gobject cairocffi selenium
wget https://github.com/epsylon/xsser/releases/download/1.8.3/xsser_1.8.3_all.deb -O "$HOME/tools/xsser"
dpkg -i "$HOME/tools/xsser/xsser_1.8.3_all.deb"
rm -rf "$HOME/tools/xsser/xsser_1.8.3_all.deb"