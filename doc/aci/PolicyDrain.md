# Policy Slow Drain

Get default properties of [all](./PolicyDrainAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyDrainName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyDrainAll.md)
  - [usage](./PolicyDrainUsage.md)
  - [intf](./PolicyDrainIntf.md)
  - [verbose](./PolicyDrainVerbose.md)

Output options:
  - [default](./PolicyDrainAll.md)
  - [json](./PolicyDrainJson.md)

Command options

```
# iserver get aci policy drain --help

Usage: iserver.py get aci policy drain [OPTIONS]

  Get aci policy interface slow drain

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

Info: finished in 34 ms and logs saved in /tmp/iserver\8a9877515350
```

[[Back]](./README.md)