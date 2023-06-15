# Policy DPP

Get default properties of [all](./PolicyDppAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyDppName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyDppAll.md)
  - [usage](./PolicyDppUsage.md)
  - [intf](./PolicyDppIntf.md)
  - [verbose](./PolicyDppVerbose.md)

Output options:
  - [default](./PolicyDppAll.md)
  - [json](./PolicyDppJson.md)

Command options

```
# iserver get aci policy dpp --help

Usage: iserver.py get aci policy dpp [OPTIONS]

  Get aci policy interface dpp

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

Info: finished in 32 ms and logs saved in /tmp/iserver\2be47146b7ba
```

[[Back]](./README.md)