## Provisioning - network data

[[Back]](./provisioned.md)

Network data describes the desired networking configuration for the deployed operating system, and is typically applied on first-boot via tools such as cloud-init.

The data is specified in the [OpenStack network_data.json format](https://docs.openstack.org/nova/latest/user/metadata.html#openstack-format-metadata) supported by cloud-init and Glean. The format is not very well documented, but you can consult the [network_data JSON schema](https://docs.openstack.org/nova/latest/_downloads/4e8fe1ae7db6dd6eebca372db68fe63e/network_data.json) shipped with OpenStack.

Example

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-networkdata
  namespace: openshift-machine-api
type: Opaque
stringData:
  networkData: |
    {
      "links": [
        {
          "id": "eno5",
          "type": "phy",
          "ethernet_mac_address": "aa:aa:aa:aa:aa:aa"
        },
        {
          "id": "eno6",
          "type": "phy",
          "ethernet_mac_address": "bb:bb:bb:bb:bb:bb"
        },
        {
          "id": "bond0",
          "type": "bond",
          "bond_links": ["eno5", "eno6"],
          "bond_mode": "802.3ad"
        },
        {
          "id": "bond0.666",
          "type": "vlan",
          "vlan_link": "bond0",
          "vlan_id": 666,
          "vlan_mac_address": "aa:aa:aa:aa:aa:aa"
        }
      ],
      "networks": [
        {
          "id": "net-bond0.666",
          "link": "bond0.666",
          "type": "ipv4",
          "ip_address": "10.10.10.65",
          "netmask": "255.255.255.240",
          "routes": [
            {
              "network": "0.0.0.0",
              "netmask": "0.0.0.0",
              "gateway": "10.10.10.78"
            }
          ]
        }
      ],
      "services": [
        {
          "type": "dns",
          "address": "30.30.30.30"
        }
      ]
    }
```

[[Back]](./provisioned.md)