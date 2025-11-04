# OpenShift Installation on Bare Metal UCS Infrastructure

## Key Features

- [improves](./bm/assisted_installer.md) assisted installer
- zero-touch OpenShift installation on bare metal servers
- network fabric checks prior to cluster installation
- post-installation cluster configuration [tasks](./Tasks.md)

## Requirements

- RedHat console REST API one-time [configuration](./Console.md)
- servers with Redfish enabled
- internet access via imc interface for communication with RedHat Console
- web server for servers' boot from iso over http 
- no http proxy on the way between servers' imc and web server
- access to machine host network for Kubernetes API

## Workflow

![Workflow](./images/workflow.png)

## Input files

Check input files templates [repository](https://github.com/akaliwod/ocp-bm-cluster/blob/main/README.md) for examples of cluster installation definition.

Cluster installation definition files
- [cluster.json](./bm/input_data_cluster_base.md)
- [server.json](./bm/input_data_server.md)
- [redfish.json](./bm/input_data_redfish.md)
- [nmstate.yaml](./bm/input_data_nmstate.md)
- [ssh.pub](./bm/input_data_ssh_pub.md)
- [web.json](./bm/input_data_web.md)
- [proxy.json](./bm/input_data_proxy.md)

Post-installation [tasks](./Tasks.md) can be defined in tasks.json file.

## HowTo Create

```
# iserver create ocp cluster bm --dir <directory> --mode install
```

[Example output](./bm/example.md)

## Other Resources

YouTube [playlist](https://www.youtube.com/playlist?list=PLcdvTuD4ZpKZEFXzRUYvZ24Dv2_X2Atsi)


[[Back]](./Operations.md)