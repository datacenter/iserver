# Node Protocol - HSRP

## Command options

Filter options:
  - [vrf](./ProtocolHsrpFilterVrf.md)

View options:
  - [inst](./ProtocolHsrpViewInstance.md)
  - [dom](./ProtocolHsrpViewDomain.md)
  - [intf](./ProtocolHsrpViewInterface.md)
  - [fault](./ProtocolHsrpViewFault.md)
  - [hfault](./ProtocolHsrpViewFaultHistory.md)
  - [event](./ProtocolHsrpViewEvent.md)
  - [diag](./ProtocolHsrpViewDiag.md)
  - [all](./ProtocolHsrpViewAll.md)

Output options:
  - [default](./ProtocolHsrpOutputDefault.md)
  - [json](./ProtocolHsrpOutputJson.md)

Command options

```
# iserver get aci proto hsrp --help

Usage: iserver.py get aci proto hsrp [OPTIONS]

  Get aci node protocol hsrp

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --port INTEGER               APIC Port  [default: 443]
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --pod TEXT                   Pod ID
  --node TEXT                  Node name patterns
  --role [any|leaf|spine]      [default: any]
  --vrf TEXT                   Filter by VRF name
  --id TEXT                    Filter by neighbor
  --when TEXT                  Filter faults by timestamp  [default: 7d]
  -v, --view TEXT              [inst|dom|intf|fault|hfault|event|diag|all]
                               [default: inst]
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\b2816db3e300
```

[[Back]](./README.md)