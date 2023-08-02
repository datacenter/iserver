# Node Protocol - CDP

## Command options

View options:
  - [inst](./ProtocolLacpViewInstance.md)
  - [intf](./ProtocolLacpViewInterface.md)
  - [stats](./ProtocolLacpViewStats.md)
  - [event](./ProtocolLacpViewEvent.md)
  - [all](./ProtocolLacpViewAll.md)

Output options:
  - [default](./ProtocolLacpOutputDefault.md)
  - [json](./ProtocolLacpOutputJson.md)

Command options

```
# iserver get aci proto lacp --help

Usage: iserver.py get aci proto lacp [OPTIONS]

  Get aci node protocol lacp

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --port INTEGER               APIC Port  [default: 443]
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --pod TEXT                   Pod ID
  --node TEXT                  Node name patterns
  --role [any|leaf|spine]      [default: any]
  --when TEXT                  Filter faults by timestamp  [default: 7d]
  -v, --view TEXT              [inst|intf|stats|event|all]  [default: intf]
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 80 ms and logs saved in /tmp/iserver\53d1c020bea3
```

[[Back]](./README.md)