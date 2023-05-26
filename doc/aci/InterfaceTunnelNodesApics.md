# Node Interface - Tunnel

## Multi-APIC

```
# iserver get aci intf tun --apic dom:milan --node any

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

+--------+----------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
| Apic   | Node                 | Interface | Admin | Oper | Layer | Tunnel Type | Type                                           | Source           | Destination      | VRF       | MTU  |
+--------+----------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
| apic11 | pod-1/bl205-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.32.64       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.32.65       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.65      | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.40.67       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.67      | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.68      | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.64/32   | 10.3.40.64       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.64/32   | 10.3.40.65       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.64/32   | 10.3.40.66       | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.64/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/bl205-eu-spdc  | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.64      | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.32.65       | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.65      | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.40.67       | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.67      | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.68      | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.32.64/32    | 10.3.40.65       | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.32.64/32    | 10.3.40.64       | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.32.64/32    | 10.3.40.66       | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.32.64/32    | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.32.64/32    | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.32.64/32    | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/bl206-eu-spdc  | tunnel18  | up    | up   | l3    | ivxlan      | fabric-ext,physical                            | 10.3.32.64/32    | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.48.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.32.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.64      | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.32.65       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.65      | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.68      | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.67/32   | 10.3.40.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.67/32   | 10.3.40.65       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.67/32   | 10.3.40.66       | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.67/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel19  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/cl201-eu-spdc  | tunnel28  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.48.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.32.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.64      | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.32.65       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.65      | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.67      | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.68/32   | 10.3.40.65       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.68/32   | 10.3.40.64       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.68/32   | 10.3.40.66       | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.68/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/cl202-eu-spdc  | tunnel26  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.30.161/32 | 172.16.10.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.30.161/32 | 172.16.11.227/32 | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.161/32 | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.30.161/32 | 172.16.30.160    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.230    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.234    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.235    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical,rl-direct,rl-vpc | 172.16.30.161/32 | 172.16.30.121/32 | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.233    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.232    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.30.120    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.237    | overlay-1 | 9000 | 
| apic11 | pod-1/rl301-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.231    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.30.121/32 | 172.16.10.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.30.121/32 | 172.16.11.227/32 | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.121/32 | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.30.121/32 | 172.16.30.120    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.230    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.234    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.235    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct,rl-vpc           | 172.16.30.121/32 | 172.16.30.161/32 | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.233    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.232    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.30.160    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.237    | overlay-1 | 9000 | 
| apic11 | pod-1/rl302-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.231    | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.48.64       | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.32.64       | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.64      | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.32.65       | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.40.67       | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.67      | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.68      | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.65/32   | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel12  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.65/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel13  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.3.192.65/32   | 172.16.22.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel23  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.3.192.65/32   | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel24  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.192.65/32   | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel25  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 172.16.30.160    | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel26  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 172.16.30.120    | overlay-1 | 9000 | 
| apic11 | pod-1/s101-eu-spdc   | tunnel27  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.192.65/32   | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.32.65/32    | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.1         | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.2         | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.3         | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel12  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.32.65/32    | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel13  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.3.32.65/32    | 172.16.22.1/32   | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel19  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.48.64       | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel20  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.32.64       | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel21  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.64      | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel22  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.65      | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel23  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.40.67       | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel24  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.67      | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel25  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.68      | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel26  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 172.16.30.120    | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel27  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.32.65/32    | 172.16.30.121    | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel28  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.32.65/32    | 172.16.30.161    | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel29  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.3.32.65/32    | 172.16.30.88     | overlay-1 | 9000 | 
| apic11 | pod-1/s102-eu-spdc   | tunnel30  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 172.16.30.160    | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.216.66/32   | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.216.66/32   | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.216.66/32   | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.66/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.216.66/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel29  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.5.216.66/32   | 172.16.70.209    | overlay-1 | 9000 | 
| apic21 | pod-1/bl2205-eu-spdc | tunnel30  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.5.216.66/32   | 172.16.70.25     | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.216.64/32   | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.216.64/32   | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.216.64/32   | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel19  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.64/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel20  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.216.64/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel29  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.5.216.64/32   | 172.16.70.209    | overlay-1 | 9000 | 
| apic21 | pod-1/bl2206-eu-spdc | tunnel30  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.5.216.64/32   | 172.16.70.25     | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.80.96/32    | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.80.96/32    | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.80.96/32    | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.96/32    | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2201-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.80.96/32    | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.216.67/32   | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.216.67/32   | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.216.67/32   | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.216.67/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2202-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.216.67/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.240.34/32   | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.240.34/32   | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.240.34/32   | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.34/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2207-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.240.34/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.5.240.35/32   | 10.5.80.64       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.5.240.35/32   | 10.5.80.66       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.5.240.35/32   | 10.5.80.65       | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.240.35/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/cl2208-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.240.35/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.70.209/32 | 172.16.21.2/32   | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.70.209/32 | 172.16.21.230/32 | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.209/32 | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.70.209/32 | 172.16.70.208    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.208/32 | 172.16.21.227    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.208/32 | 172.16.21.228    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.208/32 | 172.16.21.229    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,rl-vpc                                | 172.16.70.209/32 | 172.16.70.25/32  | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.209/32 | 172.16.21.231    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.209/32 | 172.16.21.232    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.208/32 | 172.16.70.24     | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.209/32 | 172.16.21.234    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2701-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.209/32 | 172.16.21.233    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.70.25/32  | 172.16.21.2/32   | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.70.25/32  | 172.16.21.230/32 | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.25/32  | 172.16.21.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.70.25/32  | 172.16.70.24     | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.24/32  | 172.16.21.227    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.24/32  | 172.16.21.228    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.24/32  | 172.16.21.229    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,rl-vpc                                | 172.16.70.25/32  | 172.16.70.209/32 | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.25/32  | 172.16.21.231    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.25/32  | 172.16.21.232    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.70.24/32  | 172.16.70.208    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.25/32  | 172.16.21.234    | overlay-1 | 9000 | 
| apic21 | pod-1/rl2702-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.70.25/32  | 172.16.21.233    | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.80.98       | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.80.97/32    | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.80.97/32    | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.5.80.97/32    | 172.16.12.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel19  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.5.80.97/32    | 172.16.70.232    | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel20  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.5.80.97/32    | 172.16.70.209    | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel21  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 172.16.70.208    | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel22  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.97/32    | 172.16.70.24     | overlay-1 | 9000 | 
| apic21 | pod-1/s2101-eu-spdc  | tunnel23  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.5.80.97/32    | 172.16.70.25     | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.192.66      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.240.34      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.240.35      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.192.65      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.216.64      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.216.66      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.192.64      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.216.67      | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.80.96       | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.80.97       | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.80.98/32    | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.0.1         | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.0.2         | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 10.5.0.3         | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.5.80.98/32    | 172.16.11.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel16  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.5.80.98/32    | 172.16.12.1/32   | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel17  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.5.80.98/32    | 172.16.70.232    | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel18  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 172.16.70.208    | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel19  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.5.80.98/32    | 172.16.70.209    | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel20  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.5.80.98/32    | 172.16.70.25     | overlay-1 | 9000 | 
| apic21 | pod-1/s2102-eu-spdc  | tunnel21  | up    | up   | l3    | ivxlan      | physical                                       | 10.5.80.98/32    | 172.16.70.24     | overlay-1 | 9000 | 
+--------+----------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
```

[[Back]](./InterfaceTunnel.md)