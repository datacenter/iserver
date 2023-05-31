# Policy Link Level

Get default properties of [all](./PolicyLinkAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyLinkName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyLinkAll.md)
  - [usage](./PolicyLinkUsage.md)
  - [intf](./PolicyLinkIntf.md)
  - [verbose](./PolicyLinkVerbose.md)

Output options:
  - [default](./PolicyLinkAll.md)
  - [json](./PolicyLinkJson.md)

Command options

```
# iserver get aci policy link --help

Usage: iserver.py get aci policy link [OPTIONS]

  Get aci policy interface link

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

Info: finished in 26 ms and logs saved in /tmp/iserver\57c1f005bfe3
```

[[Back]](./README.md)