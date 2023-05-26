# Node Protocol - LACP

## Show LACP interface for selected node

```
# iserver get aci proto lacp --apic apic11 --node bl205-eu-spdc -o intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id  | Name              | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1 | HX1-FI-B_PolGrp   | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po2 | SPN_PolGrp        | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po3 | UCSB1-FI-B_PolGrp | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4 | HX1-FI-A_PolGrp   | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po5 | UCSB1-FI-A_PolGrp | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
+-----+-------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

[[Back]](./ProtocolLacp.md)