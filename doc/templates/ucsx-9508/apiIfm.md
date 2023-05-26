# UCSX-9508 IFM monitoring with Intersight API

![API](image/api-ifm.png)

## equipment.Chassis

Intersight API object relationships:
- reference to IFM I/O modules via Ioms[]

```
API_DEBUG:get_ucsx_ifm.all:equipment chassis:0
```

## equipment.IoCard

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid
- reference to host ports via HostPorts[]
- reference to network ports via NetworkPorts[]

```
API_DEBUG:get_ucsx_ifm.all:equipment iocard:0
```

## ether.HostPort

Intersight API object relationships:
- reference to equipment.IoCard via Parent/Moid

```
API_DEBUG:get_ucsx_ifm.all:ether hostport:1
```

## ether.NetworkPort

Intersight API object relationships:
- reference to equipment.IoCard via Parent/Moid

```
API_DEBUG:get_ucsx_ifm.all:ether networkport:1
```