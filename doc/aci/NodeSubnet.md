# Node

## Filter by ip subnet

```
# iserver get aci node --apic apic11 --node-subnet 172.16.0.0/16

Apic: apic11

+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address    | Admin State | Fabric State | Role        | Model          | Serial      | Version        |
+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
| pod-1/rl301-eu-spdc | 301     | 1      | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO2346137N | n9000-15.2(7f) | 
| pod-1/rl302-eu-spdc | 302     | 1      | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2 | FDO234613DB | n9000-15.2(7f) | 
+---------------------+---------+--------+---------------+-------------+--------------+-------------+----------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --node-subnet 172.16.0.0/16

{
    "duration": 1743,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 1332,
        "disconnect_time": 0,
        "mo_time": 294,
        "total_time": 1626
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

True	1332	-	connect apic11o.emea-sp.cisco.com
True	294	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)