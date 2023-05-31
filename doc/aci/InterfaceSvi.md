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

View options:
  - [default](./InterfaceSviOutputState.md)
  - [address](./InterfaceSviOutputAddress.md)
  - [counter](./InterfaceSviOutputCounter.md)
  - [verbose](./InterfaceSviOutputVerbose.md)

Output options:
  - [state](./InterfaceSviOutputState.md)
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
  -v, --view [default|addr|counter|verbose]
  -o, --output [default|json]     [default: default]
  --empty                         No error on empty result
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\add795d0604b
```

[[Back]](./Interface.md)