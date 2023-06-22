# System Fault

Get system faults.

Filter options:
  - [severity](./SystemFaultSeverity.md)
  - [domain](./SystemFaultDomain.md)
  - [type](./SystemFaultType.md)
  - [code](./SystemFaultCode.md)
  - [cause](./SystemFaultCause.md)
  - [object](./SystemFaultObject.md)
  - [description](./SystemFaultDescription.md)

View options:
  - [summary](./SystemFaultViewSummary.md)
  - [domain](./SystemFaultViewDomain.md)
  - [type](./SystemFaultViewType.md)
  - [verbose](./SystemFaultViewVerbose.md)

Output options:
  - [default](./SystemFaultOutputDefault.md)
  - [json](./SystemFaultOutputJson.md)

Command options

```
# iserver get aci system fault --help

Usage: iserver.py get aci system fault [OPTIONS]

  Get aci system fault

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --severity [any|critical|major|minor|warning]
                                  Filter by severity  [default: any]
  --domain [any|access|apps|ext|fw|infra|mgmt|sec|tenant]
                                  Filter by domain  [default: any]
  --type [any|env|comm|config|oper]
                                  Filter by type  [default: any]
  --code TEXT                     Filter by code
  --cause TEXT                    Filter by cause
  --object TEXT                   Filter by object
  --desc TEXT                     Filter by description
  -v, --view [summary|domain|type|verbose]
                                  [default: summary]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 102 ms and logs saved in /tmp/iserver\46b14591fa0f
```

[[Back]](./README.md)