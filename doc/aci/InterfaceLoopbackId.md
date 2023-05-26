# Node Interface - Loopback

## Filter by interface id

```
# iserver get aci intf lb --apic apic11 --node any --id lo8

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

+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo8       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.6/32    | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 15.254.101.9/32    | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo8       | up          | up         | 172.24.3.15/32     | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo8       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| pod-1/s101-eu-spdc  | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| pod-1/s102-eu-spdc  | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

[[Back]](./InterfaceLoopback.md)