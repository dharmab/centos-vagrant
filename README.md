# CentOS Packer Build Project

[Packer](https://packer.io) automation to build CentOS virtual machines for use with [Vagrant](https://vagrantup.com). To use these boxes in your own project, type one of the following commands:

- CentOS 7: `vagrant init dharmab/centos7`.
- CentOS 6: `vagrant init dharmab/centos6`.

The box versioning on Atlas follows [Semantic Versioning](http://semver.org).

I haven't been maintaining this lately because my environment is now Docker/CoreOS based. But it should be pretty simple for someone else to maintain themselves. Just change the following in each Packer template:

- `builders.iso_url`
- `builders.iso_checksum`
- `post-processors[.type = "atlas"].artifact`
- `push.name`

## Quick Build

1. Run `setup.py` with Python 2 to download Packer
1. Generate an [Atlas](https://atlas.hashicorp.com) API key and run `export ATLAS_TOKEN="<api key>"` 
1. If you are not [dharmab](http://www.dharmab.com), edit the JSON templates and change `push.name` to `<atlas organization>/<box name>`
1. Run the following commands to push the build to Atlas and queue a build.
```bash
bin/packer build centos7.json
bin/packer build centos6.json
```

## Box Information

This section should be considered the 'Public API' for the purposes of Semantic Versioning.

- The artifact(s) of this Packer template are Vagrant boxes for CentOS 6 and CentOS 7.
- VirtualBox is a supported provider.
  - The VirtualBox boxes include the VirtualBox Guest Additions for VirtualBox 5.
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

