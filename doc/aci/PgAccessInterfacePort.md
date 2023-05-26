# Policy Group

## Access Interface - Leaf Access Port

Filter options:
  - [name](./PgAccessInterfacePortName.md)
  - [aaep](./PgAccessInterfacePortAaep.md)

Output options:
  - [policy](./PgAccessInterfacePortOutputPolicy.md) (default)
  - [aaep](./PgAccessInterfacePortOutputAaep.md)
  - [json](./PgAccessInterfacePortOutputJson.md)

Command options

```
# iserver get aci pg access intf port --help

Usage: iserver.py get aci pg access intf port [OPTIONS]

  Get aci policy group interface port

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by name
  --aaep TEXT                     Filter by aaep
  -o, --output [policy|aaep|json]
                                  [default: policy]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 37 ms and logs saved in /tmp/iserver\f6a1a1f4237c
```

[[Back]](./PgAccessInterface.md)