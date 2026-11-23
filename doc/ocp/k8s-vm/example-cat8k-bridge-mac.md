# Cat8000v: management interface with user-defined mac address

[[Back]](./README.md)

## Overview

Extension of [management in l3 bridge (multus) network](./example-cat8k-bridge-l3-provisioning.md) deployment scenario with user-defined mac address for interface

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: default
  labels:
    app: c8kv1
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
          - name: nic1
            bridge: {}
            macAddress: de:ad:00:00:be:af
```

Then

```
c8kv1#show interfaces
GigabitEthernet1 is up, line protocol is up
  Hardware is vNIC, address is dead.0000.beaf (bia dead.0000.beaf)
  Internet address is 15.25.25.25/24
```

```
$ bridge fdb
de:ad:00:00:be:af dev veth604e99ca master br1
```

[[Back]](./README.md)