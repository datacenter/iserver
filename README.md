# iserver

iserver is command line tool using REST API with various Cisco products.

Important note: documentation is partial and it will be uploaded again once sensitive information is removed

## Features

Compute
- [Intersight](./doc/intersight/README.md)
- [IMC](./doc/imc/README.md)
- [Redfish](./doc/redfish/README.md)
- [UCSM](./doc/ucsm/README.md)

Networking
- [ACI](./doc/aci/README.md)
- [Nexus](./doc/nexus/README.md)

Virtualization
- [OpenStack](./doc/osp/README.md)
- [vCenter](./doc/vcenter/README.md)

Containers
- [Helm](./doc/helm/README.md)
- [Kubernetes](./doc/k8s/README.md)
- [OpenShift](./doc/ocp/README.md)

Orchestration
- [Network Services Orchestrator](./doc/nso/README.md)

Security
- [PSIRT](./doc/psirt/README.md)

Other
- [Webex Bot](./doc/bot/README.md)

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://wwwin-github.cisco.com/emear-telcocloud/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

Features using Intersight API require [isctl](https://github.com/cgascoig/isctl) and OS installation requires isctl version >= 0.1.18.

No requiremets for non-Intersight related features.
