# Node Interface - Loopback

## Filter by ip address

```
# iserver get aci intf lb --apic apic11 --node any --ip 10.3.0.32

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

+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
| pod-1/bl205-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/bl206-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo1023    | up          | up         | 10.3.0.32/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo6       | up          | up         |              | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo5       | up          | up         |              | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+--------------+-------------+---------------------+
```

[[Back]](./InterfaceLoopback.md)