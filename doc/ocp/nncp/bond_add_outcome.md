## Inteface Bond

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | [Link](./bond_add_cli.md) | [Link](./bond_add_json.md) | [Link](./bond_add_nncp.md) | See Below

### Before

```
$ ifconfig bond666
bond666: error fetching interface information: Device not found
```

### After

```
$ ifconfig bond666
bond666: flags=5123<UP,BROADCAST,MASTER,MULTICAST>  mtu 1400
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ cat /proc/net/bonding/bond666
Ethernet Channel Bonding Driver: v5.14.0-427.64.1.el9_4.x86_64

Bonding Mode: fault-tolerance (active-backup)
Primary Slave: None
Currently Active Slave: None
MII Status: down
MII Polling Interval (ms): 140
Up Delay (ms): 0
Down Delay (ms): 0
Peer Notification Delay (ms): 0

Slave Interface: eno1
MII Status: down
Speed: Unknown
Duplex: Unknown
Link Failure Count: 0
Permanent HW addr: aa:aa:aa:aa:aa:aa
Slave queue ID: 0

Slave Interface: eno2
MII Status: down
Speed: Unknown
Duplex: Unknown
Link Failure Count: 0
Permanent HW addr: bb:bb:bb:bb:bb:bb
Slave queue ID: 0
```

[[Back]](./README.md)