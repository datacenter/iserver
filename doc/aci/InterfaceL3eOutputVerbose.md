# Node Interface - Encapsulated Routed

## Verbose output

```
# iserver get aci intf l3e
    --apic apic11
    --node any
    --id eth1/36.83
    --view verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/36.83
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-2
- SR-MPLS            : no
- MTU                : 9366
- IP Unnumbered Intf : lo0
- Delay              : 1
- Router MAC         : 00:00:00:00:00:00
```

Developer

```
# iserver get aci intf l3e
    --apic apic11
    --node any
    --id eth1/36.83
    --view verbose

{
    "duration": 6290,
    "apic": {
        "read": true,
        "success": 18,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 17,
        "connect_time": 444,
        "disconnect_time": 0,
        "mo_time": 5444,
        "total_time": 5888
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

True	444	-	connect apic11o.emea-sp.cisco.com
True	307	11	apic11o.emea-sp.cisco.com class fabricNode
True	303	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	306	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	312	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	352	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	293	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	328	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	309	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	310	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	306	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	319	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	373	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	306	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	363	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	310	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	320	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	327	42	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)