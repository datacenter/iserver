# Node

## Filter by role

Example: controller

```
# iserver get aci node --apic apic11 --role controller

Apic: apic11 (mode:online, cache:off)

+-------------+---------+--------+------------+-------------+--------------+------------+----------------+-------------+---------+
| Node Name   | Node ID | Pod ID | IP Address | Admin State | Fabric State | Role       | Model          | Serial      | Version |
+-------------+---------+--------+------------+-------------+--------------+------------+----------------+-------------+---------+
| pod-1/apic1 | 1       | 1      | 10.3.0.1   | on          | N/A          | controller | APIC-SERVER-M3 | WZP234408RN | 5.2(7g) | 
| pod-1/apic2 | 2       | 1      | 10.3.0.2   | on          | N/A          | controller | APIC-SERVER-M3 | WZP234310FJ | 5.2(7g) | 
| pod-1/apic3 | 3       | 1      | 10.3.0.3   | on          | N/A          | controller | APIC-SERVER-M3 | WZP234408PR | 5.2(7g) | 
+-------------+---------+--------+------------+-------------+--------------+------------+----------------+-------------+---------+
```

Example: spine

```
# iserver get aci node --apic apic11 --role spine

Apic: apic11 (mode:online, cache:off)

+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| Node Name          | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role  | Model         | Serial      | Version        |
+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
| pod-1/s101-eu-spdc | 101     | 1      | 10.3.192.65 | on          | active       | spine | N9K-C9316D-GX | FDO233806C2 | n9000-15.2(7g) | 
| pod-1/s102-eu-spdc | 102     | 1      | 10.3.32.65  | on          | active       | spine | N9K-C9316D-GX | FDO24350JND | n9000-15.2(7g) | 
+--------------------+---------+--------+-------------+-------------+--------------+-------+---------------+-------------+----------------+
```

Example: leaf

```
# iserver get aci node --apic apic11 --role leaf

Apic: apic11 (mode:online, cache:off)

+---------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| Node Name           | Node ID | Pod ID | IP Address    | Admin State | Fabric State | Role        | Model            | Serial      | Version        |
+---------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| pod-1/bl205-eu-spdc | 205     | 1      | 10.3.192.64   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO233804F9 | n9000-15.2(7g) | 
| pod-1/bl206-eu-spdc | 206     | 1      | 10.3.32.64    | on          | active       | leaf        | N9K-C93600CD-GX  | FDO24300ZJH | n9000-15.2(7g) | 
| pod-1/cl201-eu-spdc | 201     | 1      | 10.3.192.67   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LNB | n9000-15.2(7g) | 
| pod-1/cl202-eu-spdc | 202     | 1      | 10.3.192.68   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7g) | 
| pod-1/cl209-eu-spdc | 209     | 1      | 10.3.136.64   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO27023V1Z | n9000-15.2(7f) | 
| pod-1/cl210-eu-spdc | 210     | 1      | 10.3.136.65   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO27023V4G | n9000-15.2(7f) | 
| pod-1/rl301-eu-spdc | 301     | 1      | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO2346137N | n9000-15.2(7g) | 
| pod-1/rl302-eu-spdc | 302     | 1      | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO234613DB | n9000-15.2(7g) | 
+---------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
```

Developer

```
# iserver get aci node --apic apic11 --role leaf

{
    "duration": 964,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 457,
        "disconnect_time": 0,
        "mo_time": 347,
        "total_time": 804
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

True	457	-	connect apic11o.emea-sp.cisco.com
True	347	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./Node.md)