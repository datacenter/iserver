# Node Protocol

## ND

View options:
- [inst](./ProtocolNdViewInstance.md)
- [dom](./ProtocolNdViewDomain.md)
- [intf](./ProtocolNdViewInterface.md)
- [nei](./ProtocolNdViewNeighbor.md)
- [fault](./ProtocolNdViewFault.md)
- [hfault](./ProtocolNdViewFaultHistory.md)
- [event](./ProtocolNdViewEvent.md)
- [diag](./ProtocolNdViewDiag.md)
- [all](./ProtocolNdViewAll.md)

Output options:
  - [default](./ProtocolNdOutputDefault.md)
  - [json](./ProtocolNdOutputJson.md)

Command options

```
# iserver get aci proto nd --help

Usage: iserver.py get aci proto nd [OPTIONS]

  Get aci node protocol nd

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [inst|dom|nei|intf|fault|hfault|event|diag|a
                                  ll]  [default: nei]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 49 ms and logs saved in /tmp/iserver\d0b6f932727d
```

[[Back]](./README.md)