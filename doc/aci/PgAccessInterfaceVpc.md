# Policy Group

## Access Interface VPC

Filter options:
  - [name](./PgAccessInterfaceVpcName.md)
  - [aaep](./PgAccessInterfaceVpcAaep.md)

View options:
  - [default](./PgAccessInterfaceVpcOutputPolicy.md)
  - [aaep](./PgAccessInterfaceVpcOutputAaep.md)
  - [node](./PgAccessInterfaceVpcOutputNode.md)
  - [port](./PgAccessInterfaceVpcOutputPort.md)

Output options:
  - [default](./PgAccessInterfaceVpcOutputPolicy.md)
  - [json](./PgAccessInterfaceVpcOutputJson.md)

Command options

```
# iserver get aci pg access intf vpc --help

Usage: iserver.py get aci pg access intf vpc [OPTIONS]

  Get aci policy group interface vpc

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by name
  --aaep TEXT                     Filter by aaep
  --policy TEXT                   Filter by policy
  -v, --view [default|aaep|node|port]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 127 ms and logs saved in /tmp/iserver\26b9531aa319
```

[[Back]](./PgAccessInterface.md)