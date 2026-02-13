# Network Attachment Definition - Bridge

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
      "type": "bridge",
      "name": "br1",
      "bridge": "br1",
      "isDefaultGateway": true,
      "isMasq": true,
      "ipam": {
        "type": "host-local",
        "subnet": "10.1.1.0/28",
        "rangeStart": "10.1.1.2",
        "rangeEnd": "10.1.1.8",
        "gateway": "10.1.1.1",
        "routes": [
          {
            "dst": "10.1.2.0/28",
            "gw": "10.1.1.1"
          }
        ]
      }
    }
```

[[Back]](./README.md)