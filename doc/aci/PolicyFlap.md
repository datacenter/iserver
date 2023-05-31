# Policy Link Flap

Get default properties of [all](./PolicyFlapAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyFlapName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyFlapAll.md)
  - [usage](./PolicyFlapUsage.md)
  - [intf](./PolicyFlapIntf.md)
  - [verbose](./PolicyFlapVerbose.md)

Output options:
  - [default](./PolicyFlapAll.md)
  - [json](./PolicyFlapJson.md)

Command options

```
# iserver get aci policy flap --help

Usage: iserver.py get aci policy flap [OPTIONS]

  Get aci policy interface flap

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
  -o, --output [default|json]     [default: default]
  -v, --view [default|usage|intf|verbose]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 28 ms and logs saved in /tmp/iserver\68c9ded707af
```

[[Back]](./README.md)