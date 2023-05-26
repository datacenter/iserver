# Application Profile (AP)

Get default properties of [all](./ApplicationProfileAll.md) Application Profiles in selected APIC.

Filter options:
  - [name](./ApplicationProfileName.md)
  - [tenant](./ApplicationProfileTenant.md)
  - [epg](./ApplicationProfileEpg.md)

Output options:
  - [default](./ApplicationProfileAll.md)
  - [json](./ApplicationProfileJson.md)

Command options

```
# iserver get aci ap --help

Usage: iserver.py get aci ap [OPTIONS]

  Get aci application profile

Options:
  --apic TEXT                  APIC name
  --ip TEXT                    APIC IP
  --username TEXT              APIC Username
  --password TEXT              APIC Password
  --name TEXT                  Filter by application profile name
  --tenant TEXT                Filter by tenant name
  --epg TEXT                   Filter by epg name
  -o, --output [default|json]  [default: default]
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 29 ms and logs saved in /tmp/iserver\ad1c8b09239c
```

[[Back]](./README.md)