# Namespace

[[Back]](README.md)

```json
[
    {
        "k8s": {
            "ns": [
                {
                    "namespace": "island-a1",
                    "ovn-udn": true,
                    "ovn-multicast": true,
                    "labels": {
                        "tenant": "a"
                    }
                }
            ]
        }
    }
]
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    k8s.ovn.org/multicast-enabled: 'true'
  labels:
    k8s.ovn.org/primary-user-defined-network: ''
    tenant: a
  name: island-a1
```

[[Back]](README.md)