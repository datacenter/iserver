# server.json

List of servers with 1, 3 or more items. 

Note: 2 servers installation is not supported by OpenShift.

## Example

- server with direct RedFish access to IMC

```
[
  {
      "hostname": "bm1-1",
      "kube": true,
      "redfish": {
          "endpoint_type": "ucsc",
          "endpoint_ip": "10.1.1.1",
          "endpoint_port": "443",
          "username": "admin",
          "password": "pass"
      },
      "ssh": {
          "ip": "10.2.2.2",
          "username": "core"
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

## Minimum

- redfish credentials in [redfish.json](./input_data_redfish.md)
- nmstate yaml contains generated variables only

```
[
  {
      "hostname": "bm1-1",
      "redfish": {
          "endpoint_ip": "10.1.1.1"
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
      "nmstate": "nmstate.yaml"
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
- all variables must [resolve](https://github.com/akaliwod/ocp-bm-cluster/blob/master/variables.md)

## Server connectivity check

You can add fabric connectivity check per-interface as in the following example, currently supported for aci only

```
[
  {
      "hostname": "bm1-1",
      "interface": [
          {
              "name": "eno5",
              "mac": "aa:aa:aa:aa:aa:aa",
              "aci": {
                "apic": "my-apic",
                "node": 100,
                "port": "1/1/1"
              }
          },
          {
              "name": "eno6",
              "mac": "bb:bb:bb:bb:bb:bb",
              "aci": {
                "apic": "myapic",
                "node": 200,
                "port": "1/1/1"
              }
          }
      ]
  }
]
```

In the verfication phase of the workflow, before the actual installation starts, connectivity will be checked for example

```
ACI Workflow - Check interface
==============================


+------+------+--------+------+-------+-------+-------------+----------------+-------------------+------+------+-------+------------------------+
| Ctx  | Sync | Apic   | Node | Port  | State | IP          | Gateway        | MAC               | Bond | Vlan | Trunk | Info                   |
+------+------+--------+------+-------+-------+-------------+----------------+-------------------+------+------+-------+------------------------+
| node | ✓    | myapic | 100  | 1/1/1 | up    | 10.10.10.10 | 10.10.10.1/24  | aa:aa:aa:aa:aa:aa | True | 666  | True  | IP EP 100:1/1/1        |
|      |      |        |      |       |       |             |                |                   |      |      |       | IP EP 200:1/1/1        |
|      |      |        |      |       |       |             |                |                   |      |      |       | L3Out name             |
|      |      |        |      |       |       |             |                |                   |      |      |       | MAC EP 100:1/1/4       |
|      |      |        |      |       |       |             |                |                   |      |      |       | MAC EP 200:1/1/4       |
|      |      |        |      |       |       |             |                |                   |      |      |       | PV/VPC PG name         |
+------+------+--------+------+-------+-------+-------------+----------------+-------------------+------+------+-------+------------------------+
| node | ✓    | myapic | 200  | 1/1/1 | up    | 10.10.10.10 | 10.10.10.1/24  | bb:bb:bb:bb:bb:bb | True | 666  | True  | IP EP 2208:1/1/4       |
|      |      |        |      |       |       |             |                |                   |      |      |       | IP EP 200:1/1/1        |
|      |      |        |      |       |       |             |                |                   |      |      |       | L3Out name             |
|      |      |        |      |       |       |             |                |                   |      |      |       | MAC EP not found       |
|      |      |        |      |       |       |             |                |                   |      |      |       | PV/VPC PG name         |
+------+------+--------+------+-------+-------+-------------+----------------+-------------------+------+------+-------+------------------------+
```

[Back](../BareMetalCluster.md)