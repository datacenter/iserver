# Policy - Port Channel Member

## Usage specific output

```
# iserver get aci policy lacp-m --apic apic11 --name default --view usage

Apic: apic11

+-------------+---------------------+-----------------+-----------------+-----------------+
| Policy Name | Node                | Interface Count | Ref Policy Type | Ref Policy Name |
+-------------+---------------------+-----------------+-----------------+-----------------+
| default     | pod-1/bl205-eu-spdc | 5               | Access Infra    | infra           | 
|             | pod-1/bl206-eu-spdc | 5               |                 |                 | 
|             | pod-1/cl201-eu-spdc | 28              |                 |                 | 
|             | pod-1/cl202-eu-spdc | 28              |                 |                 | 
|             | pod-1/rl301-eu-spdc | 2               |                 |                 | 
|             | pod-1/rl302-eu-spdc | 2               |                 |                 | 
+-------------+---------------------+-----------------+-----------------+-----------------+
Context: phy
```

Developer

```
# iserver get aci policy lacp-m --apic apic11 --name default --view usage

{
    "duration": 1493,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 403,
        "disconnect_time": 0,
        "mo_time": 934,
        "total_time": 1337
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

True	403	-	connect apic11o.emea-sp.cisco.com
True	294	1	apic11o.emea-sp.cisco.com class lacpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	339	70	apic11o.emea-sp.cisco.com class l1RsLacpIfPolCons
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLacpm.md)