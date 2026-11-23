## Interface Ethernet

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Configure IP address | [Link](./eth_ip_cli.md) | [Link](./eth_ip_json.md) | [Link](./eth_ip_nncp.md) | See Below

### Before

```
$ ifconfig eno1
eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

### After

```
$ ifconfig eno1
eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 10.66.66.66  netmask 255.255.255.0  broadcast 10.66.66.255
        ether aa:aa:aa:aa:aa:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

[[Back]](./README.md)