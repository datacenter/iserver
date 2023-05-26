# Node Interface - Tunnel

## All nodes

```
# iserver get aci intf tun --apic apic11 --node any

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

+---------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
| Node                | Interface | Admin | Oper | Layer | Tunnel Type | Type                                           | Source           | Destination      | VRF       | MTU  |
+---------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
| pod-1/bl205-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.32.64       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.32.65       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.65      | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.40.67       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.67      | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.192.68      | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.64/32   | 10.3.40.64       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.64/32   | 10.3.40.65       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.64/32   | 10.3.40.66       | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.64/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.64/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/bl205-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.64/32   | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.64      | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.32.65       | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.65      | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.40.67       | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.67      | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.192.68      | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.32.64/32    | 10.3.40.65       | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.32.64/32    | 10.3.40.64       | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.32.64/32    | 10.3.40.66       | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.64/32    | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.32.64/32    | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.32.64/32    | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.32.64/32    | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/bl206-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | fabric-ext,physical                            | 10.3.32.64/32    | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.48.64       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.32.64       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.64      | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.32.65       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.65      | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.192.68      | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.67/32   | 10.3.40.64       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.67/32   | 10.3.40.65       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.67/32   | 10.3.40.66       | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.67/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.67/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel19  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/cl201-eu-spdc | tunnel28  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.67/32   | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.48.64       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.32.64       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.64      | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.32.65       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.65      | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.192.67      | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | physical,proxy-acast-mac                       | 10.3.192.68/32   | 10.3.40.65       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | physical,proxy-acast-v4                        | 10.3.192.68/32   | 10.3.40.64       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | physical,proxy-acast-v6                        | 10.3.192.68/32   | 10.3.40.66       | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.68/32   | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.68/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel17  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel18  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/cl202-eu-spdc | tunnel26  | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical                  | 10.3.192.68/32   | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.30.161/32 | 172.16.10.1/32   | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.30.161/32 | 172.16.11.227/32 | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.161/32 | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.30.161/32 | 172.16.30.160    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.230    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.234    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.11.235    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | dci-ucast,fabric-ext,physical,rl-direct,rl-vpc | 172.16.30.161/32 | 172.16.30.121/32 | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.233    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.232    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel14  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.160/32 | 172.16.30.120    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel15  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.237    | overlay-1 | 9000 | 
| pod-1/rl301-eu-spdc | tunnel16  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.161/32 | 172.16.11.231    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel1   | up    | up   | l3    | ivxlan      | physical,rl-routable,rl-ucast                  | 172.16.30.121/32 | 172.16.10.1/32   | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel2   | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep                         | 172.16.30.121/32 | 172.16.11.227/32 | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.121/32 | 172.16.11.1/32   | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel4   | up    | up   | l3    | ivxlan      | fabric-ext,learn-disabled,physical,rl-ss       | 172.16.30.121/32 | 172.16.30.120    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.230    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.234    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.11.235    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel8   | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct,rl-vpc           | 172.16.30.121/32 | 172.16.30.161/32 | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel9   | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.233    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel10  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.232    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 172.16.30.120/32 | 172.16.30.160    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel12  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.237    | overlay-1 | 9000 | 
| pod-1/rl302-eu-spdc | tunnel13  | up    | up   | l3    | ivxlan      | fabric-ext,physical,rl-direct-rt-ptep          | 172.16.30.121/32 | 172.16.11.231    | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel1   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.48.64       | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel2   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.32.64       | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel3   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.64      | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel4   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.32.65       | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel5   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.40.67       | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel6   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.67      | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel7   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.68      | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.192.65/32   | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.192.65/32   | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.3.192.65/32   | 172.16.22.1/32   | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel23  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.3.192.65/32   | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel24  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.192.65/32   | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel25  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 172.16.30.160    | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel26  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.192.65/32   | 172.16.30.120    | overlay-1 | 9000 | 
| pod-1/s101-eu-spdc  | tunnel27  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.192.65/32   | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel8   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.32.65/32    | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel9   | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.1         | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel10  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.2         | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel11  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.0.3         | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel12  | up    | up   | l3    | ivxlan      | dci-ucast,physical                             | 10.3.32.65/32    | 172.16.21.1/32   | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel13  | up    | up   | l3    | ivxlan      | dci-mcast-hrep,physical                        | 10.3.32.65/32    | 172.16.22.1/32   | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel19  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.48.64       | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel20  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.32.64       | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel21  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.64      | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel22  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.65      | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel23  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.40.67       | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel24  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.67      | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel25  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 10.3.192.68      | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel26  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 172.16.30.120    | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel27  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.32.65/32    | 172.16.30.121    | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel28  | up    | up   | l3    | ivxlan      | physical,rl-mcast-hrep,rl-ucast                | 10.3.32.65/32    | 172.16.30.161    | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel29  | up    | up   | l3    | ivxlan      | physical,rl-ucast                              | 10.3.32.65/32    | 172.16.30.88     | overlay-1 | 9000 | 
| pod-1/s102-eu-spdc  | tunnel30  | up    | up   | l3    | ivxlan      | physical                                       | 10.3.32.65/32    | 172.16.30.160    | overlay-1 | 9000 | 
+---------------------+-----------+-------+------+-------+-------------+------------------------------------------------+------------------+------------------+-----------+------+
```

[[Back]](./InterfaceTunnel.md)