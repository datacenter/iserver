# Policy MCP

Get default properties of [all](./PolicyMcpAll.md) policies in selected APIC.

Filter options:
  - [name](./PolicyMcpName.md)
  - pod id
  - node name
  - reference policy name
  - unused
  - used

View options:
  - [default](./PolicyMcpAll.md)
  - [usage](./PolicyMcpUsage.md)
  - [intf](./PolicyMcpIntf.md)
  - [verbose](./PolicyMcpVerbose.md)

Output options:
  - [default](./PolicyMcpAll.md)
  - [json](./PolicyMcpJson.md)

Command options

```
# iserver get aci policy mcp --help

Usage: iserver.py get aci policy mcp [OPTIONS]

  Get aci policy interface mcp

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

Info: finished in 39 ms and logs saved in /tmp/iserver\1618eaf89f93
```

[[Back]](./README.md)