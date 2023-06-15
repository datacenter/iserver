# Policy Spanning Tree

Get default properties of [all](./PolicyStpAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyStpName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyStpAll.md)
  - [usage](./PolicyStpUsage.md)
  - [intf](./PolicyStpIntf.md)
  - [verbose](./PolicyStpVerbose.md)

Output options:
  - [default](./PolicyStpAll.md)
  - [json](./PolicyStpJson.md)

Command options

```
# iserver get aci policy stp --help

Usage: iserver.py get aci policy stp [OPTIONS]

  Get aci policy interface stp

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

Info: finished in 66 ms and logs saved in /tmp/iserver\9fc6fc7aca13
```

[[Back]](./README.md)