## Complex Scenario

Add bonded vlan interface with static IPv4 routes.

JSON | NNCP CRD | Outcome
--- | --- | ---
[Link](./uc2_add_json.md) | [Link](./uc2_add_nncp.md) | See Below

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
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4  bytes 168 (168.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


$ ip route
[truncated]
10.66.66.0/24 dev bond666.666 proto kernel scope link src 10.66.66.66 metric 401
10.77.77.0/24 via 10.66.66.1 dev bond666.666 proto static
```

[[Back]](./README.md)