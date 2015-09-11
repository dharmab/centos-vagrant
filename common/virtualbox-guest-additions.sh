#!/bin/bash

set -e

yum -y install dkms
mountpoint='~/virtualbox-guest-addtions'
guest_additions_iso='~/VBoxGuestAdditions.iso'
mkdir ${mountpoint}
mount -o loop ${mountpoint} ${guest_additions_iso}}
# The VirtualBox Guest Additions will return a failure exit code if X11 is not
# present, so we have to override the return value
/bin/sh ${mountpoint}/VBoxLinuxAdditions.run || true
umount ${mountpoint}
rm -rf ${mountpoint}
rm -rf ${guest_additions_iso}

