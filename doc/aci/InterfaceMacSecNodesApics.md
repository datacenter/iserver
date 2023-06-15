# Node Interface - MACsec

## Multi-APIC

```
# iserver get aci intf macsec --apic dom:milan --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc
Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
| Apic   | Node                 | Interface | Admin State | Oper State | Reason     | Session State   | Peers | Cepher Suite    | Confid Offset | Ker Server Prio | Replay Window |
+--------+----------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
| apic11 | pod-1/bl205-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl205-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/bl206-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl201-eu-spdc  | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl202-eu-spdc  | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl209-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/cl210-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/24/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/24/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/24/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/24/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/25/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/25/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/25/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/25/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/26/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/26/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/26/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/26/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/27/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/27/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/27/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/27/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl301-eu-spdc  | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/24/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/24/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/24/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/24/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/25/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/25/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/25/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/25/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/26/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/26/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/26/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/26/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/27/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/27/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/27/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/27/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/rl302-eu-spdc  | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic11 | pod-1/s101-eu-spdc   | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic11 | pod-1/s102-eu-spdc   | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2205-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/bl2206-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2201-eu-spdc | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2202-eu-spdc | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/1/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/1/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/1/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/1/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/2/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/2/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/2/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/2/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/3/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/3/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/3/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/3/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/4/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/4/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/4/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/4/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/5/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/5/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/5/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/5/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/6/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/6/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/6/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/6/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2207-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/1/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/1/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/1/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/1/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/2/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/2/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/2/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/2/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/3/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/3/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/3/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/3/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/4/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/4/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/4/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/4/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/5/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/5/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/5/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/5/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/6/1  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/6/2  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/6/3  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/6/4  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2208-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2209-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/cl2210-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2701-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/rl2702-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| apic21 | pod-1/s2101-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| apic21 | pod-1/s2102-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
+--------+----------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic dom:milan --node any

{
    "duration": 26788,
    "apic": {
        "read": true,
        "success": 70,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 68,
        "connect_time": 814,
        "disconnect_time": 0,
        "mo_time": 22095,
        "total_time": 22909
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	406	-	connect apic11o.emea-sp.cisco.com
True	288	13	apic11o.emea-sp.cisco.com class fabricNode
True	408	-	connect apic21o.emea-sp.cisco.com
True	319	15	apic21o.emea-sp.cisco.com class fabricNode
True	318	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	293	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	309	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	299	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/macsecIf
True	300	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1PhysIf
True	310	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ethpmPhysIf
True	345	102	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/macsecIf
True	325	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	363	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	380	102	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/macsecIf
True	351	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	345	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	327	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/macsecIf
True	296	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l1PhysIf
True	361	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ethpmPhysIf
True	294	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/macsecIf
True	312	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l1PhysIf
True	305	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ethpmPhysIf
True	319	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/macsecIf
True	403	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1PhysIf
True	322	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ethpmPhysIf
True	305	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/macsecIf
True	342	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1PhysIf
True	319	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ethpmPhysIf
True	310	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/macsecIf
True	324	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1PhysIf
True	295	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ethpmPhysIf
True	309	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/macsecIf
True	313	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1PhysIf
True	302	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ethpmPhysIf
True	335	28	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/macsecIf
True	304	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l1PhysIf
True	317	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/ethpmPhysIf
True	307	28	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/macsecIf
True	317	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l1PhysIf
True	314	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/ethpmPhysIf
True	334	102	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/macsecIf
True	350	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l1PhysIf
True	378	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/ethpmPhysIf
True	323	102	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/macsecIf
True	341	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l1PhysIf
True	366	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/ethpmPhysIf
True	362	48	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/macsecIf
True	322	60	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l1PhysIf
True	310	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/ethpmPhysIf
True	323	48	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/macsecIf
True	335	60	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l1PhysIf
True	337	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/ethpmPhysIf
True	307	28	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/macsecIf
True	318	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l1PhysIf
True	327	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/ethpmPhysIf
True	298	28	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/macsecIf
True	320	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l1PhysIf
True	373	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/ethpmPhysIf
True	301	51	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/macsecIf
True	313	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l1PhysIf
True	481	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/ethpmPhysIf
True	303	51	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/macsecIf
True	320	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l1PhysIf
True	340	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/ethpmPhysIf
True	288	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/macsecIf
True	318	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l1PhysIf
True	306	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/ethpmPhysIf
True	292	1	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/macsecIf
True	292	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l1PhysIf
True	320	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)