# Attachable Access Entity Profile (AAEP)

Get default properties of [all](./AaepAllDefault.md) AAEPs in selected APIC.

Filter options:
  - [name](./AaepName.md)

Output options:
  - [default](./AaepAllDefault.md)
  - [json](./AaepOutputJson.md)

Command options

```
# iserver get aci aaep --help

Usage: iserver.py get aci aaep [OPTIONS]

  Get aci aaep

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by profile name
  -o, --output [default|json]  [default: default]
  --no-cache                   Disable cache
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 35 ms and logs saved in /tmp/iserver\bbf33e10c5a3
```

[[Back]](./README.md)