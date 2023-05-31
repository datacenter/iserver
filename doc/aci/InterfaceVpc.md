# Node Interface

## Virtual Port Channel (VPC)

Node selection options:
  - [single node](./InterfaceVpcNode.md)
  - [selected nodes](./InterfaceVpcNodes.md)
  - [all nodes](./InterfaceVpcNodesAll.md)
  - [multi APIC](./InterfaceVpcNodesApics.md)

Filter options:
  - [Domain ID](./InterfaceVpcId.md)
  - [Peer state](./InterfaceVpcState.md)
  - [Members state](./InterfaceVpcMember.md)

View options:
  - [default](./InterfaceVpcOutputState.md)
  - [address](./InterfaceVpcOutputAddress.md)
  - [verbose](./InterfaceVpcOutputVerbose.md)

Output options:
  - [default](./InterfaceVpcOutputState.md)
  - [json](./InterfaceVpcOutputJson.md)

Command options

```
# iserver get aci intf vpc --help

Usage: iserver.py get aci intf vpc [OPTIONS]

  Get aci node virtual port channel interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by vpc domain id
  --state [any|up|down]           [default: any]
  --member [any|up|down]          [default: any]
  -v, --view [default|address|verbose]
  -o, --output [default|json]     [default: default]
  --empty                         No error on empty result
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 38 ms and logs saved in /tmp/iserver\6dd981470340
```

[[Back]](./Interface.md)