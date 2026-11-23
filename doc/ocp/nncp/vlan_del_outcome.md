## Inteface VLAN

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete VLAN | [Link](./vlan_del_cli.md) | [Link](./vlan_del_json.md) | [Link](./vlan_del_nncp.md) | See Below

### Before

```
$ ifconfig eno1.666
eno1.666: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### After

```
$ ifconfig eno1.666
eno1.666: error fetching interface information: Device not found
```

[[Back]](./README.md)