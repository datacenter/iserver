# Policy LLDP

Get default properties of [all](./PolicyLldpAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyLldpName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyLldpAll.md)
  - [usage](./PolicyLldpUsage.md)
  - [intf](./PolicyLldpIntf.md)
  - [verbose](./PolicyLldpVerbose.md)

Output options:
  - [default](./PolicyLldpAll.md)
  - [json](./PolicyLldpJson.md)

Command options

```
# iserver get aci policy lldp --help

Usage: iserver.py get aci policy lldp [OPTIONS]

  Get aci policy interface lldp

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by policy name
  --pod TEXT                      Filter by pod id
  --node TEXT                     Filter by node name
  --ref TEXT                      Filter by ref policy name
  --unused                        Filter unused
  --used                          Filter used
  -v, --view [default|usage|intf|verbose]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 53 ms and logs saved in /tmp/iserver\0f0373f72cbc
```

[[Back]](./README.md)