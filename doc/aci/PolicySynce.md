# Policy Synchronous Ethernet

Get default properties of [all](./PolicySynceAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicySynceName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicySynceAll.md)
  - [usage](./PolicySynceUsage.md)
  - [intf](./PolicySynceIntf.md)
  - [verbose](./PolicySynceVerbose.md)

Output options:
  - [default](./PolicySynceAll.md)
  - [json](./PolicySynceJson.md)

Command options

```
# iserver get aci policy synce --help

Usage: iserver.py get aci policy synce [OPTIONS]

  Get aci policy interface synce

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

Info: finished in 162 ms and logs saved in /tmp/iserver\ccaafeca9763
```

[[Back]](./README.md)