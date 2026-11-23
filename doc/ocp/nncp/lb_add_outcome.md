## Linux Bridge

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add linux bridge | [Link](./lb_add_cli.md) | [Link](./lb_add_json.md) | [Link](./lb_add_nncp.md) | See Below

### Before

```
$ ifconfig br666
br666: error fetching interface information: Device not found
```

### After

```
$ ifconfig br666
br666: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 60  bytes 4248 (4.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3  bytes 126 (126.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ nmcli device show br666
GENERAL.DEVICE:                         br666
GENERAL.TYPE:                           bridge
GENERAL.HWADDR:                         aa:aa:aa:aa:aa:aa
GENERAL.MTU:                            1500
GENERAL.STATE:                          100 (connected)
GENERAL.CONNECTION:                     br666
GENERAL.CON-PATH:                       /org/freedesktop/NetworkManager/ActiveConnection/25476
IP4.ADDRESS[1]:                         10.66.66.66/24
IP4.GATEWAY:                            --
IP4.ROUTE[1]:                           dst = 10.66.66.0/24, nh = 0.0.0.0, mt = 425
IP6.GATEWAY:                            --
```

[[Back]](./README.md)