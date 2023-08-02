# Node Protocol - LLDP

## Command options

Filter options:
  - [device](./ProtocolLldpFilterDevice.md)
  - [mac](./ProtocolLldpFilterMac.md)
  - [server](./ProtocolLldpFilterServer.md)

View options:
  - [inst](./ProtocolLldpViewInstance.md)
  - [nei](./ProtocolLldpViewNeighbor.md)
  - [stats](./ProtocolLldpViewStats.md)
  - [fault](./ProtocolLldpViewFault.md)
  - [hfault](./ProtocolLldpViewFaultHistory.md)
  - [event](./ProtocolLldpViewEvent.md)
  - [diag](./ProtocolLldpViewDiag.md)
  - [all](./ProtocolLldpViewAll.md)

Output options:
  - [default](./ProtocolLldpOutputDefault.md)
  - [json](./ProtocolLldpOutputJson.md)

Command options

```
# iserver get aci proto lldp --help

Usage: iserver.py get aci proto lldp [OPTIONS]

  Get aci node protocol lldp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --device TEXT                   Filter neighbor by device name
  --mac TEXT                      Filter neighbor by mac address
  --xd TEXT                       Cross domain filter
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [inst|nei|stats|fault|hfault|event|diag|all]
                                  [default: nei]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 59 ms and logs saved in /tmp/iserver\9f46049f8620
```

[[Back]](./README.md)