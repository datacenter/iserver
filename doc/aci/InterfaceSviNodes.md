# Node Interface - SVI

## Multiple nodes

```
# iserver get aci intf svi --apic apic11 --node cl

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/cl201-eu-spdc | vlan2     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl201-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl201-eu-spdc | vlan230   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl201-eu-spdc | vlan244   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl201-eu-spdc | vlan252   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl201-eu-spdc | vlan268   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl201-eu-spdc | vlan270   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl201-eu-spdc | vlan274   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl201-eu-spdc | vlan276   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl201-eu-spdc | vlan278   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl201-eu-spdc | vlan280   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl201-eu-spdc | vlan282   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl201-eu-spdc | vlan286   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl201-eu-spdc | vlan288   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl201-eu-spdc | vlan290   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl201-eu-spdc | vlan293   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl201-eu-spdc | vlan295   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl201-eu-spdc | vlan310   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl201-eu-spdc | vlan312   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl201-eu-spdc | vlan316   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl201-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl201-eu-spdc | vlan330   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl201-eu-spdc | vlan334   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl201-eu-spdc | vlan344   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl201-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl201-eu-spdc | vlan440   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/cl201-eu-spdc | vlan442   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl201-eu-spdc | vlan444   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl201-eu-spdc | vlan460   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl201-eu-spdc | vlan461   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl201-eu-spdc | vlan468   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl201-eu-spdc | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl201-eu-spdc | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl201-eu-spdc | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl201-eu-spdc | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl201-eu-spdc | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl201-eu-spdc | vlan474   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl201-eu-spdc | vlan479   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl201-eu-spdc | vlan480   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl201-eu-spdc | vlan481   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl201-eu-spdc | vlan487   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl201-eu-spdc | vlan489   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/cl201-eu-spdc | vlan492   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl201-eu-spdc | vlan493   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl201-eu-spdc | vlan494   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl201-eu-spdc | vlan495   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl201-eu-spdc | vlan496   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl201-eu-spdc | vlan497   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl201-eu-spdc | vlan498   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl201-eu-spdc | vlan499   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl201-eu-spdc | vlan58    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl201-eu-spdc | vlan60    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl201-eu-spdc | vlan74    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl201-eu-spdc | vlan80    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl201-eu-spdc | vlan88    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl201-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
| pod-1/cl202-eu-spdc | vlan12    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl202-eu-spdc | vlan14    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl202-eu-spdc | vlan146   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl202-eu-spdc | vlan148   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl202-eu-spdc | vlan150   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl202-eu-spdc | vlan152   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl202-eu-spdc | vlan164   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl202-eu-spdc | vlan182   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl202-eu-spdc | vlan186   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl202-eu-spdc | vlan192   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl202-eu-spdc | vlan282   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl202-eu-spdc | vlan284   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl202-eu-spdc | vlan316   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl202-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl202-eu-spdc | vlan362   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl202-eu-spdc | vlan388   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl202-eu-spdc | vlan390   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl202-eu-spdc | vlan410   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl202-eu-spdc | vlan412   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl202-eu-spdc | vlan414   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl202-eu-spdc | vlan416   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/cl202-eu-spdc | vlan420   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl202-eu-spdc | vlan422   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl202-eu-spdc | vlan424   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl202-eu-spdc | vlan426   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl202-eu-spdc | vlan428   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl202-eu-spdc | vlan430   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl202-eu-spdc | vlan432   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl202-eu-spdc | vlan434   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl202-eu-spdc | vlan437   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl202-eu-spdc | vlan439   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl202-eu-spdc | vlan441   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl202-eu-spdc | vlan465   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl202-eu-spdc | vlan466   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl202-eu-spdc | vlan467   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl202-eu-spdc | vlan468   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl202-eu-spdc | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl202-eu-spdc | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl202-eu-spdc | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl202-eu-spdc | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl202-eu-spdc | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl202-eu-spdc | vlan482   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl202-eu-spdc | vlan483   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl202-eu-spdc | vlan484   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl202-eu-spdc | vlan485   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl202-eu-spdc | vlan486   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl202-eu-spdc | vlan487   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl202-eu-spdc | vlan488   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl202-eu-spdc | vlan489   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl202-eu-spdc | vlan490   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl202-eu-spdc | vlan491   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl202-eu-spdc | vlan492   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl202-eu-spdc | vlan494   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl202-eu-spdc | vlan6     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl202-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node cl

{
    "duration": 3877,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 393,
        "disconnect_time": 0,
        "mo_time": 3090,
        "total_time": 3483
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

True	393	-	connect apic11o.emea-sp.cisco.com
True	307	13	apic11o.emea-sp.cisco.com class fabricNode
True	454	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	357	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	488	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	308	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	282	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	299	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	293	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	302	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
```

[[Back]](./InterfaceSvi.md)