# Policy Transceiver

Get default properties of [all](./PolicyTransAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyTransName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyTransAll.md)
  - [usage](./PolicyTransUsage.md)
  - [intf](./PolicyTransIntf.md)
  - [verbose](./PolicyTransVerbose.md)

Output options:
  - [default](./PolicyTransAll.md)
  - [json](./PolicyTransJson.md)

Command options

```
# iserver get aci policy transceiver --help

Usage: iserver.py get aci policy transceiver [OPTIONS]

  Get aci policy interface transceiver

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --name TEXT                     Filter by policy name
  --pod TEXT                      Filter by pod id
  --node TEXT                     Filter by node name
  --unused                        Filter unused
  --used                          Filter used
  -v, --view [default|usage|intf|verbose]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 36 ms and logs saved in /tmp/iserver\399909da1ded
```

[[Back]](./README.md)