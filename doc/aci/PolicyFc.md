# Policy Fibre Channel

Get default properties of [all](./PolicyFcAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyFcName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyFcAll.md)
  - [usage](./PolicyFcUsage.md)
  - [intf](./PolicyFcIntf.md)
  - [verbose](./PolicyFcVerbose.md)

Output options:
  - [default](./PolicyFcAll.md)
  - [json](./PolicyFcJson.md)

Command options

```
# iserver get aci policy fc --help

Usage: iserver.py get aci policy fc [OPTIONS]

  Get aci policy interface fc

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

Info: finished in 53 ms and logs saved in /tmp/iserver\e10c5d7ff31c
```

[[Back]](./README.md)