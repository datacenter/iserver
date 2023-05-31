# Policy Priority Flow Control

Get default properties of [all](./PolicyPfcAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyPfcName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyPfcAll.md)
  - [usage](./PolicyPfcUsage.md)
  - [intf](./PolicyPfcIntf.md)
  - [verbose](./PolicyPfcVerbose.md)

Output options:
  - [default](./PolicyPfcAll.md)
  - [json](./PolicyPfcJson.md)

Command options

```
# iserver get aci policy pfc --help

Usage: iserver.py get aci policy pfc [OPTIONS]

  Get aci policy interface pfc

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

Info: finished in 29 ms and logs saved in /tmp/iserver\15446a96569c
```

[[Back]](./README.md)