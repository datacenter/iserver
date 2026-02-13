# Network Attachment Definition - VLAN

## CRD Example w/IPAM dhcp

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: test
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
      "ipam": {
        "type": "dhcp"
      }
    }
```

## CRD Example w/IPAM static

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: test
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.10.1/24",
            "gateway": "10.10.10.254"
          }
        ]
      }
    }
```

## CRD Example w/IPAM host-local

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: test
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
      "ipam": {
        "type": "host-local",
        "subnet": "10.10.10.0/24",
        "rangeStart": "10.10.10.1",
        "rangeEnd": "10.10.10.253",
        "gateway": "10.10.10.254"
      }
    }
```

[[Back]](./README.md)