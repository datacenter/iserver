# Policy Group

## Access Interface - Leaf Access Port

Filter options:
  - [name](./PgAccessInterfacePortName.md)
  - [aaep](./PgAccessInterfacePortAaep.md)

View options:
  - [default](./PgAccessInterfacePortOutputPolicy.md)
  - [aaep](./PgAccessInterfacePortOutputAaep.md)

Output options:
  - [default](./PgAccessInterfacePortOutputPolicy.md)
  - [json](./PgAccessInterfacePortOutputJson.md)

Command options

```
# iserver get aci pg access intf port --help

Usage: iserver.py get aci pg access intf port [OPTIONS]

  Get aci policy group interface port

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by name
  --aaep TEXT                  Filter by aaep
  -v, --view [default|aaep]
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 32 ms and logs saved in /tmp/iserver\2160df1dc50f
```

[[Back]](./PgAccessInterface.md)