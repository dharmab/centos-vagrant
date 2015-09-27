#!/usr/bin/env python

import os
import urllib
import zipfile
import sys
import platform


def get_packer_download_url():
    # Idiom for checking for 64-bit is a workaround for Mac OSX
    # https://docs.python.org/2/library/platform.html#platform.architecture
    if sys.maxsize < 2**32:
        raise RuntimeError("A 64-bit system is required")

    system = platform.system().lower()
    if system.startswith("linux"):
        return "https://dl.bintray.com/mitchellh/packer/packer_0.8.6_linux_amd64.zip"
    # Mac OSX
    elif system == "darwin":
        return "https://dl.bintray.com/mitchellh/packer/packer_0.8.6_darwin_amd64.zip"
    elif system == "win32":
        return "https://dl.bintray.com/mitchellh/packer/packer_0.8.6_windows_amd64.zip" 
    elif system.startswith("freebsd"):
        return "https://dl.bintray.com/mitchellh/packer/packer_0.8.6_freebsd_amd64.zip" 
    else:
        raise RuntimeError(platform.system() + " is not a supported platform")


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_packer_archive_path():
    return get_script_path() + "/__packer.zip"


def get_packer_binaries_path():
    return get_script_path() + "/bin"


def get_packer_path():
    return get_packer_binaries_path() + "/packer"


try:
    packer_download_url = get_packer_download_url()
except RuntimeError as e:
    # Unsupported platform
    print(str(e))
    exit(1)

# Preemptively remove any failed downloads
delete_file(get_packer_archive_path())

# Ensure that the packer binary directory exists
if not os.path.exists(get_packer_binaries_path()):
    os.makedirs(get_packer_binaries_path())

# Check if the packer executable is already present
# If not, download and extract it
if not os.path.isfile(get_packer_path()):
    try:
        urllib.urlretrieve(packer_download_url, get_packer_archive_path())
        with zipfile.ZipFile(get_packer_archive_path(), "r") as packer_archive:
            packer_archive.extractall(path=get_packer_binaries_path())
    finally:
        delete_file(get_packer_archive_path())

# Ensure that packer binaries are marked as executable
for root, subdirectories, files in os.walk(get_packer_binaries_path()):
    for f in files:
        os.chmod(root +  "/" + f, 755)

