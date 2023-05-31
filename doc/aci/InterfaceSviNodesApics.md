# Node Interface - SVI

## Multi-APIC

```
# iserver get aci intf svi --apic dom:milan --node any --type ext

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-----------+-------------+------------+-----------+-------------+--------+-----------+------+----------------+
| Apic   | Node                 | Interface | Admin State | Oper State | Reason    | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+--------+----------------------+-----------+-------------+------------+-----------+-------------+--------+-----------+------+----------------+
| apic11 | pod-1/bl205-eu-spdc  | vlan35    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| apic11 | pod-1/bl205-eu-spdc  | vlan61    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| apic11 | pod-1/bl205-eu-spdc  | vlan63    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan39    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan41    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan42    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan452   | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan455   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan456   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan457   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan458   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan459   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan460   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan461   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan462   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan463   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan464   | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan467   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan468   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan469   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan470   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan471   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan472   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan473   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan474   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan475   | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan476   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan477   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan478   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan479   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan480   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan481   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan482   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan483   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan484   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan487   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan488   | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan489   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan490   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan491   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan492   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan493   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan494   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan495   | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan22    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan23    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan24    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan25    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan21    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan22    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan23    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan40    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| apic21 | pod-1/bl2205-eu-spdc | vlan2     | up          | down       | vlan-down | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/bl2205-eu-spdc | vlan3     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/bl2206-eu-spdc | vlan1     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/bl2206-eu-spdc | vlan20    | up          | down       | vlan-down | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan21    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040469 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan22    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269820 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan6     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15662985 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan2     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15040469 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan3     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15662985 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan4     | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269820 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan27    | up          | down       | vlan-down | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan28    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan44    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15040476 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan45    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-14942183 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan46    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15237056 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan47    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15269821 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan25    | up          | up         |           | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan26    | up          | down       | vlan-down | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan42    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15237056 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan43    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15269821 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan44    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-14942183 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan45    | up          | up         |           | bd-external | bcast  | no        | 1500 | vxlan-15040476 | 
+--------+----------------------+-----------+-------------+------------+-----------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic dom:milan --node any --type ext

{
    "duration": 15900,
    "apic": {
        "read": true,
        "success": 40,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 38,
        "connect_time": 834,
        "disconnect_time": 0,
        "mo_time": 13909,
        "total_time": 14743
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

True	423	-	connect apic11o.emea-sp.cisco.com
True	411	-	connect apic21o.emea-sp.cisco.com
True	311	11	apic11o.emea-sp.cisco.com class fabricNode
True	324	13	apic21o.emea-sp.cisco.com class fabricNode
True	424	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	304	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	388	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	322	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	573	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	346	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	600	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	403	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	384	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	299	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	388	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	316	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	443	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	539	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	330	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	308	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
True	453	10	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	290	23	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/ipv4Addr
True	339	10	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	332	23	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/ipv4Addr
True	416	19	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	345	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/ipv4Addr
True	361	19	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	314	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/ipv4Addr
True	396	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	333	30	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/ipv4Addr
True	364	20	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	315	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/ipv4Addr
True	398	5	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	310	13	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/ipv4Addr
True	351	6	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	313	14	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/ipv4Addr
True	288	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	346	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/ipv4Addr
True	321	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	322	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)