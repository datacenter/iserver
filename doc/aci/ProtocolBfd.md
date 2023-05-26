# Node Protocol

## BFD

Node selection options:
  - [single node](./ProtocolBfdSessionNode.md)
  - [selected nodes](./ProtocolBfdSessionNodes.md)
  - [all nodes](./ProtocolBfdSessions.md)

Filter options:
  - [state](./ProtocolBfdSessionState.md)
  - [interface](./ProtocolBfdSessionInterface.md)
  - [session id](./ProtocolBfdSessionId.md)
  - [vrf](./ProtocolBfdSessionVrf.md)
  - [ip](./ProtocolBfdSessionIp.md)
  - [subnet](./ProtocolBfdSessionSubnet.md)

Output options:
  - [session](./ProtocolBfdSessionNode.md) (default)
  - [instance](./ProtocolBfdInstanceNodes.md)
  - [verbose](./ProtocolBfdSessionVerbose.md)
  - [json](./ProtocolBfdOutputJson.md)

Command options

```
# iserver get aci proto bfd --help

Usage: iserver.py get aci proto bfd [OPTIONS]

  Get aci node protocol bfd

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --node TEXT                     Node name patterns
  --role [any|leaf|spine]         [default: any]
  --id TEXT                       Filter by session id
  --intf TEXT                     Filter by interface id
  --state [any|up|down]           Filter by session state  [default: any]
  --vrf TEXT                      Filter by VRF name
  --ip TEXT                       Filter by IP address
  --subnet TEXT                   Filter by IP subnet
  -o, --output [session|instance|verbose|json]
                                  [default: session]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 67 ms and logs saved in /tmp/iserver\7520c3204383
```

[[Back]](./Protocol.md)