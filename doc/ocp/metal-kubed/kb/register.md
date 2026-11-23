# Register host

[[Back]](../README.md)

Hosts are created with [BareMetalHost](./crd/baremetalhost.md) object that leads to one of the two desired host provisioning states depending on the object definition
- [externally provisioned](./externally_provisioned.md) state for power tasks only 
- [available](./available.md) state that enables [image provisioning](./provisioned.md), [bios settings change](./change_bios_settings.md) and [firmware upgrades](./firmware_upgrade.md)

## Externally provisioned

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-bmc-secret
  namespace: openshift-machine-api
  labels:
    environment.metal3.io: baremetal
type: Opaque
data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: test
  namespace: openshift-machine-api
spec:
  online: true
  externallyProvisioned: true
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAA
    credentialsName: test-bmc-secret
    disableCertificateVerification: true
```

## Available

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-bmc-secret
  namespace: openshift-machine-api
  labels:
    environment.metal3.io: baremetal
type: Opaque
data:
  username: YWRtaW4=
  password: cGFzc3dvcmQ=
---
apiVersion: v1
kind: Secret
metadata:
  name: test-network
  namespace: openshift-machine-api
type: Opaque
stringData:
  nmstate: |
    interfaces:
      - name: eno5
        type: ethernet
        state: up
        ipv4:
          enabled: false
        ipv6:
          enabled: false
      - name: eno6
        type: ethernet
        state: up
        ipv4:
          enabled: false
        ipv6:
          enabled: false
      - name: bond0
        type: bond
        state: up
        link-aggregation:
          mode: 802.3ad
          options:
            lacp_rate: slow
          port:
          - eno5
          - eno6
      - name: bond0.666
        type: vlan
        state: up
        vlan:
          base-iface: bond0
          id: 666
        ipv4:
          enabled: true
          dhcp: false
          address:
          - ip: 10.10.10.65
            prefix-length: 28
        ipv6:
          enabled: false
    dns-resolver:
      config:
        server:
        - 30.30.30.30
    routes:
      config:
      - destination: 0.0.0.0/0
        next-hop-address: 10.10.10.78
        next-hop-interface: bond0.666
        table-id: 254
---
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: test
  namespace: openshift-machine-api
spec:
  online: true
  preprovisioningNetworkDataName: test-network
  bootMACAddress: aa:aa:aa:aa:aa:aa
  bootMode: UEFI
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAA
    credentialsName: test-bmc-secret
    disableCertificateVerification: true
```

[[Back]](../README.md)