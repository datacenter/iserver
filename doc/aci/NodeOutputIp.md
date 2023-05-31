# Node

## IP address specific output

```
# iserver get aci node --apic apic11 --node-ip 10.3.192.68

Apic: apic11

+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model            | Serial      | Version        |
+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
| pod-1/cl202-eu-spdc | 202     | 1      | 10.3.192.68 | on          | active       | leaf | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7f) | 
+---------------------+---------+--------+-------------+-------------+--------------+------+------------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --node-ip 10.3.192.68

{
    "duration": 797,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 306,
        "total_time": 703
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	306	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)