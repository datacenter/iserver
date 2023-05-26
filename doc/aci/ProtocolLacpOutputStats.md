# Node Protocol - LACP

## Interface stats output

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc -o stats

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Id  | Name              | Admin State | Oper State | Interface | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 237335   | 237331   | 0            | 0           | 0           | 0                    | 0                    | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 237360   | 237359   | 0            | 0           | 0           | 0                    | 0                    | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 237345   | 237358   | 0            | 0           | 0           | 0                    | 0                    | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 237338   | 237355   | 0            | 0           | 0           | 0                    | 0                    | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 237354   | 237345   | 0            | 0           | 0           | 0                    | 0                    | 
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

[[Back]](./ProtocolLacp.md)