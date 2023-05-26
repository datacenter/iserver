# Node Interface

## SVI

Node selection options:
  - [single node](./InterfaceSviNode.md)
  - [selected nodes](./InterfaceSviNodes.md)
  - [all nodes](./InterfaceSviNodesAll.md)
  - [multi APIC](./InterfaceSviNodesApics.md)

Filter options:
  - [Interface ID](./InterfaceSviId.md)
  - [Interface Type](./InterfaceSviType.md)
  - [Oper State](./InterfaceSviState.md)
  - [MAC Address](./InterfaceSviMac.md)
  - [IP address](./InterfaceSviIp.md)
  - [IP subnet](./InterfaceSviSubnet.md)

Output options:
  - [state](./InterfaceSviOutputState.md) (default)
  - [address](./InterfaceSviOutputAddress.md)
  - [counter](./InterfaceSviOutputCounter.md)
  - [verbose](./InterfaceSviOutputVerbose.md)
  - [json](./InterfaceSviOutputJson.md)

Command options

```
# iserver get aci intf svi --help

Usage: iserver.py get aci intf svi [OPTIONS]

  Get aci node svi interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Port name
  --admin [any|up|down]           [default: any]
  --oper [any|up|down]            [default: any]
  --type [any|int|ext]            [default: any]
  --mac TEXT                      MAC Address filter
  --vlan TEXT                     VLAN filter
  --ip TEXT                       IP Address filter
  --subnet TEXT                   IP Subnet filter
  -o, --output [state|addr|counter|verbose|json]
                                  [default: state]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 31 ms and logs saved in /tmp/iserver\78d826590b85
```

[[Back]](./Interface.md)