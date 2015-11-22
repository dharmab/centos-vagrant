# CentOS Packer Build Project

[Packer](https://packer.io) automation to build a CentOS 7 virtual machine for use with [Vagrant](https://vagrantup.com). To use this box in your own project, type `vagrant init dharmab/centos7`.

The box versioning on Atlas follows [Semantic Versioning](http://semver.org).

## Quick Build

1. Run `setup.py` with Python 2 to download Packer
1. Generate an [Atlas](https://atlas.hashicorp.com) API key and run `export ATLAS_TOKEN="<api key>"` 
1. If you are not [dharmab](http://www.dharmab.com), edit `centos7.json` and change `push.name` to `<atlas organization>/centos7`
1. Run `bin/packer push centos7.json` to push the build to Atlas and queue a build.

## Box Information

This section should be considered the 'Public API' for the purposes of Semantic Versioning.

- The artifact(s) of this Packer template are Vagrant box(es) for CentOS 7.
- VirtualBox is a supported provider.
  - The VirtualBox box includes the VirtualBox Guest Additions for VirtualBox 5.
- VMware is a supported provider.
  - The VMware box includes VMware Tools.
- All packages in the `core` group are installed.
- The [Extra Packages for Enterprise Linux](https://fedoraproject.org/wiki/EPEL) repository (EPEL) is enabled.
- All installed packages are fully up to date at build time. 
- The timezone is set to UTC.
- The language is set to US English.
- The keyboard is set to US.
- The firewall is disabled.
- SELinux is disabled.
- `requiretty` is disabled in the sudoers configuration.
- `UseDNS` is disabled in the SSH configuration.
- The root password is `vagrant`.
- A user named `vagrant` is configured.
  - The password for the `vagrant` user is `vagrant`.
  - The `vagrant` user has full passwordless sudo privileges.
  - The `vagrant` user has the standard insecure Vagrant SSH public key as an authorized key.

## Hacking on this project

I work on this project using an Arch Linux development environment, so I'll provide instructions for that Operating System. If you want to hack on this project, you're probably a smart cookie and can figure things out from there <3

### Essential documentation:

- [Packer documentation](https://packer.io/docs)
- [Kickstart documentation](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Installation_Guide/sect-kickstart-syntax.html)
- [Vagrant base box documentation](https://docs.vagrantup.com/v2/boxes/base.html)
- [VirtualBox Guest Additions documentation](https://www.virtualbox.org/manual/ch04.html)

### Basic Setup

- [Install VirtualBox](https://wiki.archlinux.org/index.php/VirtualBox#Installation_steps_for_Arch_Linux_hosts).
- [Install VMware Workstation Pro](https://wiki.archlinux.org/index.php/VMware). Get the installer from [VMware's site](https://www.vmware.com/products/workstation). 
- You can use the included setup script to download Packer, or install `packer-io` from the AUR which installs Packer as `/usr/bin/packer-io`. (The name change avoids conflict with `packer`, a popular `pacman` replacement and AUR client.)
- Open `vmplayer`, create a Virtual Machine, power it on and click **Virtual Machine** > **Install VMware Tools** to download the VMware Tools installer. You can delete the VM once the download is complete.

When debugging issues locally, remember to remove the Atlas post-processor from the template.

Remember- you can build the VMs and Vagrant boxes using free tools, and you can use the VirtualBox Vagrant box for free, but you'll need the commercial [VMware plugin for Vagrant](http://www.vagrantup.com/vmware) to use the VMware Vagrant box!
