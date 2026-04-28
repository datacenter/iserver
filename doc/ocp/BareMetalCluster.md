# OpenShift Installation on Bare Metal UCS Infrastructure

[[Back]](./Operations.md) [[Next]](./VcenterCluster.md)

![Workflow](./images/workflow.png)

## Key Features

- [improves](./bm/assisted_installer.md) assisted installer
- zero-touch OpenShift installation on bare metal servers
- network fabric checks prior to cluster installation
- post-installation cluster configuration [tasks](./Tasks.md)

## Requirements

- RedHat console REST API one-time [configuration](./Console.md)
- Redfish-enabled servers with internet access
- web server for virtual-media-boot-from-iso

## Input files

> [!NOTE]
> Refer to [repository](https://wwwin-github.cisco.com/emear-telcocloud/ocp-bm-cluster/blob/master/README.md) for examples of cluster installation definition.

### All-in-one

- [cluster.json](./bm/input_data_cluster_aio.md)

### File-per-section

- [cluster.json](./bm/input_data_cluster_base.md)
- [server.json](./bm/input_data_server.md)
- [redfish.json](./bm/input_data_redfish.md)
- [nmstate.yaml](./bm/input_data_nmstate.md)
- [ssh.pub](./bm/input_data_ssh_pub.md)
- [web.json](./bm/input_data_web.md)
- [proxy.json](./bm/input_data_proxy.md)

Post-installation [tasks](./Tasks.md) can be defined in tasks.json file.

### Cilium manifests

In case of Cilium CNI, unpack all manifests into `manifests` directory

```
$ find my-cluster-input-data
manifests/subscription.yaml
manifests/...
cluster.json
...
```

> [!NOTE]
> No need to modify default manifests, [auto-fixups](./bm/cilium_fixup.md) will handle cidr and operator replica count

## RunIt

```
# iserver create ocp cluster bm --dir <directory> --mode install
```

Checks (fail-fast approach)
- [input file syntax](./bm/example_input_data_check.md)
- [OpenShift API](./bm/example_openshift_api_check.md)
- [web server](./bm/example_web_check.md)
- [redfish](./bm/example_redfish_check.md)
- [dns](./bm/example_fqdn_check.md)
- [nmstate and variables](./bm/example_variables_check.md)
- [OpenShift Console REST API body generation](./bm/example_console_body_generation.md)

Execution (run until completion)
- [create cluster, infra and manifests](./bm/example_create_cluster.md)
- [iso download, manipulation and upload to web server](./bm/example_iso.md)
- [vmedia boot and wait for call-back-home](./bm/example_boot.md)
- [extra configuration](./bm/example_extra_configuration.md)
- [wait for completion](./bm/example_wait.md)
- [post installation](./bm/example_post.md)

[[Back]](./Operations.md) [[Next]](./VcenterCluster.md)