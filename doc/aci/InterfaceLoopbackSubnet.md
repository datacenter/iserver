# Node Interface - Loopback

## Filter by ip subnet

```
# iserver get aci intf lb --apic apic11 --node any --subnet 15.0.0.0/8

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

+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| Node                | Interface | Admin State | Oper State | IPv4 Address      | Last Errors | Current Error Index |
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
| pod-1/cl201-eu-spdc | lo6       | up          | up         | 15.254.101.8/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo7       | up          | up         | 15.254.101.2/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo8       | up          | up         | 15.254.101.6/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo10      | up          | up         | 15.254.101.99/32  | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo11      | up          | up         | 15.254.101.4/32   | 0           | 4294967295          | 
| pod-1/cl201-eu-spdc | lo13      | up          | up         | 15.254.101.0/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo6       | up          | up         | 15.254.101.3/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo7       | up          | up         | 15.254.101.1/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo8       | up          | up         | 15.254.101.9/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo11      | up          | up         | 15.254.101.7/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo12      | up          | up         | 15.254.101.5/32   | 0           | 4294967295          | 
| pod-1/cl202-eu-spdc | lo13      | up          | up         | 15.254.101.100/32 | 0           | 4294967295          | 
| pod-1/rl301-eu-spdc | lo6       | up          | up         |                   | 0           | 4294967295          | 
| pod-1/rl302-eu-spdc | lo5       | up          | up         |                   | 0           | 4294967295          | 
+---------------------+-----------+-------------+------------+-------------------+-------------+---------------------+
```

[[Back]](./InterfaceLoopback.md)