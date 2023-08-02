# L2 Out

## Command options

Filter options:
  - [name](./L2OutFilterName.md)
  - [tenant](./L2OutFilterTenant.md)

View options:
  - [state](./L2OutViewState.md)
  - [node](./L2OutViewNode.md)
  - [intf](./L2OutViewIntf.md)
  - [fault](./L2OutViewFault.md)
  - [hfault](./L2OutViewFaultHistory.md)
  - [event](./L2OutViewEvent.md)
  - [audit](./L2OutViewAudit.md)
  - [diag](./L2OutViewDiag.md)
  - [all](./L2OutViewAll.md)

Output options:
  - [default](./L2OutOutputDefault.md)
  - [json](./L2OutOutputJson.md)

Command options

```
# iserver get aci l2out --help

Usage: iserver.py get aci l2out [OPTIONS]

  Get aci l2out

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by application profile name
  --tenant TEXT                   Filter by tenant name
  --fault                         Filter with faults
  --severity [any|critical|major|minor|warning]
                                  Filter faults by severity  [default: any]
  --when TEXT                     Filter faults by timestamp  [default: 7d]
  -v, --view TEXT                 [state|node|intf|fault|hfault|event|audit|di
                                  ag|all]  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\8d2278bd46d1
```

[[Back]](./README.md)