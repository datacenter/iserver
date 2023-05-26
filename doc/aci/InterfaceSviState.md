# Node Interface - SVI

## Filter by state

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc --oper up

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106014 | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15531940 | 
| pod-1/bl205-eu-spdc | vlan14    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/bl205-eu-spdc | vlan16    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942188 | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811132 | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/bl205-eu-spdc | vlan24    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15597468 | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335346 | 
| pod-1/bl205-eu-spdc | vlan26    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/bl205-eu-spdc | vlan28    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106012 | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15499182 | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/bl205-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/bl205-eu-spdc | vlan4     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942189 | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909413 | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/bl205-eu-spdc | vlan46    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/bl205-eu-spdc | vlan48    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/bl205-eu-spdc | vlan50    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/bl205-eu-spdc | vlan55    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14778362 | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| pod-1/bl205-eu-spdc | vlan63    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| pod-1/bl205-eu-spdc | vlan69    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/bl205-eu-spdc | vlan7     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

[[Back]](./InterfaceSvi.md)