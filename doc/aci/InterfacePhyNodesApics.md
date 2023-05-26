# Node Interface - Physical

## Multi-APIC

```
# iserver get aci intf phy --apic dom:milan --node any --speed 400G

Apic: apic11,apic21
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

+--------+----------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| Apic   | Node                 | Interface | Admin | Switching | Oper | Reason      | Type | Layer  | PC | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+--------+----------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
| apic11 | pod-1/bl205-eu-spdc  | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0D | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:0F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:10 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:11 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 4C:71:0D:7E:84:12 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl205-eu-spdc  | 1/35      | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:7E:84:13 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/bl205-eu-spdc  | 1/36      | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:7E:84:14 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/bl206-eu-spdc  | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:CD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:CF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:D1 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:C9:EC:D2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/bl206-eu-spdc  | 1/35      | up    | enabled   | up   | connected   | fab  | routed |    | 3C:13:CC:C9:EC:D3 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/bl206-eu-spdc  | 1/36      | up    | enabled   | up   | connected   | fab  | routed |    | 3C:13:CC:C9:EC:D4 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/s101-eu-spdc   | 1/3       | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:CF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/4       | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/5       | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:55:D1:D1 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/s101-eu-spdc   | 1/6       | up    | enabled   | up   | connected   | fab  | routed |    | 4C:71:0D:55:D1:D2 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/s101-eu-spdc   | 1/7       | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D3 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/8       | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D4 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/9       | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D5 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/10      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D6 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/11      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D7 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/12      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D8 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/13      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:D9 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/14      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:DA | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s101-eu-spdc   | 1/15      | up    | enabled   | down | sfp-missing | fab  | routed |    | 4C:71:0D:55:D1:DB | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/3       | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:23 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/4       | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:24 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/5       | up    | enabled   | up   | connected   | fab  | routed |    | 8C:94:1F:FA:54:25 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/s102-eu-spdc   | 1/6       | up    | enabled   | up   | connected   | fab  | routed |    | 8C:94:1F:FA:54:26 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic11 | pod-1/s102-eu-spdc   | 1/7       | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:27 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/8       | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:28 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/9       | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:29 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/10      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2A | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/11      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2B | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/12      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2C | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/13      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2D | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/14      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/15      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:D2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/35      | up    | enabled   | up   | connected   | fab  | routed |    | 3C:13:CC:B9:ED:D3 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/bl2205-eu-spdc | 1/36      | up    | enabled   | up   | connected   | fab  | routed |    | 3C:13:CC:B9:ED:D4 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/bl2206-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:5D | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:5E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:5F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:60 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:61 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 64:3A:EA:DA:B1:62 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2206-eu-spdc | 1/35      | up    | enabled   | up   | connected   | fab  | routed |    | 64:3A:EA:DA:B1:63 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/bl2206-eu-spdc | 1/36      | up    | enabled   | up   | connected   | fab  | routed |    | 64:3A:EA:DA:B1:64 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/s2101-eu-spdc  | 1/3       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3A:FF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/4       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:00 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/5       | up    | enabled   | up   | connected   | fab  | routed |    | F0:4A:02:A9:3B:01 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/s2101-eu-spdc  | 1/6       | up    | enabled   | up   | connected   | fab  | routed |    | F0:4A:02:A9:3B:02 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/s2101-eu-spdc  | 1/9       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:05 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/10      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:06 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/11      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:07 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/12      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:08 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/13      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:09 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/14      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:0A | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/15      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:0B | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/17      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:0D | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/18      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:0E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/19      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:0F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/20      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:10 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/21      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:11 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/22      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:12 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/23      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:13 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/24      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:14 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/25      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:15 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/26      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:16 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/27      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:17 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/28      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:18 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/29      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:19 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/30      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:1A | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/31      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:1B | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2101-eu-spdc  | 1/32      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:3B:1C | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/3       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:AD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/4       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:AE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/5       | up    | enabled   | up   | connected   | fab  | routed |    | F0:4A:02:A9:32:AF | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/s2102-eu-spdc  | 1/6       | up    | enabled   | up   | connected   | fab  | routed |    | F0:4A:02:A9:32:B0 | trunk | 400G  | full   | 9366 | kp-fec      | 
| apic21 | pod-1/s2102-eu-spdc  | 1/9       | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B3 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/10      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B4 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/11      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B5 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/12      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B6 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/13      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B7 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/14      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B8 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/15      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:B9 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/17      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:BB | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/18      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:BC | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/20      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:BE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/22      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/24      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/26      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C4 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/27      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C5 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/28      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C6 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/29      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C7 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/30      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C8 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/31      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C9 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/32      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:CA | trunk | 400G  | full   | 9366 | disable-fec | 
+--------+----------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
```

[[Back]](./InterfacePhy.md)