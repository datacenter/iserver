# Policy - MCP

## Get all policies

```
# iserver get aci policy mcp --apic apic11

Apic: apic11

+--------------+----+-------------+------------+--------------+
| Policy Name  | TF | Admin State | Interfaces | Ref Policies |
+--------------+----+-------------+------------+--------------+
| default      |    | enabled     | 408        | 81           | 
| mcp-enabled  |    | enabled     | 4          | 3            | 
| nidemo-dummy |    | enabled     | 2          | 1            | 
+--------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy mcp --apic apic11

{
    "duration": 1611,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 1080,
        "total_time": 1477
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
True	365	3	apic11o.emea-sp.cisco.com class mcpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	418	414	apic11o.emea-sp.cisco.com class l1RsMcpIfPolCons
True	297	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyMcp.md)