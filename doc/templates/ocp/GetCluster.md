
# OpenShift Container Platform (OCP)

## Get OCP Cluster settings and state

### List of clusters

```
# iserver get ocp cluster

+------------------------------+--------------------+---------+--------------+
| Name                         | Type               | Release | CNI          |
+------------------------------+--------------------+---------+--------------+
| Milan-BM1                    | assisted-installer | 4.12.9  | OVN          |
| Milan-BM2                    | assisted-installer | 4.12.9  | OVN          |
| Milan-BM5                    | assisted-installer | 4.12.9  | OVN          |
| Milan-Central-ACI-Calico     | vsphere-ipi        | 4.11.3  | Calico       |
| Milan-Edge-NXOS-OpenshiftSDN | vsphere-ipi        | 4.11.3  | OpenShiftSDN |
| Milan-Kali-Devel             | vsphere-ipi        | 4.11.3  | OpenShiftSDN |
| Milan-Kali-Kubevirt          | vsphere-ipi        | 4.11.3  | OpenShiftSDN |
| Milan-Kali-OpenshiftSDN      | vsphere-ipi        | 4.11.3  | OpenShiftSDN |
+------------------------------+--------------------+---------+--------------+
```

### Get cluster nodes state in vCenter

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view vcenter

+------------------+-------------------------------+------+--------------------------+-------------------------+-----+-------------+------------+-----+-----+------------+-----+
| Name             | vCenter                       | SF   | VM Name                  | Host                    | CPU | Usage       | Memory     | [%] | NIC | Storage    | [%] |
+------------------+-------------------------------+------+--------------------------+-------------------------+-----+-------------+------------+-----+-----+------------+-----+
| Milan-Kali-Devel | vc-iks-kali-eu-spdc.cisco.com | P+ H | devel-fnrrp-master-0     | esx72.emea-sp.cisco.com | 4   | 2.27 [GHz]  | 16.0 [GiB] | 28% | 1   | 120.0 [GB] | 13% |
|                  |                               | P+ H | devel-fnrrp-master-1     | esx71.emea-sp.cisco.com | 4   | 1.9 [GHz]   | 16.0 [GiB] | 25% | 1   | 120.0 [GB] | 8%  |
|                  |                               | P+ H | devel-fnrrp-master-2     | esx72.emea-sp.cisco.com | 4   | 2.3 [GHz]   | 16.0 [GiB] | 30% | 1   | 120.0 [GB] | 10% |
|                  |                               | P- H | devel-fnrrp-rhcos        | esx71.emea-sp.cisco.com | 2   | 0 [Hz]      | 4.0 [GiB]  | 0%  | 1   | 21.81 [GB] | 10% |
|                  |                               | P+ H | devel-fnrrp-worker-db2jd | esx72.emea-sp.cisco.com | 4   | 500.0 [MHz] | 8.0 [GiB]  | 12% | 1   | 120.0 [GB] | 6%  |
|                  |                               | P+ H | devel-fnrrp-worker-fvwck | esx71.emea-sp.cisco.com | 4   | 950.0 [MHz] | 8.0 [GiB]  | 27% | 1   | 120.0 [GB] | 9%  |
|                  |                               | P+ H | devel-fnrrp-worker-tprng | esx71.emea-sp.cisco.com | 4   | 900.0 [MHz] | 8.0 [GiB]  | 26% | 1   | 120.0 [GB] | 9%  |
|                  |                               | P+ H | ocp-devel-installer      | esx71.emea-sp.cisco.com | 1   | 0 [Hz]      | 2.0 [GiB]  | 4%  | 1   | 50.0 [GB]  | 8%  |
+------------------+-------------------------------+------+--------------------------+-------------------------+-----+-------------+------------+-----+-----+------------+-----+
```

### Verify Kubernetes API access

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view kc --verify

+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
| Name             | Type        | Release | CNI          | Kubeconfig | API FQDN          | API VIP      | API DNS      | K8s API |
+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
| Milan-Kali-Devel | vsphere-ipi | 4.11.3  | OpenShiftSDN | ✓          | api.devel.ocp.lan | 10.58.24.162 | 10.58.24.162 | ✓      |
+------------------+-------------+---------+--------------+------------+-------------------+--------------+--------------+---------+
```

### Get Installer Virtual Machine Access

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view manager

+------------------+-------------+---------+--------------+--------------+----------+----------+
| Name             | Type        | Release | CNI          | IP           | Username | Password |
+------------------+-------------+---------+--------------+--------------+----------+----------+
| Milan-Kali-Devel | vsphere-ipi | 4.11.3  | OpenShiftSDN | 10.58.24.161 | user     | pass     |
+------------------+-------------+---------+--------------+--------------+----------+----------+
```

### Verify OpenShift Console Access

- checks if the names resolve to proper addresses

```
# iserver get ocp cluster --cluster Milan-Kali-Devel --view console

+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| Name             | Console URL                                          | Expected Resolved IP | DNS Resolved IP | Authentication FQDN                | Expected Resolved IP | DNS Resolved IP | Username  | Password                |
+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
| Milan-Kali-Devel | https://console-openshift-console.apps.devel.ocp.lan | 10.58.24.163         | 10.58.24.163    | oauth-openshift.apps.devel.ocp.lan | 10.58.24.163         | 10.58.24.163    | kubeadmin | 5JZq4-RIaJ9-zQ2Ee-EkcjX |
+------------------+------------------------------------------------------+----------------------+-----------------+------------------------------------+----------------------+-----------------+-----------+-------------------------+
```

[[Back]](./README.md)