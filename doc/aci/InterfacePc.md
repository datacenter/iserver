# Node Interface

## Port Channel (PC)

Node selection options:
  - [single node](./InterfacePcNode.md)
  - [selected nodes](./InterfacePcNodes.md)
  - [all nodes](./InterfacePcNodesAll.md)
  - [multi APIC](./InterfacePcApics.md)

Filter options:
  - [Port Channel ID](./InterfacePcId.md)
  - [Port Channel Name](./InterfacePcName.md)
  - [VPC Domain](./InterfacePcDomain.md)
  - [Speed](./InterfacePcSpeed.md)
  - [State](./InterfacePcState.md)

Output options:
  - [state](./InterfacePcOutputState.md) (default)
  - [port](./InterfacePcOutputPort.md)
  - [verbose](./InterfacePcOutputVerbose.md)
  - [json](./InterfacePcOutputJson.md)

Command options

```
# iserver get aci intf pc --help

Usage: iserver.py get aci intf pc [OPTIONS]

  Get aci node port channel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by port channel id
  --name TEXT                     Filter by name
  --speed TEXT                    Filter by speed
  --domain TEXT                   Filter by domain id
  --state [any|up|down]           Filter by state  [default: any]
  -o, --output [state|port|verbose|json]
                                  [default: state]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\81441bbaf9e7
```

[[Back]](./Interface.md)