# Node Protocol - LACP

## Verbose output

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc -o verbose

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

LACP Instance
-------------
- Node                    : pod-1/bl205-eu-spdc
- Admin State             : enabled
- System MAC              : 4C:71:0D:7E:84:C0
- Admin Priority          : 32768
- Oper Priority           : 32768
- Port Channel Interfaces : 5/0/5


+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id  | Name              | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+

+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| Id  | Name              | Admin State | Oper State | Interface | PDU Sent | PDU Recv | PDU Recv Err | Marker Sent | Marker Recv | Marker Response Sent | Marker Response Recv |
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 237335   | 237331   | 0            | 0           | 0           | 0                    | 0                    | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 237360   | 237359   | 0            | 0           | 0           | 0                    | 0                    | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 237345   | 237358   | 0            | 0           | 0           | 0                    | 0                    | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 237338   | 237355   | 0            | 0           | 0           | 0                    | 0                    | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 237354   | 237346   | 0            | 0           | 0           | 0                    | 0                    | 
+-----+-------------------+-------------+------------+-----------+----------+----------+--------------+-------------+-------------+----------------------+----------------------+
```

[[Back]](./ProtocolLacp.md)