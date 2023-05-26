# Node Interface - Encapsulated Routed

## Verbose output

```
# iserver get aci intf l3e --apic apic11 --node any --id eth1/36.83 -o verbose

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

[[Back]](./InterfaceL3e.md)