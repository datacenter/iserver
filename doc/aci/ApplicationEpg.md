# Application Endpoint Group (EPG)

Get default properties of [all](./ApplicationEpgAllDefault.md) EPGs in selected APIC.

Filter options:
  - [name](./ApplicationEpgName.md)
  - [tenant](./ApplicationEpgTenant.md)
  - [application profile](./ApplicationEpgProfile.md)
  - [bridge domain](./ApplicationEpgBridgeDomain.md)
  - [subnet](./ApplicationEpgSubnet.md)
  - [IP address](./ApplicationEpgIp.md)
  - [deployed node](./ApplicationEpgNode.md)
  - [contract](./ApplicationEpgContract.md)

Output options:
  - [default output](./ApplicationEpgAllDefault.md)
  - [properties](./ApplicationEpgAllProperties.md)
  - [with bridge domain details](./ApplicationEpgAllBridgeDomain.md)
  - [with contract details](./ApplicationEpgAllContract.md)
  - [with deployed node details](./ApplicationEpgAllNode.md)
  - [verbose](./ApplicationEpgVerbose.md)
  - [json](./ApplicationEpg.md) output

Command options

```
# iserver get aci epg --help

Usage: iserver.py get aci epg [OPTIONS]

  Get aci epg

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by epg name
  --tenant TEXT                   Filter by tenant name
  --app TEXT                      Filter by application profile name
  --bd TEXT                       Filter by bridge domain name
  --subnet TEXT                   Filter by IP subnet
  --ip TEXT                       Filter by IP address
  --node TEXT                     Filter by deployed node name
  --contract TEXT                 Filter by contract name
  -o, --output [default|prop|bd|contract|node|json|verbose]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 31 ms and logs saved in /tmp/iserver\cafd86ac2b4d
```

[[Back]](./README.md)