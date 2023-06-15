# Node Interface - Encapsulated Routed

## Verbose output

```
# iserver get aci intf l3e --apic apic11 --node any --id eth1/24* --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.46
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-24
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.47
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-20
- SR-MPLS            : no
- MTU                : 1500
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.48
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-14
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:14:05


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.50
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-15
- SR-MPLS            : no
- MTU                : 9216
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.51
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-23
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.52
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-21
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.53
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-25
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.54
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-11
- SR-MPLS            : no
- MTU                : 9216
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:22:05


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.55
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-22
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.54
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-20
- SR-MPLS            : no
- MTU                : 1500
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.55
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-14
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:14:06


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.56
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-24
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.59
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-11
- SR-MPLS            : no
- MTU                : 9216
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:22:05


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.60
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-15
- SR-MPLS            : no
- MTU                : 9216
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.61
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-21
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.62
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-23
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.63
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-25
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF


Encapsulated Routed Interface
-----------------------------
- Interface          : eth1/24.64
- Admin State        : up
- Oper State         : up
- Reason             : 
- Encap              : vlan-22
- SR-MPLS            : no
- MTU                : 9000
- IP Unnumbered Intf : 
- Delay              : 1
- Router MAC         : 00:22:BD:F8:19:FF
```

Developer

```
# iserver get aci intf l3e --apic apic11 --node any --id eth1/24* --view verbose

{
    "duration": 7109,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 6185,
        "total_time": 6567
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

True	382	-	connect apic11o.emea-sp.cisco.com
True	295	13	apic11o.emea-sp.cisco.com class fabricNode
True	288	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	297	66	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4If
True	277	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	294	68	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4If
True	292	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	328	75	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4If
True	293	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	283	74	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4If
True	288	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	287	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4If
True	280	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	286	11	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4If
True	310	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	333	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4If
True	289	6	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	294	49	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4If
True	293	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	294	44	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4If
True	287	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l3EncRtdIf query rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf
True	297	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4If
```

[[Back]](./InterfaceL3e.md)