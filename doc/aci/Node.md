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

Output options:
  - [default](./NodeAll.md)
  - [intf](./NodeOutputIntf.md)
  - [ip](./NodeOutputIp.md)
  - [power](./NodeOutputPower.md)
  - [psu](./NodeOutputPsu.md)
  - [sensor](./NodeOutputSensor.md)
  - [temp](./NodeOutputTemp.md)
  - [json](./NodeOutputJson.md)

Command options

```
# iserver get aci node --help

Usage: iserver.py get aci node [OPTIONS]

  Get aci node

Options:
  --apic TEXT                     APIC name
  --ip TEXT                       APIC IP
  --username TEXT                 APIC Username
  --password TEXT                 APIC Password
  --pod TEXT                      Pod ID
  --role [any|controller|leaf|spine]
                                  [default: any]
  --id TEXT                       Filter by node id
  --name TEXT                     Filter by node name
  --model TEXT                    Filter by model
  --node-ip TEXT                  Filter by subnet with IP
  --node-subnet TEXT              Filter by subnet within subnet
  -o, --output [default|intf|ip|power|psu|sensor|temp|json]
                                  [default: default]
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 27 ms and logs saved in /tmp/iserver\3fcace495bb5
```

[[Back]](./README.md)