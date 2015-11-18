# CentOS Packer Build Project

[Packer](https://packer.io) automation to build a CentOS 7 virtual machine for use with [Vagrant](https://vagrantup.com).

## Quick Build

1. Run `setup.py` with Python 2 to download Packer
1. Generate an [Atlas](https://atlas.hashicorp.com) API key and run `export ATLAS_TOKEN="<api key>"` 
1. If you are not [dharmab](https://www.dharmab.com), edit `centos7.json` and change `push.name` to `<atlas organization>/centos7`
1. Run `bin/packer push centos7.json` to push the build to Atlas and queue a build.

