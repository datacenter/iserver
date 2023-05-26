# Node

## All nodes in multiple APICs

```
# iserver get aci node --apic dom:milan

Apic: apic11,apic21

+--------+----------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| Apic   | Node Name            | Node ID | Pod ID | IP Address    | Admin State | Fabric State | Role        | Model            | Serial      | Version        |
+--------+----------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
| apic11 | pod-1/apic1          | 1       | 1      | 10.3.0.1      | on          |              | controller  | APIC-SERVER-M3   | WZP234408RN | 5.2(7f)        | 
| apic11 | pod-1/apic2          | 2       | 1      | 10.3.0.2      | on          |              | controller  | APIC-SERVER-M3   | WZP234310FJ | 5.2(7f)        | 
| apic11 | pod-1/apic3          | 3       | 1      | 10.3.0.3      | on          |              | controller  | APIC-SERVER-M3   | WZP234408PR | 5.2(7f)        | 
| apic11 | pod-1/bl205-eu-spdc  | 205     | 1      | 10.3.192.64   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO233804F9 | n9000-15.2(7f) | 
| apic11 | pod-1/bl206-eu-spdc  | 206     | 1      | 10.3.32.64    | on          | active       | leaf        | N9K-C93600CD-GX  | FDO24300ZJH | n9000-15.2(7f) | 
| apic11 | pod-1/cl201-eu-spdc  | 201     | 1      | 10.3.192.67   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LNB | n9000-15.2(7f) | 
| apic11 | pod-1/cl202-eu-spdc  | 202     | 1      | 10.3.192.68   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO23350LJY | n9000-15.2(7f) | 
| apic11 | pod-1/rl301-eu-spdc  | 301     | 1      | 172.16.30.160 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO2346137N | n9000-15.2(7f) | 
| apic11 | pod-1/rl302-eu-spdc  | 302     | 1      | 172.16.30.120 | on          | active       | remote leaf | N9K-C9336C-FX2   | FDO234613DB | n9000-15.2(7f) | 
| apic11 | pod-1/s101-eu-spdc   | 101     | 1      | 10.3.192.65   | on          | active       | spine       | N9K-C9316D-GX    | FDO233806C2 | n9000-15.2(7f) | 
| apic11 | pod-1/s102-eu-spdc   | 102     | 1      | 10.3.32.65    | on          | active       | spine       | N9K-C9316D-GX    | FDO24350JND | n9000-15.2(7f) | 
| apic21 | pod-1/apic21         | 1       | 1      | 10.5.0.1      | on          |              | controller  | APIC-SERVER-M3   | WZP24171PHT | 5.2(7f)        | 
| apic21 | pod-1/apic22         | 2       | 1      | 10.5.0.2      | on          |              | controller  | APIC-SERVER-M3   | WMP2519006W | 5.2(7f)        | 
| apic21 | pod-1/apic23         | 3       | 1      | 10.5.0.3      | on          |              | controller  | APIC-SERVER-M3   | WZP24171PBD | 5.2(7f)        | 
| apic21 | pod-1/bl2205-eu-spdc | 2205    | 1      | 10.5.216.66   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO24280TYP | n9000-15.2(7f) | 
| apic21 | pod-1/bl2206-eu-spdc | 2206    | 1      | 10.5.216.64   | on          | active       | leaf        | N9K-C93600CD-GX  | FDO243707PU | n9000-15.2(7f) | 
| apic21 | pod-1/cl2201-eu-spdc | 2201    | 1      | 10.5.80.96    | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO2441006U | n9000-15.2(7f) | 
| apic21 | pod-1/cl2202-eu-spdc | 2202    | 1      | 10.5.216.67   | on          | active       | leaf        | N9K-C93360YC-FX2 | FDO24350A1T | n9000-15.2(7f) | 
| apic21 | pod-1/cl2207-eu-spdc | 2207    | 1      | 10.5.240.34   | on          | active       | leaf        | N9K-C9336C-FX2   | FDO23490E4G | n9000-15.2(7f) | 
| apic21 | pod-1/cl2208-eu-spdc | 2208    | 1      | 10.5.240.35   | on          | active       | leaf        | N9K-C9336C-FX2   | FDO234807ED | n9000-15.2(7f) | 
| apic21 | pod-1/rl2701-eu-spdc | 2701    | 1      | 172.16.70.208 | on          | active       | remote leaf | N9K-C93108TC-EX  | FDO21010LJC | n9000-15.2(7f) | 
| apic21 | pod-1/rl2702-eu-spdc | 2702    | 1      | 172.16.70.24  | on          | active       | remote leaf | N9K-C93108TC-EX  | FDO20501N3W | n9000-15.2(7f) | 
| apic21 | pod-1/s2101-eu-spdc  | 2101    | 1      | 10.5.80.97    | on          | active       | spine       | N9K-C9332D-GX2B  | FDO25500ZWG | n9000-15.2(7f) | 
| apic21 | pod-1/s2102-eu-spdc  | 2102    | 1      | 10.5.80.98    | on          | active       | spine       | N9K-C9332D-GX2B  | FDO25500ZVK | n9000-15.2(7f) | 
+--------+----------------------+---------+--------+---------------+-------------+--------------+-------------+------------------+-------------+----------------+
```

[[Back]](./Node.md)