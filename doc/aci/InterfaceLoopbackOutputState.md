# Node Interface - Loopback

## Default state output

```
# iserver get aci intf lb --apic apic11 --node cl201-eu-spdc

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/cl201-eu-spdc | lo0       | up          | up         | 10.3.192.67/32     | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1       | up          | up         | 172.16.11.232/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo2       | up          | up         | 10.3.40.67/32      | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo3       | up          | up         | 172.30.4.0/32      | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo4       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo5       | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo6       | up          | up         | 15.254.101.8/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo7       | up          | up         | 15.254.101.6/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.0/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo9       | up          | up         | 15.254.101.4/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo10      | up          | up         | 15.254.101.99/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo11      | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo12      | up          | up         | 15.254.101.2/32    | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo13      | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node cl201-eu-spdc

{
    "duration": 2098,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 1612,
        "total_time": 1999
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

True	387	-	connect apic11o.emea-sp.cisco.com
True	1033	13	apic11o.emea-sp.cisco.com class fabricNode
True	283	15	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	296	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)