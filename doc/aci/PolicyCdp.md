# Policy CDP

Get default properties of [all](./PolicyAuthAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyCdpName.md)
  - [node](./PolicyCdpNode.md)
  - [reference policy name](./PolicyCdpRef.md)
  - [unused](./PolicyCdpUnused.md)
  - [used](./PolicyCdpUsed.md)

View options:
  - [default](./PolicyCdpAll.md)
  - [usage](./PolicyCdpUsage.md)
  - [intf](./PolicyCdpIntf.md)
  - [verbose](./PolicyCdpVerbose.md)

Output options:
  - [default](./PolicyCdpAll.md)
  - [json](./PolicyCdpJson.md)

Command options

```
# iserver get aci policy cdp --help

Usage: iserver.py get aci policy cdp [OPTIONS]

  Get aci policy interface cdp

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

Info: finished in 30 ms and logs saved in /tmp/iserver\f820562c3cfc
```

[[Back]](./README.md)