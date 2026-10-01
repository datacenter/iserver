## Provisioning - pre-provisioning network data

[[Back]](./provisioned.md)

Pre-provisioning network data describes the desired networking configuration for the deploy ramdisk running ironic-python-agent (IPA).

Specifying pre-provisioning network data is useful in DHCP-less scenarios, where we cannot rely on DHCP to provide network configuration for the IPA ramdisk during the inspection and provisioning phases. In this situation we can use redfish virtualmedia to boot the IPA ramdisk, and the generated virtualmedia ISO will also serve as a configuration drive to provide the network configuration.

The data is specified in the [OpenStack network_data.json format](https://docs.openstack.org/nova/latest/user/metadata.html#openstack-format-metadata)

Example

```yaml
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
```

[[Back]](./provisioned.md)