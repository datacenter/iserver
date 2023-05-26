# UCSX-9508 IFM host port monitoring with Intersight API

![API](image/api-host-port.png)

## equipment.Chassis

Intersight API object relationships:
- reference to IFM I/O modules via Ioms[]

```
API_DEBUG:get_ucsx_port.host:equipment chassis:0
```

## equipment.IoCard

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid
- reference to host ports via HostPorts[]
- reference to network ports via NetworkPorts[]

```
API_DEBUG:get_ucsx_port.host:equipment iocard:0
```

## ether.HostPort

Intersight API object relationships:
- reference to equipment.IoCard via Parent/Moid
- reference to adapter.ExtEthInterface via PeerInterface/Moid if ifm connected to node

```
API_DEBUG:get_ucsx_port.host:ether hostport:1
```

## adapter.ExtEthInterface

Intersight API object relationships:
- reference to ether.HostPort via PeerInterface/Moid if ifm connected to node
- reference to adapter.Unit via Parent/Moid

```
API_DEBUG:get_ucsx_port.host:adapter extethinterface:1
```

## adapter.Unit

Intersight API object relationships:
- reference to adapter.ExtEthInterface via ExtEthIfs[]
- reference to compute.Blade via Parent/Moid

```
API_DEBUG:get_ucsx_port.host:adapter unit:1
```

## compute.Blade

Intersight API object relationships:
- reference to adapter.Unit via Adapters[]
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_port.host:compute blade:1
```