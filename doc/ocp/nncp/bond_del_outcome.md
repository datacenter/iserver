## Inteface Bond

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete bond | [Link](./bond_del_cli.md) | [Link](./bond_del_json.md) | [Link](./bond_del_nncp.md) | See Below

### Before

```
$ ifconfig bond666
bond666: flags=5123<UP,BROADCAST,MASTER,MULTICAST>  mtu 1400
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### After

```
$ ifconfig bond666
bond666: error fetching interface information: Device not found
```

[[Back]](./README.md)