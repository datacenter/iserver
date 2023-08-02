# Node Protocol - CDP

## Command options

Filter options:
  - [interface](./ProtocolCdpFilterInterface.md)
  - [system](./ProtocolCdpFilterSystem.md)
  - [platform](./ProtocolCdpFilterPlatform.md)
  - [capabilities](./ProtocolCdpFilterCapabilities.md)

View options:
  - [inst](./ProtocolCdpViewInstance.md)
  - [intf](./ProtocolCdpViewInterface.md)
  - [nei](./ProtocolCdpViewNeighbor.md)
  - [event](./ProtocolCdpViewEvent.md)
  - [all](./ProtocolCdpViewAll.md)

Output options:
  - [default](./ProtocolCdpOutputDefault.md)
  - [json](./ProtocolCdpOutputJson.md)

Command options

```
# iserver get aci proto cdp --help

Usage: iserver.py get aci proto cdp [OPTIONS]

  Get aci node protocol cdp

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --port INTEGER               APIC Port  [default: 443]
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --pod TEXT                   Pod ID
  --node TEXT                  Node name patterns
  --role [any|leaf|spine]      [default: any]
  --sys TEXT                   Filter by system name
  --platform TEXT              Filter by platform name
  --cap TEXT                   Filter by capabilities
  --intf TEXT                  Filter by interface name
  --when TEXT                  Filter faults by timestamp  [default: 7d]
  -v, --view TEXT              [inst|intf|nei|event|all]  [default: nei]
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 36 ms and logs saved in /tmp/iserver\0b4be1601ee9
```

[[Back]](./README.md)