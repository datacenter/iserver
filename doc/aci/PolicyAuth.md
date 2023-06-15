# Policy 802.1X

Get default properties of [all](./PolicyAuthAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyAuthName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyAuthAll.md)
  - [usage](./PolicyAuthUsage.md)
  - [intf](./PolicyAuthIntf.md)
  - [verbose](./PolicyAuthVerbose.md)

Output options:
  - [default](./PolicyAuthAll.md)
  - [json](./PolicyAuthJson.md)

Command options

```
# iserver get aci policy auth --help

Usage: iserver.py get aci policy auth [OPTIONS]

  Get aci policy interface 802.1x

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

Info: finished in 53 ms and logs saved in /tmp/iserver\b6b4b5655776
```

[[Back]](./README.md)