# Policy Port Channel

Get default properties of [all](./PolicyLacpAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyLacpName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyLacpAll.md)
  - [usage](./PolicyLacpUsage.md)
  - [intf](./PolicyLacpIntf.md)
  - [verbose](./PolicyLacpVerbose.md)

Output options:
  - [default](./PolicyLacpAll.md)
  - [json](./PolicyLacpJson.md)

Command options

```
# iserver get aci policy lacp --help

Usage: iserver.py get aci policy lacp [OPTIONS]

  Get aci policy interface port_channel

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

Info: finished in 45 ms and logs saved in /tmp/iserver\b4fdb5222dd3
```

[[Back]](./README.md)