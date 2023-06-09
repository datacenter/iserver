# Policy Port Security

Get default properties of [all](./PolicyPortsecAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyPortsecName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyPortsecAll.md)
  - [usage](./PolicyPortsecUsage.md)
  - [intf](./PolicyPortsecIntf.md)
  - [verbose](./PolicyPortsecVerbose.md)

Output options:
  - [default](./PolicyPortsecAll.md)
  - [json](./PolicyPortsecJson.md)

Command options

```
# iserver get aci policy portsec --help

Usage: iserver.py get aci policy portsec [OPTIONS]

  Get aci policy interface port_security

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

Info: finished in 65 ms and logs saved in /tmp/iserver\2b5c06f223dc
```

[[Back]](./README.md)