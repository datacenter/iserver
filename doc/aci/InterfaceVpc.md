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

Output options:
  - [state](./InterfaceVpcOutputState.md) (default)
  - [address](./InterfaceVpcOutputAddress.md)
  - [verbose](./InterfaceVpcOutputVerbose.md)
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
  -o, --output [state|address|verbose|json]
                                  [default: state]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 32 ms and logs saved in /tmp/iserver\caad786acc49
```

[[Back]](./Interface.md)