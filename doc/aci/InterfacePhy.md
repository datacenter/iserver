# Node Interface - Physical

## Command options

Filter options:
  - [Interface ID](./InterfacePhyFilterId.md)
  - [Switching State](./InterfacePhyFilterSwitching.md)
  - [Operational State](./InterfacePhyFilterOper.md)
  - [Type](./InterfacePhyFilterType.md)
  - [Layer](./InterfacePhyFilterLayer.md)
  - [MAC Address](./InterfacePhyFilterMac.md)
  - [Speed](./InterfacePhyFilterSpeed.md)
  - [FEC](./InterfacePhyFilterFec.md)
  - [Transceiver Optics](./InterfacePhyFilterOptics.md)
  - [Transceiver Type](./InterfacePhyFilterTrans.md)
  - [Internal VLAN](./InterfacePhyFilterVlan.md)
  - [Encapsulation VLAN](./InterfacePhyFilterEncapVlan.md)
  - [Fabric VxLAN](./InterfacePhyFilterFabVxlan.md)
  - [EPG](./InterfacePhyFilterEpg.md)
  - [CDP/LLDP Neighbor](./InterfacePhyFilterNei.md)
  - [QoS Stats](./InterfacePhyFilterQos.md)

View options:
  - [state](./InterfacePhyViewState.md)
  - [ether](./InterfacePhyViewEther.md)
  - [err](./InterfacePhyViewErr.md)
  - [qos](./InterfacePhyViewQos.md)
  - [trans](./InterfacePhyViewTrans.md)
  - [eee](./InterfacePhyViewEee.md)
  - [load](./InterfacePhyViewLoad.md)
  - [nei](./InterfacePhyViewNei.md)
  - [cdp](./InterfacePhyViewCdp.md)
  - [lldp](./InterfacePhyViewLldp.md)
  - [vlan](./InterfacePhyViewVlan.md)
  - [epg](./InterfacePhyViewEpg.md)
  - [pg](./InterfacePhyViewPg.md)
  - [aaep](./InterfacePhyViewAaep.md)
  - [pol](./InterfacePhyViewPol.md)
  - [fault](./InterfacePhyViewFault.md)
  - [hfault](./InterfacePhyViewFaultHistory.md)
  - [event](./InterfacePhyViewEvent.md)
  - [audit](./InterfacePhyViewAudit.md)
  - [diag](./InterfacePhyViewDiag.md)
  - [all](./InterfacePhyViewAll.md)
  - [verbose](./InterfacePhyViewVerbose.md)

Output options:
  - [default](./InterfacePhyOutputDefault.md)
  - [json](./InterfacePhyOutputJson.md)

Command options

```
# iserver get aci intf phy --help

Usage: iserver.py get aci intf phy [OPTIONS]

  Get aci node physical interface

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
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
  --ctx TEXT                      Filter by context
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|trans|vlan|epg|load|eee|nei|cdp|lldp|
                                  pg|pol|aaep|ether|err|qos|fault|hfault|event
                                  |audit|diag|all|verbose]  [default: state]
  --pivot                         Pivot view
  --no-cache                      Disable cache
  -o, --output [default|json]     [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 55 ms and logs saved in /tmp/iserver\37ff88fa4a4a
```

[[Back]](./README.md)