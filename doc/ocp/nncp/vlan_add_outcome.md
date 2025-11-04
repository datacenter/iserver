## Inteface VLAN

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add VLAN | [Link](./vlan_add_cli.md) | [Link](./vlan_add_json.md) | [Link](./vlan_add_nncp.md) | See Below

### Before

```
$ ifconfig eno1.666
eno1.666: error fetching interface information: Device not found
```

### After

```
$ ifconfig eno1.666
eno1.666: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

[[Back]](./README.md)