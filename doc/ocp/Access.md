# OpenShift Cluster Access

OpenShift cluster must be defined in iserver for any day2 [operations](./Operations.md) with cluster name provided using --cluster parameter. This reference is further called connector. 

```
# iserver get k8s node --cluster bm1
# iserver set ocp nfd --cluster bm1
```

Connector definition is local to the machine where iserver runs on. It is stored in user's local directory structure e.g. "/home/user/.itool" or "C:\Users\user\.itool". It is highly recommended to not manually change anything in this directory.

Cluster installed via iserver has connector created automatically.

## Connector

- (locally significant) cluster name e.g. bm1
- [domain name](./Domain.nd) (optional)
- kubeconfig file (mandatory)
- ssh public key for cluster nodes' access (optional)
- ip address of cluster node (aka management node), with cli tools (optional)

### workflow and connector

- day2 operations workflows always require kubernetes API (kubeconfig required)
- some day2 operations workflows run commands via ssh on the cluster nodes (ssh public key required)
- some day2 operations workflows depend on [cli tools](./cli/README.md) such as helm or virtctl (ssh public key and management ip required)

## Add connector

```
# iserver set ocp connector --cluster test --kubeconfig C:\tmp\kubeconfig

OpenShift Cluster
-----------------
- new cluster: test
- kubeconfig set
- ssh public key not modified and currently unset
- management ip not modified and currently unset
- domain not modified and currently unset
```

## Get connectors

```
# iserver get ocp connector

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | local  | ✓          | ✓              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+
```

Note:
- use --cluster option to select cluster by name
- use --domain option to select clusters by domain

## Check access

```
# iserver get ocp connector -v access

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | local  | ✓          | ✓              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+

Collect cluster access |################################| 1/1

+---------+------------------------+-------------------------+-----+------+-----+
| Cluster | API                    | Ingress                 | DNS | Kube | SSH |
+---------+------------------------+-------------------------+-----+------+-----+
| bm1     | api.bm1.ocp.domain.com | apps.bm1.ocp.domain.com | ✓   | ✓    | ✓   | 
+---------+------------------------+-------------------------+-----+------+-----+
```

Note:
- use --cluster option to select cluster by name
- use --domain option to select clusters by domain

## Check cli

```
# iserver get ocp connector -v cli

+---------+--------+------------+----------------+---------------+
| Cluster | Domain | Kubeconfig | SSH Public Key | Management IP |
+---------+--------+------------+----------------+---------------+
| bm1     | local  | ✓          | ✓              | 10.10.10.10   |
+---------+--------+------------+----------------+---------------+

Collect cluster access |################################| 1/1

+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
| Cluster | API                    | Ingress                 | DNS | Kube | SSH | Mgmt SSH | cilium | hubble | helm | virtctl |
+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
| bm5     | api.bm1.ocp.domain.com | apps.bm1.ocp.domain.com | ✓   | ✓    | ✓   | ✓        | ✓      | ✓      | ✓    | ✓       | 
+---------+------------------------+-------------------------+-----+------+-----+----------+--------+--------+------+---------+
```

Note:
- use --cluster option to select cluster by name
- use --domain option to select clusters by domain

## Modify connector

```
# iserver set ocp connector --cluster test --domain local --ssh C:\Users\user\.ssh\id_ed25519.pub                 

OpenShift Cluster
-----------------
- existing cluster: test
- kubeconfig not modified
- ssh public key set
- management ip not modified and currently unset
- domain set
```

## Delete connector

```
# iserver delete ocp connector --cluster test
Cluster deleted: test
```

[[Back]](./Operations.md)