# Node Interface - Loopback

## Multi-APIC

```
# iserver get aci intf lb --apic dom:milan --node any

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| Apic   | Node                 | Interface | Admin State | Oper State | IPv4 Address       | Last Errors | Current Error Index |
+--------+----------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
| apic11 | pod-1/bl205-eu-spdc  | lo0       | up          | up         | 10.3.192.64/32     | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo1       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo2       | up          | up         | 172.16.11.233/32   | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo3       | up          | up         | 172.31.2.25/32     | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo4       | up          | up         | 115.115.115.115/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo5       | up          | up         | 172.24.0.15/32     | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo6       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo7       | up          | up         | 172.24.0.253/32    | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo8       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo9       | up          | up         | 205.205.205.25/32  | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo10      | up          | up         | 205.205.205.15/32  | 0           | 4294967295          | 
| apic11 | pod-1/bl205-eu-spdc  | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo0       | up          | up         | 10.3.32.64/32      | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo1       | up          | up         | 10.3.48.64/32      | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo2       | up          | up         | 172.16.11.237/32   | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo3       | up          | up         | 172.31.2.26/32     | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo4       | up          | up         | 116.116.116.116/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo5       | up          | up         | 124.124.124.124/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo6       | up          | up         | 172.24.0.14/32     | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo7       | up          | up         | 172.24.0.252/32    | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo8       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo9       | up          | up         | 118.118.118.118/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo10      | up          | up         | 120.120.120.120/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo11      | up          | up         | 206.206.206.25/32  | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo12      | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo13      | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo14      | up          | up         | 206.206.206.15/32  | 0           | 4294967295          | 
| apic11 | pod-1/bl206-eu-spdc  | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo0       | up          | up         | 10.3.192.67/32     | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo1       | up          | up         | 10.3.40.67/32      | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo2       | up          | up         | 172.16.11.232/32   | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo3       | up          | up         | 172.30.4.0/32      | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo4       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo5       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo6       | up          | up         | 15.254.101.8/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo7       | up          | up         | 15.254.101.2/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo8       | up          | up         | 15.254.101.6/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo9       | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo10      | up          | up         | 15.254.101.99/32   | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo11      | up          | up         | 15.254.101.4/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo12      | up          | up         | 121.121.121.121/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo13      | up          | up         | 15.254.101.0/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl201-eu-spdc  | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo0       | up          | up         | 10.3.192.68/32     | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo1       | up          | up         | 10.3.40.67/32      | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo2       | up          | up         | 172.16.11.231/32   | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo3       | up          | up         | 172.30.4.1/32      | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo4       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo5       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo6       | up          | up         | 15.254.101.3/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo7       | up          | up         | 15.254.101.1/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo8       | up          | up         | 15.254.101.9/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo9       | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo10      | up          | up         | 122.122.122.122/32 | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo11      | up          | up         | 15.254.101.7/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo12      | up          | up         | 15.254.101.5/32    | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo13      | up          | up         | 15.254.101.100/32  | 0           | 4294967295          | 
| apic11 | pod-1/cl202-eu-spdc  | lo1023    | up          | up         | 10.3.0.32/32       | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo0       | up          | up         | 172.16.30.160/32   | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo1       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo2       | up          | up         | 172.16.30.161/32   | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo3       | up          | up         | 172.16.30.88/32    | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo4       | up          | up         | 172.31.3.31/32     | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo5       | up          | up         | 172.30.4.4/32      | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo6       | up          | up         |                    | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo7       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo8       | up          | up         | 172.24.3.15/32     | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo9       | up          | up         | 131.131.131.131/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl301-eu-spdc  | lo1023    | up          | up         | 172.16.30.32/32    | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo0       | up          | up         | 172.16.30.120/32   | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo1       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo2       | up          | up         | 172.16.30.121/32   | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo3       | up          | up         | 172.16.30.88/32    | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo4       | up          | up         | 172.31.3.32/32     | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo5       | up          | up         |                    | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo6       | up          | up         | 172.30.4.5/32      | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo7       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo8       | up          | up         | 132.132.132.132/32 | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo9       | up          | up         | 172.24.3.14/32     | 0           | 4294967295          | 
| apic11 | pod-1/rl302-eu-spdc  | lo1023    | up          | up         | 172.16.30.32/32    | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo0       | up          | up         | 10.3.192.65/32     | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo1       | up          | up         | 10.3.40.65/32      | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo2       | up          | up         | 10.3.192.101/32    | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo3       | up          | up         | 10.3.40.64/32      | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo4       | up          | up         | 10.3.192.102/32    | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo5       | up          | up         | 10.3.40.66/32      | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo6       | up          | up         | 10.3.192.103/32    | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo7       | up          | up         | 101.101.101.101/32 | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo9       | up          | up         | 10.3.0.34/32       | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo10      | up          | up         | 10.3.0.35/32       | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo11      | up          | up         | 172.16.11.236/32   | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo12      | up          | up         | 172.16.11.228/32   | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo13      | up          | up         | 172.16.11.225/32   | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo14      | up          | up         | 172.16.11.226/32   | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo15      | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo16      | up          | up         | 172.16.1.1/32      | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo17      | up          | up         | 172.16.11.227/32   | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo18      | up          | up         | 172.16.12.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo19      | up          | up         | 172.16.11.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s101-eu-spdc   | lo20      | up          | up         | 10.58.28.181/32    | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo0       | up          | up         | 10.3.32.65/32      | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo1       | up          | up         | 10.3.40.64/32      | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo2       | up          | up         | 10.3.152.66/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo3       | up          | up         | 10.3.40.65/32      | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo4       | up          | up         | 10.3.152.65/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo5       | up          | up         | 10.3.40.66/32      | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo6       | up          | up         | 10.3.152.67/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo7       | up          | up         | 102.102.102.102/32 | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo8       | up          | up         | 10.3.0.33/32       | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo9       | up          | up         | 10.3.0.34/32       | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo10      | up          | up         | 10.3.0.35/32       | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo11      | up          | up         | 172.16.11.236/32   | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo12      | up          | up         | 172.16.11.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo13      | up          | up         | 172.16.11.225/32   | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo14      | up          | up         | 172.16.11.226/32   | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo15      | up          | up         | 172.16.10.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo16      | up          | up         | 172.16.1.1/32      | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo17      | up          | up         | 172.16.11.227/32   | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo18      | up          | up         | 172.16.12.1/32     | 0           | 4294967295          | 
| apic11 | pod-1/s102-eu-spdc   | lo19      | up          | up         | 10.58.28.182/32    | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo0       | up          | up         | 10.5.216.66/32     | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo1       | up          | up         | 10.5.192.65/32     | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo2       | up          | up         | 172.16.21.232/32   | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo3       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo4       | up          | up         | 125.125.125.125/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo5       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo6       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo7       | up          | up         | 205.205.205.205/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2205-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo0       | up          | up         | 10.5.216.64/32     | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo1       | up          | up         | 10.5.192.65/32     | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo2       | up          | up         | 172.16.21.233/32   | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo3       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo4       | up          | up         | 126.126.126.126/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo5       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo6       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo7       | up          | up         | 206.206.206.206/32 | 0           | 4294967295          | 
| apic21 | pod-1/bl2206-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo0       | up          | up         | 10.5.80.96/32      | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo1       | up          | up         | 10.5.192.64/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo2       | up          | up         | 172.16.21.231/32   | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo3       | up          | up         | 201.201.201.201/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo4       | up          | up         | 203.203.203.203/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo5       | up          | up         | 172.24.2.251/32    | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo6       | up          | up         | 172.24.2.253/32    | 0           | 4294967295          | 
| apic21 | pod-1/cl2201-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo0       | up          | up         | 10.5.216.67/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo1       | up          | up         | 10.5.192.64/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo2       | up          | up         | 172.16.21.234/32   | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo3       | up          | up         | 204.204.204.204/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo4       | up          | up         | 202.202.202.202/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo5       | up          | up         | 172.24.2.250/32    | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo6       | up          | up         | 172.24.2.252/32    | 0           | 4294967295          | 
| apic21 | pod-1/cl2202-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo0       | up          | up         | 10.5.240.34/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo1       | up          | up         | 10.5.192.66/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo2       | up          | up         | 172.16.21.237/32   | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo3       | up          | up         | 207.207.207.207/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo4       | up          | up         | 207.207.207.207/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2207-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo0       | up          | up         | 10.5.240.35/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo1       | up          | up         | 10.5.192.66/32     | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo2       | up          | up         | 172.16.21.235/32   | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo3       | up          | up         | 208.208.208.208/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo4       | up          | up         | 208.208.208.208/32 | 0           | 4294967295          | 
| apic21 | pod-1/cl2208-eu-spdc | lo1023    | up          | up         | 10.5.0.32/32       | 0           | 4294967295          | 
| apic21 | pod-1/rl2701-eu-spdc | lo0       | up          | up         | 172.16.70.208/32   | 0           | 4294967295          | 
| apic21 | pod-1/rl2701-eu-spdc | lo1       | up          | up         | 171.171.171.171/32 | 0           | 4294967295          | 
| apic21 | pod-1/rl2701-eu-spdc | lo2       | up          | up         | 172.16.70.209/32   | 0           | 4294967295          | 
| apic21 | pod-1/rl2701-eu-spdc | lo3       | up          | up         | 172.16.70.232/32   | 0           | 4294967295          | 
| apic21 | pod-1/rl2701-eu-spdc | lo1023    | up          | up         | 172.16.70.32/32    | 0           | 4294967295          | 
| apic21 | pod-1/rl2702-eu-spdc | lo0       | up          | up         | 172.16.70.24/32    | 0           | 4294967295          | 
| apic21 | pod-1/rl2702-eu-spdc | lo1       | up          | up         | 172.172.172.172/32 | 0           | 4294967295          | 
| apic21 | pod-1/rl2702-eu-spdc | lo2       | up          | up         | 172.16.70.25/32    | 0           | 4294967295          | 
| apic21 | pod-1/rl2702-eu-spdc | lo3       | up          | up         | 172.16.70.232/32   | 0           | 4294967295          | 
| apic21 | pod-1/rl2702-eu-spdc | lo1023    | up          | up         | 172.16.70.32/32    | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo0       | up          | up         | 10.5.80.97/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo1       | up          | up         | 10.5.80.65/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo2       | up          | up         | 10.5.80.66/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo3       | up          | up         | 10.5.160.70/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo4       | up          | up         | 10.5.80.64/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo5       | up          | up         | 10.5.160.69/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo6       | up          | up         | 10.5.160.71/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo7       | up          | up         | 10.5.0.33/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo9       | up          | up         | 10.5.0.35/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo10      | up          | up         | 172.16.21.238/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo11      | up          | up         | 172.16.21.239/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo12      | up          | up         | 172.16.21.240/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo13      | up          | up         | 172.16.21.2/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo14      | up          | up         | 172.16.21.230/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo15      | up          | up         | 172.16.21.1/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo16      | up          | up         | 172.16.22.1/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo17      | up          | up         | 111.111.111.111/32 | 0           | 4294967295          | 
| apic21 | pod-1/s2101-eu-spdc  | lo18      | up          | up         | 10.58.50.181/32    | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo0       | up          | up         | 10.5.80.98/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo1       | up          | up         | 10.5.80.65/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo2       | up          | up         | 10.5.80.64/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo3       | up          | up         | 10.5.160.65/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo4       | up          | up         | 10.5.80.66/32      | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo5       | up          | up         | 10.5.160.66/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo6       | up          | up         | 10.5.160.67/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo7       | up          | up         | 10.5.0.33/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo8       | up          | up         | 10.5.0.34/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo9       | up          | up         | 10.5.0.35/32       | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo10      | up          | up         | 172.16.21.236/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo11      | up          | up         | 172.16.21.239/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo12      | up          | up         | 172.16.21.240/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo13      | up          | up         | 172.16.21.2/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo14      | up          | up         | 172.16.21.230/32   | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo15      | up          | up         | 172.16.21.1/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo16      | up          | up         | 172.16.22.1/32     | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo17      | up          | up         | 112.112.112.112/32 | 0           | 4294967295          | 
| apic21 | pod-1/s2102-eu-spdc  | lo18      | up          | up         | 10.58.50.182/32    | 0           | 4294967295          | 
+--------+----------------------+-----------+-------------+------------+--------------------+-------------+---------------------+
```

[[Back]](./InterfaceLoopback.md)