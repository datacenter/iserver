# Policy - L2

## Usage specific output

```
# iserver get aci policy l2 --apic apic11 --name default --view usage

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------------+------------------+--------------------+
| Policy Name | Node                | Interface Count | Ref Policy Type  | Ref Policy Name    |
+-------------+---------------------+-----------------+------------------+--------------------+
| default     | pod-1/bl205-eu-spdc | 16              | PC/VPC Interface | NXOS_FABRIC_PolGrp | 
|             | pod-1/bl206-eu-spdc | 21              | PC/VPC Interface | pod4a-MX_PolGrp    | 
|             | pod-1/cl201-eu-spdc | 44              |                  |                    | 
|             | pod-1/cl202-eu-spdc | 48              |                  |                    | 
|             | pod-1/cl209-eu-spdc | 28              |                  |                    | 
|             | pod-1/cl210-eu-spdc | 28              |                  |                    | 
|             | pod-1/rl301-eu-spdc | 24              |                  |                    | 
|             | pod-1/rl302-eu-spdc | 24              |                  |                    | 
+-------------+---------------------+-----------------+------------------+--------------------+
Context: phy
```

Developer

```
# iserver get aci policy l2 --apic apic11 --name default --view usage

{
    "duration": 1925,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 429,
        "disconnect_time": 0,
        "mo_time": 1068,
        "total_time": 1497
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

True	429	-	connect apic11o.emea-sp.cisco.com
True	343	6	apic11o.emea-sp.cisco.com class l2IfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	410	470	apic11o.emea-sp.cisco.com class l1RsL2IfPolCons
True	315	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyL2.md)