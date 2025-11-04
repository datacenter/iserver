## Linux Bridge

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete linux bridge | [Link](./lb_del_cli.md) | [Link](./lb_del_json.md) | [Link](./lb_del_nncp.md) | See Below

### Before

```
$ ifconfig br666
br666: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 60  bytes 4248 (4.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3  bytes 126 (126.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### After

```
$ ifconfig br666
br666: error fetching interface information: Device not found
```

[[Back]](./README.md)