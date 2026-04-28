# server.json

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_redfish.md) [[Prev]](./input_data_cluster_base.md)

- List of servers with 1, 3 or more items
- redfish authentication local or from [redfish.json](./input_data_redfish.md)
- templated [nmstate.yaml](./input_data_nmstate.md) for network configuration
- mix of endpoint types supported i.e., FI and directly attached
- redfish endpoint types: ucsc (def), bmc, fi
- server role assignment for 3+ clusters
- single server selected as [management](../ManagementServer.md) with `kube:true`

> [!CAUTION]
> 2 servers installation is not supported by OpenShift

## Example

```json
[
  {
      "hostname": "bm1-1",
      "kube": true,
      "redfish": {
          "endpoint_ip": "10.1.1.1",
          "username": "admin",
          "password": "pass"
      },
      "ssh": {
          "ip": "10.2.2.2"
      },
      "vlan": 666,
      "interface": [
          {
              "name": "eno5",
              "mac": "aa:aa:aa:aa:aa:aa"
          },
          {
              "name": "eno6",
              "mac": "bb:bb:bb:bb:bb:bb"
          }
      ],
      "nmstate": "nmstate.yaml",
      "variables": {
        ...
      }
  }
]
```

## Fabric Interconnect

If server is connected to Fabric Interconnect

```
      "redfish": {
          "endpoint_type": "fi",
          "inventory_type": "Server",
          "inventory_id": "ID-of-the-server",
          "endpoint_ip": "10.1.1.1",
          "endpoint_port": "443",
          "username": "admin",
          "password": "pass"
      },
```

where endpoint_ip will be of Fabric Interconnect

Check inventory IDs using

```
$ iserver get redfish fi --ip 10.1.1.1 --username admin --password pass
+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+
| Inventory Type | Chassis Id | Inventory Id (IOM1) | Inventory Id (IOM2) | Chassis Name | Chassis Model | Chassis Serial |
+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+
| Chassis        | chassis-1  | IoCard-1-1          | IoCard-1-2          | my-name      | UCSX-9508     | my-serial      |
+----------------+------------+---------------------+---------------------+--------------+---------------+----------------+

+----------------+--------------+------------+--------------+---------------+
| Inventory Type | Inventory Id | Chassis Id | Server Model | Server Serial |
+----------------+--------------+------------+--------------+---------------+
| Server         | my-server1   | chassis-1  | UCSX-210C-M6 | my-serial1    |
| Server         | my-server2   | chassis-1  | UCSX-210C-M6 | my-serial2    |
| Server         | my-server3   | chassis-1  | UCSX-210C-M6 | my-serial3    |
| Server         | my-server4   | chassis-1  | UCSX-210C-M6 | my-serial4    |
+----------------+--------------+------------+--------------+---------------+ 
```

## Server attributes

### kube:true

- make sure only single server has kube:true, this is where cli tools are going to be installed
- if kube:true is not defined, the first server on the list is set with kube:true

### ssh

- ssh.username defaults to 'core' value and is optional
- ssh.ip must belong to cluster's machine network subnet

### redfish

- redfish.endpoint_type defaults to 'ucsc' value 
- redfish.endpoint_port defaults to 443 value 
- redfish credentials can be in [redfish.json](./input_data_redfish.md) file

### interface

- max of 2 interfaces can be defined in the liast
- [nmstate-yaml](./input_data_nmstate.md) file must exist in the same directory 
- all variables must [resolve](https://wwwin-github.cisco.com/emear-telcocloud/ocp-bm-cluster/blob/master/variables.md)

[[Back]](../BareMetalCluster.md) [[Next]](./input_data_redfish.md) [[Prev]](./input_data_cluster_base.md)