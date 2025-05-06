# iserver

iserver is command line tool using REST API with various Cisco products.

Important note: documentation is partial and it will be uploaded again once sensitive information is removed

## Features

Compute
- [Intersight](./doc/intersight/README.md)
- IMC
- Redfish
- UCSM

Networking
- ACI
- Nexus

Virtualization
- OpenStack
- vCenter

Containers
- Helm
- Kubernetes
- OpenShift

Orchestration
- Network Services Orchestrator

Security
- PSIRT

Other
- Webex Bot

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://github.com/datacenter/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

Features using Intersight API require [isctl](https://github.com/cgascoig/isctl) and OS installation requires isctl version >= 0.1.18.

No requiremets for non-Intersight related features.
