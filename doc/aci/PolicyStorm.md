# Policy Storm Control

Get default properties of [all](./PolicyStormAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyStormName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyStormAll.md)
  - [usage](./PolicyStormUsage.md)
  - [intf](./PolicyStormIntf.md)
  - [verbose](./PolicyStormVerbose.md)

Output options:
  - [default](./PolicyStormAll.md)
  - [json](./PolicyStormJson.md)

Command options

```
# iserver get aci policy storm --help

Usage: iserver.py get aci policy storm [OPTIONS]

  Get aci policy interface storm_control

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

Info: finished in 31 ms and logs saved in /tmp/iserver\240d36b8692a
```

[[Back]](./README.md)