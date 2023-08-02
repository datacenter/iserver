# Node Interface - Virtual Port Channel (VPC)

## Addr view

```
# iserver get aci intf vpc --apic apic21 --node bl2205-eu-spdc --view addr

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Virtual Port Channel - Address [#1]
---------------------------------------------

+----------------------+--------+----------------+-------------------+-------------------+------------+----------------+-------------------+-----------+
| Node                 | Domain | VPC IP         | VPC MAC           | Local MAC         | Local Prio | Peer IP        | Peer MAC          | Peer Prio |
+----------------------+--------+----------------+-------------------+-------------------+------------+----------------+-------------------+-----------+
| pod-1/bl2205-eu-spdc | 256    | 10.5.192.65/32 | 00:23:04:EE:BF:00 | 3C:13:CC:B9:EE:80 | 2205       | 10.5.216.64/32 | 64:3A:EA:DA:B2:10 | 2206      | 
+----------------------+--------+----------------+-------------------+-------------------+------------+----------------+-------------------+-----------+
```

Developer

```
# iserver get aci intf vpc --apic apic21 --node bl2205-eu-spdc --view addr

{
    "duration": 1772,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 361,
        "disconnect_time": 0,
        "mo_time": 1234,
        "total_time": 1595
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	361	-	connect apic21o.emea-sp.cisco.com:443
True	266	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	286	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	425	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	257	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
```

[[Back]](./InterfaceVpc.md)