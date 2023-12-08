# iserver

iserver is command line tool using REST API with various Cisco products.

## Features

- [ACI](./doc/aci/README.md)
- [Helm](./doc/helm/README.md)
- [Intersight](./doc/intersight/README.md)
- [Kubernetes](./doc/k8s/README.md)
- [Network Services Orchestrator (NSO)](./doc/nso/README.md)
- [Nexus](./doc/nexus/README.md)
- [Redfish](./doc/redfish/README.md)
- [OpenShift](./doc/ocp/README.md)
- [OpenStack](./doc/osp/README.md)
- [PSIRT](./doc/psirt/README.md)
- [UCSM](./doc/ucsm/README.md)

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://wwwin-github.cisco.com/emear-telcocloud/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

Features using Intersight API require [isctl](https://github.com/cgascoig/isctl) and OS installation requires isctl version >= 0.1.18.

No requiremets for non-Intersight related features.
