# Node Interface - MACsec

## All nodes

```
# iserver get aci intf macsec --apic apic11 --node any

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

+---------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
| Node                | Interface | Admin State | Oper State | Reason     | Session State   | Peers | Cepher Suite    | Confid Offset | Ker Server Prio | Replay Window |
+---------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
| pod-1/bl205-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl205-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/bl206-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl201-eu-spdc | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/24   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/25   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/26   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/27   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/31   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/32   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/33   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/34   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/35   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/37   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/38   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/39   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/40   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/41   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/42   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/43   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/44   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/45   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/46   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/47   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/48   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/49   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/50   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/51   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/52   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/53   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/54   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/55   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/56   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/57   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/58   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/59   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/60   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/61   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/62   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/63   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/64   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/65   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/66   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/67   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/68   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/69   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/70   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/71   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/72   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/73   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/74   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/75   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/76   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/77   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/78   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/79   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/80   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/81   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/82   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/83   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/84   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/85   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/86   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/87   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/88   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/89   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/90   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/91   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/92   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/93   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/94   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/95   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/96   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/97   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/98   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/99   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/100  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/101  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/cl202-eu-spdc | eth1/102  | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/24/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/24/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/24/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/24/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/25/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/25/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/25/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/25/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/26/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/26/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/26/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/26/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/27/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/27/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/27/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/27/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl301-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/1    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/2    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/3    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/4    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/5    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/6    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/7    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/8    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/9    | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/10   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/11   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/12   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/13   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/14   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/15   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/17   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/18   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/19   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/20   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/21   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/22   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/23   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/24/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/24/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/24/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/24/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/25/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/25/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/25/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/25/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/26/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/26/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/26/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/26/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/27/1 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/27/2 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/27/3 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/27/4 | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/29   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/30   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/rl302-eu-spdc | eth1/36   | disabled    | down       | admin-down | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
| pod-1/s101-eu-spdc  | eth1/16   | disabled    | down       | admin-down | not-initialized | 0     | 0               | 0             | 16              | 64            | 
| pod-1/s102-eu-spdc  | eth1/16   | disabled    | down       | if-down    | not-initialized | 0     | gcm-aes-xpn-256 | offset-0      | 16              | 64            | 
+---------------------+-----------+-------------+------------+------------+-----------------+-------+-----------------+---------------+-----------------+---------------+
```

Developer

```
# iserver get aci intf macsec --apic apic11 --node any

{
    "duration": 10012,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 411,
        "disconnect_time": 0,
        "mo_time": 8345,
        "total_time": 8756
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
    }
}

Log: apic
----------

True	411	-	connect apic11o.emea-sp.cisco.com
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
True	307	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	303	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	312	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	357	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/macsecIf
True	327	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1PhysIf
True	316	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ethpmPhysIf
True	357	102	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/macsecIf
True	343	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	375	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	339	102	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/macsecIf
True	391	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	362	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	319	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/macsecIf
True	351	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1PhysIf
True	359	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ethpmPhysIf
True	319	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/macsecIf
True	331	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1PhysIf
True	366	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ethpmPhysIf
True	331	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/macsecIf
True	299	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1PhysIf
True	293	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ethpmPhysIf
True	313	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/macsecIf
True	304	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1PhysIf
True	370	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ethpmPhysIf
```

[[Back]](./InterfaceMacSec.md)