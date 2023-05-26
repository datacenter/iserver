# Node Interface

## Physical

Node selection options:
  - [single node](./InterfacePhyNode.md)
  - [selected nodes](./InterfacePhyNodes.md)
  - [all nodes](./InterfacePhyNodesAll.md)
  - [multi APIC](./InterfacePhyNodesApics.md)

Filter options:
  - [Interface ID](./InterfacePhyId.md)
  - [Switching State](./InterfacePhySwitching.md)
  - [Operational State](./InterfacePhyOper.md)
  - [Type](./InterfacePhyType.md)
  - [Layer](./InterfacePhyLayer.md)
  - [MAC Address](./InterfacePhyMac.md)
  - [Speed](./InterfacePhySpeed.md)
  - [FEC](./InterfacePhyFec.md)
  - [Transceiver Optics](./InterfacePhyOptics.md)
  - [Transceiver Type](./InterfacePhyTrans.md)
  - [Internal VLAN](./InterfacePhyVlan.md)
  - [Encapsulation VLAN](./InterfacePhyEncapVlan.md)
  - [Fabric VxLAN](./InterfacePhyFabVxlan.md)
  - [EPG](./InterfacePhyEpg.md)
  - [CDP/LLDP Neighbor](./InterfacePhyNei.md)
  - [QoS Stats](./InterfacePhyQos.md)

Output options:
  - [state](./InterfacePhyOutputState.md) (default)
  - [ether](./InterfacePhyOutputEther.md)
  - [err](./InterfacePhyOutputErr.md)
  - [qos](./InterfacePhyOutputQos.md)
  - [trans](./InterfacePhyOutputTrans.md)
  - [eee](./InterfacePhyOutputEee.md)
  - [load](./InterfacePhyOutputLoad.md)
  - [nei](./InterfacePhyOutputNei.md)
  - [cdp](./InterfacePhyOutputCdp.md)
  - [lldp](./InterfacePhyOutputLldp.md)
  - [vlan](./InterfacePhyOutputVlan.md)
  - [epg](./InterfacePhyOutputEpg.md)
  - [pg](./InterfacePhyOutputPg.md)
  - [aaep](./InterfacePhyOutputAaep.md)
  - [pol](./InterfacePhyOutputPol.md)
  - [verbose](./InterfacePhyOutputVerbose.md)
  - [json](./InterfacePhyOutputJson.md)

Command options

```
# iserver get aci intf phy --help

Usage: iserver.py get aci intf phy [OPTIONS]

  Get aci node physical interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by interface id
  --switching [any|enabled|disabled]
                                  Filter by switching state  [default: any]
  --oper [any|up|down]            Filter by operational state  [default: any]
  --type [any|leaf|fab]           Filter by port type  [default: any]
  --qos [any|data|data-rx|data-tx|drops|drops-rx|drops-tx]
                                  Filter by qos counters  [default: any]
  --layer [any|l2|l3]             Filter by layer  [default: any]
  --mac TEXT                      Filter by mac address
  --speed [any|1G|10G|25G|40G|100G|400G]
                                  Filter by interface speed  [default: any]
  --fec TEXT                      Filter by fec
  --optics TEXT                   Filter by transceiver optics
  --trans TEXT                    Filter by transceiver type
  --epg TEXT                      Filter by epg name
  --vlan TEXT                     Filter by vlan value
  --evlan TEXT                    Filter by encapsulation vlan value
  --fvxlan TEXT                   Filter by fabric vxlan value
  --nei TEXT                      Filter by cdp/lldp neight system name
  -o, --output [default|trans|vlan|epg|load|eee|nei|cdp|lldp|pg|pol|aaep|ether|err|qos|verbose|json]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 46 ms and logs saved in /tmp/iserver\aae974eb17ab
```

[[Back]](./Interface.md)