#!/bin/bash

set -e

# Install dependencies
yum -y install dkms bzip2

# Mount the ISO
mountpoint=/tmp/virtualbox-guest-addtions
guest_additions_iso=/tmp/VBoxGuestAdditions.iso
mkdir ${mountpoint}
mount -o loop ${guest_additions_iso} ${mountpoint}

# Install the VirtualBox Guest Additions
# The installer will return a failure exit code if X11 is not present, so we 
# have to override the return value
/bin/sh ${mountpoint}/VBoxLinuxAdditions.run || true

# Unmount the ISO
umount ${mountpoint}

# Clean up
rm -rf ${mountpoint}
rm -rf ${guest_additions_iso}

