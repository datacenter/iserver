# Node Interface - SVI

## Verbose output

```
# iserver get aci intf svi --apic apic11 --node bl205-eu-spdc -o counter

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
| Node                | Interface | Admin State | Oper State | Pkts In    | Pkts Out   | Mcast In | Mcast Out | Disc In | Disc Out | Err In | Err Out |
+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan14    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan16    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan24    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan26    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan28    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan34    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | 58571760   | 82864264   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan4     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan41    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan46    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan48    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan50    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan53    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan55    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | 3732452734 | 2991666515 | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan63    | up          | up         | 50772453   | 40522670   | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan69    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan7     | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | 0          | 0          | 0        | 0         | 0       | 0        | 0      | 0       | 
+---------------------+-----------+-------------+------------+------------+------------+----------+-----------+---------+----------+--------+---------+
```

[[Back]](./InterfaceSvi.md)