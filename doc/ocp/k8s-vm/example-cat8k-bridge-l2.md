# Cat8000v: management in l2 bridge (multus)

[[Back]](./README.md)

## Overview

Modification of [management in l3 bridge (multus)](./example-cat8k-bridge-l3-provisioning.md) deployment scenario with bridge in l2 mode
- (NetworkAttachmentDefinition) bridge in default l2-mode
- (NetworkAttachmentDefinition) default route injection

## Provision

> [!NOTE]
> NetworkAttachmentDefinition has the only change

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: c8kv1-management
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "bridge",
      "name": "br1",
      "bridge": "br1",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "15.25.25.25/24",
            "gateway": "15.25.25.254"
          }
        ],
        "routes": [
          {
            "dst": "0.0.0.0/0"
          }
        ]
      }
    }
```

## Cat8000v

```
c8kv1#show int gigabitEthernet 1
GigabitEthernet1 is up, line protocol is up
  Hardware is vNIC, address is 0221.6600.000a (bia 0221.6600.000a)
  Internet address is 15.25.25.25/24
```

```
c8kv1#show ip route vrf Mgmt-intf
S*    0.0.0.0/0 [254/0] via 15.25.25.254
      15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        15.25.25.0/24 is directly connected, GigabitEthernet1
L        15.25.25.25/32 is directly connected, GigabitEthernet1
```

> [!NOTE]
> DCN not configured to accept traffic from virtual maching thus no ping response

```
c8kv1#ping vrf Mgmt-intf 8.8.8.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
```

## Host

```
# tcpdump -i br1 -e -n -nn
dropped privs to tcpdump
15:15:10.966305 02:21:66:00:00:0a > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 60: Request who-has 15.25.25.254 tell 15.25.25.25, length 46
```

[[Back]](./README.md)