#!/bin/bash
#
# Installs VMware Tools

# Only run this script if actually running a VMware build
if [ "${PACKER_BUILDER_TYPE}" != "vmware-iso" ] && [ "${PACKER_BUILDER_TYPE}" != "vmware-vmx" ]; then
    exit 0
fi

# Mount the ISO
mountpoint=/tmp/vmware-tools
guest_additions_iso=/tmp/VMwareTools.iso
mkdir "${mountpoint}"
mount -o loop "${guest_additions_iso}" "${mountpoint}"

# Install VMware tools
"${mountpoint}/run_upgrader.sh"

# Unmount the ISO
umount "${mountpoint}"

# Clean up
rm -rf "${mountpoint}"
rm -rf "${guest_additions_iso}"
