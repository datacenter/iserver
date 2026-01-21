# Management server

While most of the OpenShift [operations](./Operations.md) use REST API only, there are few that require running [CLI commands](./cli/README.md) on the management server over SSH. 

Management server := Linux server with [CLI commands](../cli/README.md) executed by iserver via ssh in order to interact with OpenShift cluster as defined locally in kubeconfig file. 

When OpenShift cluster is [installed](../BareMetalCluster.md) by iserver, the selected node of the cluster is prepared and configured to be the management node.

In case OpenShift cluster was installed differently, it is still recommended to dedicate one of the nodes (e.g. control plane node) to be management node.

## HowTo

![Overview](./images/management.png)

## Check cluster definition

```
# iserver get ocp connector --cluster bm1

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | ---    | V          | V              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+
```

Notes:
- [domain](./Domain.md) not important here
- kubeconfig defined locally at iserver <=> Kubernetes REST API can be executed to remote OpenShift cluster
- ssh public key defined locally at iserver <=> when ssh to OpenShift cluster node, iserver will use the configured ssh key
- management server ip address defined <=> when CLI commands in the context of OpenShift cluster have to be executed, iserver will ssh to this server
- the above output confirms connector definition only

## Check cluster access

```
# iserver get ocp connector --cluster bm1 -v cli

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | ---    | V          | V              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+

OpenShift Cluster: bm1
Collect cluster access |################################| 1/1

+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
| Cluster | API                    | Ingress                 | DNS | Kube | SSH | Mgmt SSH | cilium | hubble | helm | virtctl |
+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
| bm1     | api.bm1.ocp.domain.com | apps.bm1.ocp.domain.com | V   | V    | V   | V        | V      | X      | X    | X       | 
+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
```

## Define management server IP address

```
# iserver set ocp connector --cluster bm1 --mgmt 10.10.10.10

OpenShift Cluster
-----------------
- existing cluster: bm1
- kubeconfig not modified
- ssh public key not modified
- management host ip address set
- domain not modified
```

Note:
- this command defines the ip address 
- use 'get ocp connector -v cli' command as above to check if functionally setup is fine

## Define management server SSH public key

```
# iserver set ocp connector --cluster bm1 --ssh $HOME/.ssh/id_ed25519.pub

OpenShift Cluster
-----------------
- existing cluster: bm1
- kubeconfig not modified
- ssh public key set
- management host ip address not modified
- domain not modified
```

Note:
- this command defines the ssh public key location
- public key is copied to internal iserver filesystem
- if public key changes, you need to rerun this command
- make sure that public key is authorized to access OpenShift cluster as per [documentation](./ssh/README.md)

## CLI tools on the management node

CLI command line tools do not have to be prepared manually Check [CLI Tools](./cli/README.md) for details how to automate it.

[[Back]](../Operations.md)