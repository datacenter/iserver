# Node Protocol - LACP

## Show LACP interface for selected nodes

```
# iserver get aci proto lacp --apic apic11 --node rl -o intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id  | Name                   | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
| po2 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po1 | UCSB1-R3DC-FI-B_PolGrp | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po2 | UCSB1-R3DC-FI-A_PolGrp | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
+-----+------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

[[Back]](./ProtocolLacp.md)