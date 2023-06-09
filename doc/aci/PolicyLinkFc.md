# Policy Link Level Flow Control

Get default properties of [all](./PolicyLinkFcAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyLinkFcName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyLinkFcAll.md)
  - [usage](./PolicyLinkFcUsage.md)
  - [intf](./PolicyLinkFcIntf.md)
  - [verbose](./PolicyLinkFcVerbose.md)

Output options:
  - [default](./PolicyLinkFcAll.md)
  - [json](./PolicyLinkFcJson.md)

Command options

```
# iserver get aci policy link-fc --help

Usage: iserver.py get aci policy link-fc [OPTIONS]

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
  -v, --view [default|usage|intf|verbose]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 41 ms and logs saved in /tmp/iserver\0a24533b8caf
```

[[Back]](./README.md)