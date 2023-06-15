# Policy - MCP

## Get all policies

```
# iserver get aci policy mcp --apic apic11

Apic: apic11 (mode:online, cache:off)

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| default      |    | enabled     | 464        | 81           | 
| mcp-enabled  |    | enabled     | 4          | 3            | 
| nidemo-dummy |    | enabled     | 2          | 1            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy mcp --apic apic11

{
    "duration": 1814,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 1048,
        "total_time": 1478
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

True	430	-	connect apic11o.emea-sp.cisco.com
True	327	3	apic11o.emea-sp.cisco.com class mcpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	397	470	apic11o.emea-sp.cisco.com class l1RsMcpIfPolCons
True	324	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyMcp.md)