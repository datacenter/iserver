# Operating System Installation

Operating System installation requires:
- [OS Image](./OsImage.md)
- [OS Configuration](./OsConfig.md)
- [Software Configuration Utility](./OsScu.md)

Supported OS installation workflows

Intent | Command | Documentation
--- | --- | ---
OS install with DHCP | iserver create os-install dhcp | [examples](OsInstallDhcp.md)
OS install with static IP | iserver create os-install static | [examples](OsInstallStatic.md)
OS install with embedded kickstart  | iserver create os-install embedded | [examples](OsInstallEmbedded.md)

Perform [batch](OsInstallBatch.md) OS installation on multiple servers based on the YAML files input.