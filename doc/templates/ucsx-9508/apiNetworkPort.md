# UCSX-9508 IFM network port monitoring with Intersight API

![API](image/api-network-port.png)

## equipment.Chassis

Intersight API object relationships:
- reference to IFM I/O modules via Ioms[]

```
API_DEBUG:get_ucsx_port.net:equipment chassis:0
```

## equipment.IoCard

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid
- reference to host ports via HostPorts[]
- reference to network ports via NetworkPorts[]

```
API_DEBUG:get_ucsx_port.net:equipment iocard:0
```

## ether.NetworkPort

Intersight API object relationships:
- reference to equipment.IoCard via Parent/Moid
- reference to ether.PhysicalPort via PeerInterface/Moid

```
API_DEBUG:get_ucsx_port.net:ether networkport:1
```

## ether.PhysicalPort

Intersight API object relationships:
- no reference to ether.NetworkPort

```
API_DEBUG:get_ucsx_port.net:ether physicalport:1
```