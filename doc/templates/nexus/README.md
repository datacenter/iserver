# Nexus

Uses NX-OS API calls to provide the configuration and operational state of Nexus device via CLI.

## Usage

Nexus device can be [pre-defined](./Device.md) and then used in with '--device <name>' option. Last used device name becomes default one.

Example:

```
# iserver get nx mac --device my-nexus
```

Nexus devices can be tagged with domain to perform commands on the group of Nexus devices.

```
# iserver get nx mac --device dom:lab
```

Nexus access authentication details can be defined in each command execution instead.

```
# iserver get nx mac --ip 10.1.1.1 --username admin --password secret
```

## Features

- [lacp](Lacp.md)
- [lldp](Lldp.md)
- [mac](Mac.md)
- [ver](Ver.md)

## Cross domain

- [psirt](Psirt.md)
- [server](./Server.md)

[[Back]](../../README.md)