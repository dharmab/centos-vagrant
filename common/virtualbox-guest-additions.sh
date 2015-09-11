#!/bin/bash

set -e

yum -y install dkms
mountpoint=/tmp/virtualbox-guest-addtions
guest_additions_iso=/tmp/VBoxGuestAdditions.iso
mkdir ${mountpoint}
mount -o loop ${guest_additions_iso} ${mountpoint}
# The VirtualBox Guest Additions will return a failure exit code if X11 is not
# present, so we have to override the return value
/bin/sh ${mountpoint}/VBoxLinuxAdditions.run || true
umount ${mountpoint}
rm -rf ${mountpoint}
rm -rf ${guest_additions_iso}

