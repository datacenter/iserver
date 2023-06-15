# Policy - Link Level

## Get all policies

```
# iserver get aci policy link --apic apic11

Apic: apic11 (mode:online, cache:off)

+-----------------------------+----+----------+----------+---------+--------------+----------------------+---------------+-------------+------------+--------------+
| Policy Name                 | TF | PHY Type | Auto Neg | Speed   | Delay [msec] | Link Debounce [msec] | FEC Mode      | EMI Retrain | Interfaces | Ref Policies |
+-----------------------------+----+----------+----------+---------+--------------+----------------------+---------------+-------------+------------+--------------+
| 100G-auto                   |    | auto     | on       | 100G    | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| 100g-fix                    |    | auto     | off      | 100G    | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| 100G-fixed                  |    | auto     | on       | 100G    | 0            | 100                  | auto-fec      | disable     | 0          | 0            | 
| 10G-auto                    |    | auto     | on       | inherit | 0            | 100                  | inherit       | disable     | 0          | 1            | 
| 10G-fix                     |    | auto     | off      | 10G     | 0            | 100                  | inherit       | disable     | 18         | 8            | 
| 10G-fix-FEC                 |    | auto     | off      | 10G     | 0            | 100                  | cons16-rs-fec | disable     | 0          | 0            | 
| 1G-auto                     |    | auto     | on       | 1G      | 0            | 100                  | inherit       | disable     | 4          | 1            | 
| 1G-fix                      |    | auto     | off      | 1G      | 0            | 100                  | inherit       | disable     | 4          | 1            | 
| 25G-auto                    |    | auto     | on       | 25G     | 0            | 100                  | ieee-rs-fec   | disable     | 0          | 0            | 
| 25G-fix                     |    | auto     | off      | 25G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| 25G-fix-FEC                 |    | auto     | off      | inherit | 0            | 100                  | cl91-rs-fec   | disable     | 4          | 2            | 
| 40G-auto                    |    | auto     | on       | 40G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| 40G-fix                     |    | auto     | off      | 40G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| default                     |    | auto     | on       | inherit | 0            | 100                  | inherit       | disable     | 395        | 54           | 
| fabric-inherit              |    | auto     | off      | inherit | 0            | 100                  | inherit       | disable     | 4          | 3            | 
| inherit                     |    | auto     | off      | inherit | 0            | 100                  | inherit       | disable     | 33         | 0            | 
| Inherit                     |    | auto     | on       | inherit | 0            | 100                  | inherit       | disable     | 33         | 16           | 
| nidemo-dummy                |    | auto     | on       | inherit | 0            | 100                  | inherit       | disable     | 2          | 1            | 
| pod2A-25G-cl74-fc           |    | auto     | on       | 25G     | 0            | 100                  | cl74-fc-fec   | disable     | 0          | 0            | 
| pod2A-25G-cl91-rs           |    | auto     | on       | 25G     | 0            | 100                  | cl91-rs-fec   | disable     | 0          | 0            | 
| podZZ-25G-cl74-fc           |    | auto     | on       | 25G     | 0            | 100                  | cl74-fc-fec   | disable     | 0          | 0            | 
| podZZ-25G-cl91-rs           |    | auto     | on       | 25G     | 0            | 100                  | cl91-rs-fec   | disable     | 0          | 0            | 
| system-link-level-100G-auto |    | auto     | on       | 100G    | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-100M-auto |    | auto     | on       | 100M    | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-10G-auto  |    | auto     | on       | 10G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-1G-auto   |    | auto     | on       | 1G      | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-25G-auto  |    | auto     | on       | 25G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-400G-auto |    | auto     | on       | 400G    | 0            | 100                  | inherit       | disable     | 0          | 0            | 
| system-link-level-40G-auto  |    | auto     | on       | 40G     | 0            | 100                  | inherit       | disable     | 0          | 0            | 
+-----------------------------+----+----------+----------+---------+--------------+----------------------+---------------+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy link --apic apic11

{
    "duration": 2029,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 434,
        "disconnect_time": 0,
        "mo_time": 1101,
        "total_time": 1535
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

True	434	-	connect apic11o.emea-sp.cisco.com
True	345	29	apic11o.emea-sp.cisco.com class fabricHIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	403	464	apic11o.emea-sp.cisco.com class l1RsHIfPolCons
True	353	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLink.md)