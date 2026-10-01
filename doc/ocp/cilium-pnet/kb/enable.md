# Private Network - Enable feature

[[Back]](../README.md) [[iserver-way]](../enable.md) [[Next]](./network.md)

## Cilium configuration

```shell
iserver set ocp cilium pnet --mode feature --option multus --option local-access --option net-binding --option webhook --option certmanager
```

Minimum

```yaml
enterprise:
  featureGate:
    approved:
      - PrivateNetworks
  privateNetworks:
    enabled: true
```

With options

```yaml
enterprise:
  featureGate:
    approved:
      - PrivateNetworks
      - PrivateNetworkLocalAccess
  privateNetworks:
    enabled: true
    mode: local-access
    webhook:
      enabled: true
      vms:
        networkBinding: isovalent
    api:
      tls:
        enabled: true
        method: certmanager
        certmanager:
          issuerRef:
            group: cert-manager.io
            kind: Issuer
            name: cilium
    networkAttachmentDefinitions:
      enabled: true
```

Options
- multus: must be enabled for secondary interfaces into private network and mtv integration
- webhook: enable mtv integration (requires [mtv](../../mtv/README.md))
- net-binding: define custom network binding for attaching KubeVirt VMs to private networks (requires [cnv](../../cnv/README.md))
- certmanager: enables TLS for communication to connected INB (requires [certmanager](../../cert-manager/README.md))
- local-access: required for connecting the private network with local-access feature

Important requirements
- kube proxy replacement must be enabled
- cni.chaining must be set to `none` value
Check the complete list of private network feature incompatibilities in [documentation](https://iep-docs.cisco.com/iep/latest/inv/ipn/resources/caveats-and-limitations.html#feature-incompatibilities)

## Network binding

OpenShift 4.21 and lower

```yaml
oc patch hyperconvergeds \
  -n openshift-cnv kubevirt-hyperconverged \
  --type=merge --patch='{
    "spec": {
      "networkBinding": {
        "isovalent": {
          "domainAttachmentType": "managedTap"
        }
      }
    }
  }'
```

OpenShift 4.22 and higher

```yaml
oc patch hyperconvergeds \
  -n openshift-cnv kubevirt-hyperconverged \
  --type=merge --patch='{
    "spec": {
      "networking": {
        "networkBinding": {
          "isovalent": {
            "domainAttachmentType": "managedTap"
          }
        }
      }
    }
  }'
```

[[Back]](../README.md) [[iserver-way]](../enable.md) [[Next]](./network.md)