# Server

List of server definitions with at least 1 item. List must have 1, 3 or more items. 2 servers deployment is not supported by OpenShift.

## cluster.json

Servers can be defined in cluster.json

```
{
  "name": "bm1",
  "openshift_version": "4.17.2",
  "cpu_architecture": "x86_64",
  "server": [
    {
      "hostname": "bm1-1",
      ...
    }
  ],
  ...
}
```

## server.json

Servers can be defined in server.json

```
[
  {
    "hostname": "bm1-1",
    ...
  }
]
```

## Server definition example

```
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
```

Notes:
- make sure only single server has kube:true, this is where cli tools are going to be installed
- ssh.username defaults to 'core' value and is optionl
- redfish.endpoint_type defaults to 'ucsc' value and is optional
- redfish.endpoint_port defaults to 443 value and is optional
- redfish credentials can be in redfish.json file
- [nmstate-yaml](./input_data_nmstate.md) file must exist in the root directory
- all variables must resolve

[Back](../BareMetalCluster.md)