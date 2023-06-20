# Application Endpoint Group (EPG)

Get default properties of selected EPGs.

Filter options:
  - [name](./ApplicationEpgName.md)
  - [tenant](./ApplicationEpgTenant.md)
  - [application profile](./ApplicationEpgProfile.md)
  - [pcTag](./ApplicationEpgPcTag.md)
  - [bridge domain](./ApplicationEpgBridgeDomain.md)
  - [subnet](./ApplicationEpgSubnet.md)
  - [IP address](./ApplicationEpgIp.md)
  - [contract](./ApplicationEpgContract.md)
  - [deployed node](./ApplicationEpgNode.md)
  - [domain](./ApplicationEpgDomain.md)
  - [leaf policy group](./ApplicationEpgPg.md)

View options:
  - [summary](./ApplicationEpgAllDefault.md)
  - [properties](./ApplicationEpgAllProperties.md)
  - [bridge domain details](./ApplicationEpgAllBridgeDomain.md)
  - [contract details](./ApplicationEpgAllContract.md)
  - [deployed node details](./ApplicationEpgAllNode.md)
  - [static port details](./ApplicationEpgAllPort.md)
  - [domain details](./ApplicationEpgAllDomain.md)
  - [member details](./ApplicationEpgAllMember.md)
  - [all details](./ApplicationEpgAllDetails.md)
  - [verbose](./ApplicationEpgVerbose.md)

Output options:
  - [default](./ApplicationEpgAllDefault.md)
  - [json](./ApplicationEpgJson.md)

Command options

```
# iserver get aci epg --help

Usage: iserver.py get aci epg [OPTIONS]

  Get aci epg

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --tenant TEXT                   Filter by tenant name
  --ap TEXT                       Filter by application profile name
  --name TEXT                     Filter by epg name
  --pctag TEXT                    Filter by pcTag
  --bd TEXT                       Filter by bridge domain name
  --subnet TEXT                   Filter by IP subnet
  --address TEXT                  Filter by IP address
  --contract TEXT                 Filter by contract name
  --node TEXT                     Filter by deployed node name
  --domain TEXT                   Filter by domain name
  --member [any|dyn|st]           [default: any]
  --pg TEXT                       Filter by policy group name
  -v, --view [summary|prop|bd|contract|ep|node|stport|domain|member|all|verbose]
                                  [default: summary]
  --pivot                         Pivot view
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 136 ms and logs saved in /tmp/iserver\7631b8922e6f
```

[[Back]](./README.md)