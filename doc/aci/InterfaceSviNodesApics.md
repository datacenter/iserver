# Node Interface - SVI

## Multi-APIC

```
# iserver get aci intf svi --apic dom:milan --node any --type ext

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
Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Apic   | Node                 | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+--------+----------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| apic11 | pod-1/bl205-eu-spdc  | vlan49    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| apic11 | pod-1/bl205-eu-spdc  | vlan56    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| apic11 | pod-1/bl205-eu-spdc  | vlan67    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan53    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan57    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| apic11 | pod-1/bl206-eu-spdc  | vlan58    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan460   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan461   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan468   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan474   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan479   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan480   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan492   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan493   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan494   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan495   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan496   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan497   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan498   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| apic11 | pod-1/cl201-eu-spdc  | vlan499   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan465   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan466   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan467   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan468   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan482   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan483   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan484   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan485   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan486   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan487   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan488   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan489   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan490   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| apic11 | pod-1/cl202-eu-spdc  | vlan491   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan22    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan23    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan24    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| apic11 | pod-1/rl301-eu-spdc  | vlan25    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan22    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan23    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan24    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| apic11 | pod-1/rl302-eu-spdc  | vlan25    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| apic21 | pod-1/bl2205-eu-spdc | vlan3     | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/bl2205-eu-spdc | vlan4     | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/bl2206-eu-spdc | vlan5     | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/bl2206-eu-spdc | vlan6     | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan22    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269820 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan23    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15662985 | 
| apic21 | pod-1/cl2201-eu-spdc | vlan24    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040469 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan26    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040469 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan27    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15662985 | 
| apic21 | pod-1/cl2202-eu-spdc | vlan28    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269820 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan29    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan30    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan31    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14942183 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan32    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15269821 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan33    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15040476 | 
| apic21 | pod-1/cl2207-eu-spdc | vlan34    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15237056 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan25    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15269817 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan26    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15105996 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan27    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15040476 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan28    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15237056 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan29    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15269821 | 
| apic21 | pod-1/cl2208-eu-spdc | vlan30    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14942183 | 
+--------+----------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic dom:milan --node any --type ext

{
    "duration": 17016,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 46,
        "connect_time": 791,
        "disconnect_time": 0,
        "mo_time": 15024,
        "total_time": 15815
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	299	13	apic11o.emea-sp.cisco.com class fabricNode
True	391	-	connect apic21o.emea-sp.cisco.com
True	320	15	apic21o.emea-sp.cisco.com class fabricNode
True	410	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	307	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	425	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	348	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	449	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	312	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	441	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	309	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	292	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	317	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	298	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	298	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	378	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	300	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	357	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	283	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	289	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	296	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	292	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	297	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
True	419	10	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	294	24	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/ipv4Addr
True	325	10	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	313	24	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/ipv4Addr
True	379	19	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	307	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/ipv4Addr
True	365	19	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	284	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/ipv4Addr
True	368	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	294	30	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/ipv4Addr
True	342	20	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	298	29	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/ipv4Addr
True	340	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	363	3	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/ipv4Addr
True	301	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	301	3	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/ipv4Addr
True	311	5	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	308	13	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/ipv4Addr
True	327	6	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	284	14	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/ipv4Addr
True	293	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	304	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/ipv4Addr
True	295	0	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	292	21	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)