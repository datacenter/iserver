# Policy Port Channel Member

Get default properties of [all](./PolicyLacpmAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyLacpmName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyLacpmAll.md)
  - [usage](./PolicyLacpmUsage.md)
  - [intf](./PolicyLacpmIntf.md)
  - [verbose](./PolicyLacpmVerbose.md)

Output options:
  - [default](./PolicyLacpmAll.md)
  - [json](./PolicyLacpmJson.md)

Command options

```
# iserver get aci policy lacp-m --help

Usage: iserver.py get aci policy lacp-m [OPTIONS]

  Get aci policy interface port_channel_member

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

Info: finished in 27 ms and logs saved in /tmp/iserver\6158bfc29a66
```

[[Back]](./README.md)