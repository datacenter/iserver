# Policy CoPP

Get default properties of [all](./PolicyCoppAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyCoppName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyCoppAll.md)
  - [usage](./PolicyCoppUsage.md)
  - [intf](./PolicyCoppIntf.md)
  - [verbose](./PolicyCoppVerbose.md)

Output options:
  - [default](./PolicyCoppAll.md)
  - [json](./PolicyCoppJson.md)

Command options

```
# iserver get aci policy copp --help

Usage: iserver.py get aci policy copp [OPTIONS]

  Get aci policy interface copp

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

Info: finished in 121 ms and logs saved in /tmp/iserver\a1f5a10a7428
```

[[Back]](./README.md)