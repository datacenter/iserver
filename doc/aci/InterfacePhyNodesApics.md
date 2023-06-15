# Node Interface - Physical

## Multi-APIC

```
# iserver get aci intf phy --apic dom:milan --node any --speed 400G

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
| apic11 | pod-1/cl209-eu-spdc  | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:0F:FD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:0F:FE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:0F:FF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:00 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:01 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:02 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl209-eu-spdc  | 1/36      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:04 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:CD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:CF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:D1 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:D2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/cl210-eu-spdc  | 1/35      | up    | disabled  | down | sfp-missing | fab  | routed |    | C0:F8:7F:FE:10:D3 | trunk | 400G  | full   | 9366 | disable-fec | 
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
| apic11 | pod-1/s102-eu-spdc   | 1/14      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic11 | pod-1/s102-eu-spdc   | 1/15      | up    | enabled   | down | sfp-missing | fab  | routed |    | 8C:94:1F:FA:54:2F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:CD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:CE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:D0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/bl2205-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 3C:13:CC:B9:ED:D1 | trunk | 400G  | full   | 9366 | disable-fec | 
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
| apic21 | pod-1/cl2209-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:ED | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:EE | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:EF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:F0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:F1 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:F2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2209-eu-spdc | 1/36      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:E4:42:F4 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/29      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:7D | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/30      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:7E | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/31      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:7F | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/32      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:80 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/33      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:81 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/34      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:82 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/cl2210-eu-spdc | 1/35      | up    | disabled  | down | sfp-missing | fab  | routed |    | 24:2A:04:99:C1:83 | trunk | 400G  | full   | 9366 | disable-fec | 
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
| apic21 | pod-1/s2102-eu-spdc  | 1/19      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:BD | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/21      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:BF | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/22      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C0 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/23      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C1 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/24      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C2 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/26      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C4 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/27      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C5 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/28      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C6 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/29      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C7 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/30      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C8 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/31      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:C9 | trunk | 400G  | full   | 9366 | disable-fec | 
| apic21 | pod-1/s2102-eu-spdc  | 1/32      | up    | enabled   | down | sfp-missing | fab  | routed |    | F0:4A:02:A9:32:CA | trunk | 400G  | full   | 9366 | disable-fec | 
+--------+----------------------+-----------+-------+-----------+------+-------------+------+--------+----+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic dom:milan --node any --speed 400G

{
    "duration": 16746,
    "apic": {
        "read": true,
        "success": 48,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 46,
        "connect_time": 799,
        "disconnect_time": 0,
        "mo_time": 14474,
        "total_time": 15273
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

True	400	-	connect apic11o.emea-sp.cisco.com
True	309	13	apic11o.emea-sp.cisco.com class fabricNode
True	399	-	connect apic21o.emea-sp.cisco.com
True	306	15	apic21o.emea-sp.cisco.com class fabricNode
True	313	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	303	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	290	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l1PhysIf
True	305	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ethpmPhysIf
True	329	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l1PhysIf
True	348	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ethpmPhysIf
True	344	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l1PhysIf
True	358	108	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ethpmPhysIf
True	294	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l1PhysIf
True	313	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ethpmPhysIf
True	292	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l1PhysIf
True	363	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ethpmPhysIf
True	310	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l1PhysIf
True	319	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ethpmPhysIf
True	312	52	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l1PhysIf
True	327	48	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ethpmPhysIf
True	288	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l1PhysIf
True	307	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ethpmPhysIf
True	292	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l1PhysIf
True	290	16	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ethpmPhysIf
True	342	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/l1PhysIf
True	308	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2205/ethpmPhysIf
True	297	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/l1PhysIf
True	326	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2206/ethpmPhysIf
True	326	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/l1PhysIf
True	341	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2201/ethpmPhysIf
True	338	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/l1PhysIf
True	343	108	apic21o.emea-sp.cisco.com class topology/pod-1/node-2202/ethpmPhysIf
True	298	60	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/l1PhysIf
True	320	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2207/ethpmPhysIf
True	306	60	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/l1PhysIf
True	317	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2208/ethpmPhysIf
True	297	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/l1PhysIf
True	304	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2209/ethpmPhysIf
True	339	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/l1PhysIf
True	318	36	apic21o.emea-sp.cisco.com class topology/pod-1/node-2210/ethpmPhysIf
True	309	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/l1PhysIf
True	325	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2701/ethpmPhysIf
True	298	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/l1PhysIf
True	319	54	apic21o.emea-sp.cisco.com class topology/pod-1/node-2702/ethpmPhysIf
True	303	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/l1PhysIf
True	301	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2101/ethpmPhysIf
True	291	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/l1PhysIf
True	296	34	apic21o.emea-sp.cisco.com class topology/pod-1/node-2102/ethpmPhysIf
```

[[Back]](./InterfacePhy.md)