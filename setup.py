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

    base_url = "https://releases.hashicorp.com/packer/0.8.6/"
    system = platform.system().lower()
    if system.startswith("linux"):
        return base_url + "packer_0.8.6_linux_amd64.zip"
    # Mac OSX
    elif system == "darwin":
        return base_url + "packer_0.8.6_darwin_amd64.zip"
    elif system.startswith("freebsd"):
        return base_url + "packer_0.8.6_freebsd_amd64.zip"
    else:
        raise RuntimeError(platform.system() + " is not a supported platform")


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_packer_archive_path():
    return os.path.join(get_script_path(), "packer.zip")


def get_packer_binaries_path():
    return os.path.join(get_script_path(), "bin")


def is_windows():
    return platform.system().lower() == "windows"


def get_packer_path():
    packer_binary = "packer"
    if is_windows:
        packer_binary = "packer.exe"
    return os.path.join(get_packer_binaries_path(), packer_binary)


def main():
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
        print("Did not find packer executable, downloading...")
        try:
            urllib.urlretrieve(packer_download_url, get_packer_archive_path())
            with zipfile.ZipFile(get_packer_archive_path(), "r") as archive:
                archive.extractall(path=get_packer_binaries_path())
        finally:
            delete_file(get_packer_archive_path())
    else:
        print("packer executable found, skipping download...")

    if not is_windows():
        # Ensure that packer binaries are marked as executable
        for root, subdirectories, files in os.walk(get_packer_binaries_path()):
            for f in files:
                os.chmod(os.path.join(root, f), 755)



if __name__ == "__main__":
    main()
