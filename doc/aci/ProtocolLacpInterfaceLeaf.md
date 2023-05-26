# Node Protocol - LACP

## Show LACP interfaces for all leaf nodes

```
# iserver get aci proto lacp --apic apic11 --role leaf -o intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| Id   | Name                     | Admin State | Oper State | Interface | Oper Key | Nbr System MAC | Nbr System Prio | Nbr Oper Key | Nbr Port | Nbr Port Prio | Nbr Port State |
+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
| po1  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po2  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po3  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po5  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
| po1  | HX1-FI-A_PolGrp          | up          | up         | eth1/11   | 32769    | None           | None            | None         | None     | None          | None           | 
| po2  | HX1-FI-B_PolGrp          | up          | up         | eth1/12   | 32770    | None           | None            | None         | None     | None          | None           | 
| po3  | UCSB1-FI-B_PolGrp        | up          | up         | eth1/2    | 33111    | None           | None            | None         | None     | None          | None           | 
| po4  | UCSB1-FI-A_PolGrp        | up          | up         | eth1/1    | 32771    | None           | None            | None         | None     | None          | None           | 
| po5  | SPN_PolGrp               | up          | up         | eth1/27   | 33112    | None           | None            | None         | None     | None          | None           | 
| po1  | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | None           | None            | None         | None     | None          | None           | 
| po2  | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | None           | None            | None         | None     | None          | None           | 
| po3  | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | None           | None            | None         | None     | None          | None           | 
| po4  | pod1a-MX_PolGrp          | up          | up         | eth1/23   | 33454    | None           | None            | None         | None     | None          | None           | 
| po5  | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | None           | None            | None         | None     | None          | None           | 
| po6  | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | None           | None            | None         | None     | None          | None           | 
| po7  | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | None           | None            | None         | None     | None          | None           | 
| po8  | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | None           | None            | None         | None     | None          | None           | 
| po9  | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | None           | None            | None         | None     | None          | None           | 
| po10 | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | None           | None            | None         | None     | None          | None           | 
| po11 | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | None           | None            | None         | None     | None          | None           | 
| po12 | pod1a-NVBench_PolGrp     | up          | down       |           |          |                |                 |              |          |               |                | 
| po13 | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | None           | None            | None         | None     | None          | None           | 
| po14 | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | None           | None            | None         | None     | None          | None           | 
| po15 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | None           | None            | None         | None     | None          | None           | 
| po16 | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | None           | None            | None         | None     | None          | None           | 
| po17 | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | None           | None            | None         | None     | None          | None           | 
| po18 | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | None           | None            | None         | None     | None          | None           | 
| po19 | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | None           | None            | None         | None     | None          | None           | 
| po20 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | None           | None            | None         | None     | None          | None           | 
| po21 | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | None           | None            | None         | None     | None          | None           | 
| po22 | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | None           | None            | None         | None     | None          | None           | 
| po23 | pod4a-MX_PolGrp          | up          | up         | eth1/67   | 33452    | None           | None            | None         | None     | None          | None           | 
| po24 | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | None           | None            | None         | None     | None          | None           | 
| po25 | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | None           | None            | None         | None     | None          | None           | 
| po26 | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | None           | None            | None         | None     | None          | None           | 
| po27 | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | None           | None            | None         | None     | None          | None           | 
| po28 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | None           | None            | None         | None     | None          | None           | 
| po1  | pod4a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/55   | 32789    | None           | None            | None         | None     | None          | None           | 
| po2  | pod4a-AIO-1-PET_PolGrp   | up          | up         | eth1/50   | 32783    | None           | None            | None         | None     | None          | None           | 
| po3  | pod4a-COMP-3-PET_PolGrp  | up          | up         | eth1/65   | 32781    | None           | None            | None         | None     | None          | None           | 
| po4  | pod4a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/52   | 32784    | None           | None            | None         | None     | None          | None           | 
| po5  | pod4a-COMP-2-SAMX_PolGrp | up          | up         | eth1/61   | 32792    | None           | None            | None         | None     | None          | None           | 
| po6  | pod4a-COMP-2-PET_PolGrp  | up          | up         | eth1/62   | 32793    | None           | None            | None         | None     | None          | None           | 
| po7  | pod4a-AIO-2-PET_PolGrp   | up          | up         | eth1/53   | 33464    | None           | None            | None         | None     | None          | None           | 
| po8  | pod4a-COMP-3-SAMX_PolGrp | up          | up         | eth1/64   | 33463    | None           | None            | None         | None     | None          | None           | 
| po9  | Infra_PolGrp             | up          | up         | eth1/96   | 33111    | None           | None            | None         | None     | None          | None           | 
| po10 | pod4a-COMP-1-PET_PolGrp  | up          | up         | eth1/59   | 32791    | None           | None            | None         | None     | None          | None           | 
| po11 | pod4a-AIO-3-PET_PolGrp   | up          | up         | eth1/56   | 32790    | None           | None            | None         | None     | None          | None           | 
| po12 | pod4a-COMP-1-SAMX_PolGrp | up          | up         | eth1/58   | 33465    | None           | None            | None         | None     | None          | None           | 
| po13 | pod4a-MX_PolGrp          | up          | down       |           |          |                |                 |              |          |               |                | 
| po14 | pod-4a-br-API            | up          | up         | eth1/68   | 33119    | None           | None            | None         | None     | None          | None           | 
| po15 | pod4a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/49   | 32782    | None           | None            | None         | None     | None          | None           | 
| po16 | pod1a-AIO-3-PET_PolGrp   | up          | up         | eth1/8    | 33122    | None           | None            | None         | None     | None          | None           | 
| po17 | pod1a-COMP-2-PET_PolGrp  | up          | up         | eth1/14   | 33124    | None           | None            | None         | None     | None          | None           | 
| po18 | pod1a-COMP-1-PET_PolGrp  | up          | up         | eth1/11   | 33123    | None           | None            | None         | None     | None          | None           | 
| po19 | pod1a-AIO-1-SAMX_PolGrp  | up          | up         | eth1/1    | 32794    | None           | None            | None         | None     | None          | None           | 
| po20 | pod1a-AIO-1-PET_PolGrp   | up          | up         | eth1/2    | 33120    | None           | None            | None         | None     | None          | None           | 
| po21 | pod1a-AIO-3-SAMX_PolGrp  | up          | up         | eth1/7    | 33121    | None           | None            | None         | None     | None          | None           | 
| po22 | pod1a-AIO-2-PET_PolGrp   | up          | up         | eth1/5    | 32795    | None           | None            | None         | None     | None          | None           | 
| po23 | pod1a-AIO-2-SAMX_PolGrp  | up          | up         | eth1/4    | 33456    | None           | None            | None         | None     | None          | None           | 
| po24 | pod1a-MX_PolGrp          | up          | down       |           |          |                |                 |              |          |               |                | 
| po25 | pod1a-NVBench_PolGrp     | up          | down       |           |          |                |                 |              |          |               |                | 
| po26 | pod1a-API_PolGrp         | up          | up         | eth1/24   | 33453    | None           | None            | None         | None     | None          | None           | 
| po27 | pod1a-COMP-1-SAMX_PolGrp | up          | up         | eth1/10   | 33457    | None           | None            | None         | None     | None          | None           | 
| po28 | pod1a-COMP-2-SAMX_PolGrp | up          | up         | eth1/13   | 32796    | None           | None            | None         | None     | None          | None           | 
| po1  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
| po2  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po1  | UCSB1-R3DC-FI-B_PolGrp   | up          | up         | eth1/4    | 32775    | None           | None            | None         | None     | None          | None           | 
| po2  | UCSB1-R3DC-FI-A_PolGrp   | up          | up         | eth1/3    | 32776    | None           | None            | None         | None     | None          | None           | 
+------+--------------------------+-------------+------------+-----------+----------+----------------+-----------------+--------------+----------+---------------+----------------+
```

[[Back]](./ProtocolLacp.md)