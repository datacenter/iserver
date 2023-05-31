# Node Interface - SVI

## Multiple nodes

```
# iserver get aci intf svi --apic apic11 --node cl

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/cl201-eu-spdc | vlan103   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl201-eu-spdc | vlan105   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl201-eu-spdc | vlan109   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl201-eu-spdc | vlan111   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl201-eu-spdc | vlan113   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl201-eu-spdc | vlan141   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl201-eu-spdc | vlan22    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl201-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl201-eu-spdc | vlan345   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl201-eu-spdc | vlan347   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl201-eu-spdc | vlan349   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/cl201-eu-spdc | vlan351   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl201-eu-spdc | vlan353   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl201-eu-spdc | vlan358   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl201-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl201-eu-spdc | vlan360   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl201-eu-spdc | vlan362   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/cl201-eu-spdc | vlan366   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl201-eu-spdc | vlan380   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl201-eu-spdc | vlan430   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl201-eu-spdc | vlan432   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl201-eu-spdc | vlan452   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl201-eu-spdc | vlan455   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl201-eu-spdc | vlan456   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl201-eu-spdc | vlan457   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl201-eu-spdc | vlan458   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl201-eu-spdc | vlan459   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl201-eu-spdc | vlan460   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl201-eu-spdc | vlan461   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl201-eu-spdc | vlan462   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl201-eu-spdc | vlan463   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl201-eu-spdc | vlan464   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl201-eu-spdc | vlan467   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl201-eu-spdc | vlan468   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl201-eu-spdc | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl201-eu-spdc | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl201-eu-spdc | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl201-eu-spdc | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl201-eu-spdc | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl201-eu-spdc | vlan474   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl201-eu-spdc | vlan489   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl201-eu-spdc | vlan493   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl201-eu-spdc | vlan495   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl201-eu-spdc | vlan501   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl201-eu-spdc | vlan52    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl201-eu-spdc | vlan58    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl201-eu-spdc | vlan62    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl201-eu-spdc | vlan64    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl201-eu-spdc | vlan67    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl201-eu-spdc | vlan69    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl201-eu-spdc | vlan73    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl201-eu-spdc | vlan77    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl201-eu-spdc | vlan79    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl201-eu-spdc | vlan81    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl201-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
| pod-1/cl201-eu-spdc | vlan93    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl202-eu-spdc | vlan100   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl202-eu-spdc | vlan102   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl202-eu-spdc | vlan104   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl202-eu-spdc | vlan106   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl202-eu-spdc | vlan156   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl202-eu-spdc | vlan22    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl202-eu-spdc | vlan24    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl202-eu-spdc | vlan247   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl202-eu-spdc | vlan249   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl202-eu-spdc | vlan251   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl202-eu-spdc | vlan253   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl202-eu-spdc | vlan255   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl202-eu-spdc | vlan261   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl202-eu-spdc | vlan263   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl202-eu-spdc | vlan28    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl202-eu-spdc | vlan285   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl202-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl202-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl202-eu-spdc | vlan371   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl202-eu-spdc | vlan421   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl202-eu-spdc | vlan475   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl202-eu-spdc | vlan476   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl202-eu-spdc | vlan477   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl202-eu-spdc | vlan478   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl202-eu-spdc | vlan479   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl202-eu-spdc | vlan480   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl202-eu-spdc | vlan481   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl202-eu-spdc | vlan482   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl202-eu-spdc | vlan483   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl202-eu-spdc | vlan484   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl202-eu-spdc | vlan485   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl202-eu-spdc | vlan487   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl202-eu-spdc | vlan488   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl202-eu-spdc | vlan489   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl202-eu-spdc | vlan490   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl202-eu-spdc | vlan491   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl202-eu-spdc | vlan492   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl202-eu-spdc | vlan493   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl202-eu-spdc | vlan494   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl202-eu-spdc | vlan495   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl202-eu-spdc | vlan496   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl202-eu-spdc | vlan498   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl202-eu-spdc | vlan52    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl202-eu-spdc | vlan54    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl202-eu-spdc | vlan6     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl202-eu-spdc | vlan62    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl202-eu-spdc | vlan64    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl202-eu-spdc | vlan72    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl202-eu-spdc | vlan76    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl202-eu-spdc | vlan78    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl202-eu-spdc | vlan84    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl202-eu-spdc | vlan88    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl202-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
| pod-1/cl202-eu-spdc | vlan92    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl202-eu-spdc | vlan98    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node cl

{
    "duration": 2820,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 414,
        "disconnect_time": 0,
        "mo_time": 2043,
        "total_time": 2457
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

True	414	-	connect apic11o.emea-sp.cisco.com
True	329	11	apic11o.emea-sp.cisco.com class fabricNode
True	598	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	322	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	478	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	316	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
```

[[Back]](./InterfaceSvi.md)