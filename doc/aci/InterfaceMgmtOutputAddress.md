# Node Interface - Management

## Address focused output

```
# iserver get aci intf mgmt --apic apic11 --node any -o addr

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

+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| Node                | Name  | Admin State | OperState | MAC Address       | IP Address      | Router MAC        |
+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:7E:83:F0 | 10.58.28.145/27 | 4C:71:0D:7E:83:F0 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | up        | 3C:13:CC:C9:EC:B0 | 10.58.28.146/27 | 3C:13:CC:C9:EC:B0 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | up        | 4C:71:0D:23:FA:38 | 10.58.28.141/27 | 4C:71:0D:23:FA:38 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | up        | 10:B3:D5:B5:62:1C | 10.58.28.142/27 | 10:B3:D5:B5:62:1C | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | up        | A0:B4:39:4A:2B:44 | 10.58.28.135/27 | A0:B4:39:4A:2B:44 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | up        | A0:B4:39:4A:2D:18 | 10.58.28.136/27 | A0:B4:39:4A:2D:18 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | up        | 4C:71:0D:55:D1:CC | 10.58.28.151/27 | 4C:71:0D:55:D1:CC | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | up        | 8C:94:1F:FA:54:20 | 10.58.28.152/27 | 8C:94:1F:FA:54:20 | 
+---------------------+-------+-------------+-----------+-------------------+-----------------+-------------------+
```

[[Back]](./InterfaceMgmt.md)