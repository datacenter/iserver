# Policy L2

Get default properties of [all](./PolicyL2All.md) policies in selected APIC.

Filter options:
  - [name](./PolicyL2Name.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyL2All.md)
  - [usage](./PolicyL2Usage.md)
  - [intf](./PolicyL2Intf.md)
  - [verbose](./PolicyL2Verbose.md)

Output options:
  - [default](./PolicyL2All.md)
  - [json](./PolicyL2Json.md)

Command options

```
# iserver get aci policy l2 --help

Usage: iserver.py get aci policy l2 [OPTIONS]

  Get aci policy interface l2

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

Info: finished in 34 ms and logs saved in /tmp/iserver\0f7ecfbef18d
```

[[Back]](./README.md)