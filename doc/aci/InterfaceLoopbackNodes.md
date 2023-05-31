# Node Interface - Loopback

## Multiple nodes

```
# iserver get aci intf lb --apic apic11 --node bl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo0       | up          | up         | 10.3.192.64/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo1       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo2       | up          | up         | 172.16.11.233/32   | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo3       | up          | up         | 172.31.2.25/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo4       | up          | up         | 115.115.115.115/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo5       | up          | up         | 172.24.0.15/32     | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo6       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo7       | up          | up         | 172.24.0.253/32    | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo9       | up          | up         | 205.205.205.25/32  | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo10      | up          | up         | 205.205.205.15/32  | 0           | 4294967295          | 
| pod-1/bl205-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo0       | up          | up         | 10.3.32.64/32      | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo2       | up          | up         | 172.16.11.237/32   | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo3       | up          | up         | 172.31.2.26/32     | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo4       | up          | up         | 116.116.116.116/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo5       | up          | up         | 124.124.124.124/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo6       | up          | up         | 172.24.0.14/32     | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo7       | up          | up         | 172.24.0.252/32    | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo8       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo9       | up          | up         | 118.118.118.118/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo10      | up          | up         | 120.120.120.120/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo11      | up          | up         | 206.206.206.25/32  | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo12      | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo13      | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo14      | up          | up         | 206.206.206.15/32  | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

Developer

```
# iserver get aci intf lb --apic apic11 --node bl

{
    "duration": 2233,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 405,
        "disconnect_time": 0,
        "mo_time": 1609,
        "total_time": 2014
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

True	405	-	connect apic11o.emea-sp.cisco.com
True	324	11	apic11o.emea-sp.cisco.com class fabricNode
True	306	12	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	300	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	316	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3LbRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf
True	363	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
```

[[Back]](./InterfaceLoopback.md)