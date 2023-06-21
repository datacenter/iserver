# iserver

iserver is command line tool using REST API with various Cisco products.

## Server Features

- [Servers inventory](./doc/features/ServersInventory.md)
- [Server details](./doc/features/ServerDetails.md)
- [Power control](./doc/features/PowerControl.md)
- [Locator LED control](./doc/features/LedControl.md)
- [Operating System installation](./doc/features/OsInstall.md)
- [Workflows](./doc/features/Workflows.md)
- [Workflow details](./doc/features/Workflow.md)
- [Power and Thermal monitoring](./doc/green/README.md)

## Other Features

- [ACI](./doc/aci/README.md)
- [Redfish](./doc/redfish/README.md)
- [UCSM](./doc/ucsm/README.md)

## Installation

- iserver binary is compiled for Windows, Linux and MAC
- download the latest release from the [Releases](https://github.com/datacenter/iserver/releases/latest) page.
- move binary somewhere that is on your path (e.g. /usr/local/bin)

If binary is not available or you prefer using source code, clone the repository and run iserver using Python3 with [required](requirements) pip3 packages.

## Requirements

Features using Intersight API require [isctl](https://github.com/cgascoig/isctl) and OS installation requires isctl version >= 0.1.18.

No requiremets for non-Intersight related features.
