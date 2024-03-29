# Node

Controller selection options:
  - [single apic](./NodeAll.md)
  - [multiple apic](./NodeDomain.md)

Filter options:
  - [role](./NodeRole.md)
  - [model](./NodeModel.md)
  - [node id](./NodeId.md)
  - [node name](./NodeName.md)
  - [ip](./NodeIp.md)
  - [subnet](./NodeSubnet.md)

View options:
  - [default](./NodeAll.md)
  - [intf](./NodeOutputIntf.md)
  - [ip](./NodeOutputIp.md)
  - [power](./NodeOutputPower.md)
  - [psu](./NodeOutputPsu.md)
  - [sensor](./NodeOutputSensor.md)
  - [temp](./NodeOutputTemp.md)

Output options:
  - [default](./NodeAll.md)
  - [json](./NodeOutputJson.md)

Command options

```
# iserver get aci node --help

Usage: iserver.py get aci node [OPTIONS]

  Get aci node

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --port INTEGER                  APIC Port  [default: 443]
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --role [any|controller|leaf|spine]
                                  [default: any]
  --id TEXT                       Filter by node id
  --name TEXT                     Filter by node name
  --model TEXT                    Filter by model
  --address TEXT                  Filter by subnet with IP
  --subnet TEXT                   Filter by subnet within subnet
  -v, --view TEXT                 [state|intf|ip|power|psu|sensor|temp|all]
                                  [default: state]
  -o, --output [default|json]     [default: default]
  --no-cache                      Disable cache
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 103 ms and logs saved in /tmp/iserver\6ecdacd80e77
```

[[Back]](./README.md)