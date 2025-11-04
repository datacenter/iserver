## Complex Scenario

Add linux bridge with bonded vlan upstream as per the following diagram

![UC1](../images/ocp_nncp_uc1.png)

JSON | NNCP CRD | Outcome
--- | --- | ---
[Link](./uc1_add_json.md) | [Link](./uc1_add_nncp.md) | See Below

```
$ ifconfig enp216s0f0
enp216s0f0: flags=6211<UP,BROADCAST,RUNNING,SLAVE,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 38335  bytes 5183274 (4.9 MiB)
        RX errors 0  dropped 17  overruns 0  frame 0
        TX packets 3099  bytes 990402 (967.1 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ ifconfig enp216s0f1
enp216s0f1: flags=6211<UP,BROADCAST,RUNNING,SLAVE,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 6525  bytes 3269025 (3.1 MiB)
        RX errors 0  dropped 25  overruns 0  frame 0
        TX packets 3113  bytes 997288 (973.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ ifconfig bond666
bond666: flags=5187<UP,BROADCAST,RUNNING,MASTER,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 65  bytes 30056 (29.3 KiB)
        RX errors 0  dropped 52  overruns 0  frame 0
        TX packets 4  bytes 180 (180.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ cat /proc/net/bonding/bond666
Ethernet Channel Bonding Driver: v5.14.0-427.64.1.el9_4.x86_64

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: None
Currently Active Slave: enp216s0f0
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0
Peer Notification Delay (ms): 0

Slave Interface: enp216s0f0
MII Status: up
Speed: 10000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: aa:aa:aa:aa:aa:aa
Slave queue ID: 0

Slave Interface: enp216s0f1
MII Status: up
Speed: 10000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: bb:bb:bb:bb:bb:bb
Slave queue ID: 0

$ ifconfig bond666.666
bond666.666: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4  bytes 180 (180.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ nmcli dev show bond666.666
GENERAL.DEVICE:                         bond666.666
GENERAL.TYPE:                           vlan
GENERAL.HWADDR:                         aa:aa:aa:aa:aa:aa
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     bond666.666
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/25488
IP4.GATEWAY:                            --
IP6.GATEWAY:                            --

$ nmcli dev show br666
GENERAL.DEVICE:                         br666
GENERAL.TYPE:                           bridge
GENERAL.HWADDR:                         aa:aa:aa:aa:aa:aa
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     br666
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/25487
IP4.ADDRESS[1]:                         10.66.66.66/24
IP4.GATEWAY:                            --
IP4.ROUTE[1]:                           dst = 10.66.66.0/24, nh = 0.0.0.0, mt = 425
IP6.GATEWAY:                            --
```

[[Back]](./README.md)