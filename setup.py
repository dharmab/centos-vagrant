#!/usr/bin/env python

import os
import urllib
import zipfile

script_path = os.path.dirname(os.path.realpath(__file__))
packer_archive_path = script_path + "/packer.zip"
bin_path = script_path + "/bin"

if not os.path.isfile(bin_path + "/packer"):
    if not os.path.exists(bin_path):
        os.makedirs(bin_path)
    try:
        urllib.urlretrieve("https://dl.bintray.com/mitchellh/packer/packer_0.8.6_linux_amd64.zip", packer_archive_path)
        with zipfile.ZipFile(packer_archive_path, "r") as packer_archive:
            packer_archive.extractall(path=bin_path)
    finally:
        os.remove(packer_archive_path)

for root, subdirectories, files in os.walk(bin_path):
    for f in files:
        os.chmod(root +  "/" + f, 755)

