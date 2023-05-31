# Policy - MCP

## Filter by name

```
# iserver get aci policy mcp --apic apic11 --name default

Apic: apic11

+-------------+----+-------------+------------+--------------+
| Policy Name | TF | Admin State | Interfaces | Ref Policies |
+-------------+----+-------------+------------+--------------+
| default     |    | enabled     | 408        | 81           | 
+-------------+----+-------------+------------+--------------+
Context: phy
```

Developer

```
# iserver get aci policy mcp --apic apic11 --name default

{
    "duration": 1550,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 412,
        "disconnect_time": 0,
        "mo_time": 1040,
        "total_time": 1452
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

True	412	-	connect apic11o.emea-sp.cisco.com
True	325	3	apic11o.emea-sp.cisco.com class mcpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	394	414	apic11o.emea-sp.cisco.com class l1RsMcpIfPolCons
True	321	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyMcp.md)