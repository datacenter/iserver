# Policy - MCP

## Filter by name

```
# iserver get aci policy mcp --apic apic11 --name default

Apic: apic11 (mode:online, cache:off)

+-------------+----+-------------+------------+--------------+
| Policy Name | TF | Admin State | Interfaces | Ref Policies |
+-------------+----+-------------+------------+--------------+
| default     |    | enabled     | 464        | 81           | 
+-------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy mcp --apic apic11 --name default

{
    "duration": 1792,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 466,
        "disconnect_time": 0,
        "mo_time": 1034,
        "total_time": 1500
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

True	466	-	connect apic11o.emea-sp.cisco.com
True	331	3	apic11o.emea-sp.cisco.com class mcpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	384	470	apic11o.emea-sp.cisco.com class l1RsMcpIfPolCons
True	319	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyMcp.md)