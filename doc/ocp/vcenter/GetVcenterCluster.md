# OpenShift Container Platform (OCP)

## Get OCP Cluster settings and state

### List of clusters

```
# iserver get ocp cluster

+------------------------------+--------------------+---------+--------------+
| Name                         | Type               | Release | CNI          |
+------------------------------+--------------------+---------+--------------+
| <name>                       | assisted-installer | <ver>   | OVN          |
| <name>                       | vsphere-ipi        | <ver>   | Calico       |
+------------------------------+--------------------+---------+--------------+
```

### Get cluster nodes state in vCenter

```
# iserver get ocp cluster --cluster <name> --view vcenter

+------------------+-------------------------------+------+------------------------+--------+-----+-------------+------------+-----+-----+------------+-----+
| Name             | vCenter                       | SF   | VM Name                | Host   | CPU | Usage       | Memory     | [%] | NIC | Storage    | [%] |
+------------------+-------------------------------+------+------------------------+--------+-----+-------------+------------+-----+-----+------------+-----+
| <name>           | <vcenter>                     | P+ H | <vm-base>-master-0     | <host> | 4   | 2.27 [GHz]  | 16.0 [GiB] | 28% | 1   | 120.0 [GB] | 13% |
|                  |                               | P+ H | <vm-base>-master-1     | <host> | 4   | 1.9 [GHz]   | 16.0 [GiB] | 25% | 1   | 120.0 [GB] | 8%  |
|                  |                               | P+ H | <vm-base>-master-2     | <host> | 4   | 2.3 [GHz]   | 16.0 [GiB] | 30% | 1   | 120.0 [GB] | 10% |
|                  |                               | P- H | <vm-base>-rhcos        | <host> | 2   | 0 [Hz]      | 4.0 [GiB]  | 0%  | 1   | 21.81 [GB] | 10% |
|                  |                               | P+ H | <vm-base>-worker-db2jd | <host> | 4   | 500.0 [MHz] | 8.0 [GiB]  | 12% | 1   | 120.0 [GB] | 6%  |
|                  |                               | P+ H | <vm-base>-worker-fvwck | <host> | 4   | 950.0 [MHz] | 8.0 [GiB]  | 27% | 1   | 120.0 [GB] | 9%  |
|                  |                               | P+ H | <vm-base>-worker-tprng | <host> | 4   | 900.0 [MHz] | 8.0 [GiB]  | 26% | 1   | 120.0 [GB] | 9%  |
|                  |                               | P+ H | <name>                 | <host> | 1   | 0 [Hz]      | 2.0 [GiB]  | 4%  | 1   | 50.0 [GB]  | 8%  |
+------------------+-------------------------------+------+------------------------+--------+-----+-------------+------------+-----+-----+------------+-----+
```

### Verify Kubernetes API access

```
# iserver get ocp cluster --cluster <name> --view kc --verify

+--------+-------------+---------+--------------+------------+--------------+--------------+--------------+---------+
| Name   | Type        | Release | CNI          | Kubeconfig | API FQDN     | API VIP      | API DNS      | K8s API |
+--------+-------------+---------+--------------+------------+--------------+--------------+--------------+---------+
| <name> | vsphere-ipi | <ver>   | OpenShiftSDN | ✓          | api.<domain> | <ip>         | <ip>         | ✓      |
+--------+-------------+---------+--------------+------------+--------------+--------------+--------------+---------+
```

### Get Installer Virtual Machine Access

```
# iserver get ocp cluster --cluster <name> --view manager

+--------+-------------+---------+--------------+------+----------+----------+
| Name   | Type        | Release | CNI          | IP   | Username | Password |
+--------+-------------+---------+--------------+------+----------+----------+
| <name> | vsphere-ipi | <ver>   | OpenShiftSDN | <ip> | user     | pass     |
+--------+-------------+---------+--------------+------+----------+----------+
```

### Verify OpenShift Console Access

- checks if the names resolve to proper addresses

```
# iserver get ocp cluster --cluster <name> --view console

+--------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| Name   | Console URL                                          | Expected Resolved IP | DNS Resolved IP | Authentication FQDN                | Expected Resolved IP | DNS Resolved IP | Username  | Password                |
+--------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| <name> | https://console-openshift-console.apps.<domain>      | <ingress>            | <ingress>       | oauth-openshift.apps.<domain>      | <ingress>            | <ingress>       | kubeadmin | ********                |
+--------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
```

[[Back]](../VcenterCluster.md)