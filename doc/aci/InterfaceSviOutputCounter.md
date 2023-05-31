# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view counter

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
| Node                | Interface | Admin State | Oper State | Pkts In    | Pkts Out   | Mcast In | Mcast Out | Disc In | Disc Out | Err In | Err Out |
+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan14    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan16    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan24    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan26    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan28    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan34    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | 71250295   | 107484666  | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan4     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan46    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan48    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan50    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan55    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 4395942297 | 3523875933 | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan63    | up          | up         | 50783561   | 40546197   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan69    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan7     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --view counter

{
    "duration": 2638,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 778,
        "disconnect_time": 0,
        "mo_time": 1535,
        "total_time": 2313
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
    }
}

Log: apic
----------

True	778	-	connect apic11o.emea-sp.cisco.com
True	474	11	apic11o.emea-sp.cisco.com class fabricNode
True	750	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	311	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
```

[[Back]](./InterfaceSvi.md)