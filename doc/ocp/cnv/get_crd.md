# Container Virtualization Operator - Get CRDs

## Workflow

- get cnv related crds

## Example

```
# iserver get ocp cnv --cluster bm1 --view crd

OpenShift Workflow - Container Virtualization Operator - Get CRDs
=================================================================

OpenShift Cluster: bm1

Get OpenShift Virtualization CRD
--------------------------------
- AAQ
- CDIConfig
- CDI
- DataImportCron
- DataSource
- DataVolume
- ObjectTransfer
- StorageProfile
- VolumeCloneSource
- VolumeImportSource
- VolumeUploadSource
- VirtualMachineClone
- VirtualMachineExport
- OpenstackVolumePopulator
- OvirtVolumePopulator
- HyperConverged
- HostPathProvisioner
- MigrationPolicy
- NetworkAddonsConfig
- VirtualMachineClusterInstancetype
- VirtualMachinePool
- VirtualMachineRestore
- VirtualMachineSnapshotContent
- VirtualMachineSnapshot
- SSP


Containerized Data Importer (CDI) Config
----------------------------------------
- Name                          : config
- Owner                         : CDI/cdi-kubevirt-hyperconverged
- HTTP Proxy                    : http://proxy.domain.com:80
- HTTPs Proxy                   : http://proxy.domain.com:80
- No Proxy                      : domain.com,localhost
- Upload Proxy URL              : cdi-uploadproxy-openshift-cnv.apps.bm1.ocp.domain.com
- POD CPU Limits (Default)      : 750m
- POD Memory Limits (Default)   : 600M
- POD CPU Requests (Default)    : 100m
- POD Memory Requests (Default) : 60M



Containerized Data Importer (CDI)
---------------------------------
- Name  : cdi-kubevirt-hyperconverged
- Phase : Deployed
- Ready : V


+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| ID | Data Import Cron           | Schedule     | Ready | Storage | Data Source     | Data Volume                  |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 1  | centos-stream10-image-cron | 4 7/12 * * * | V     | 30Gi    | centos-stream10 | centos-stream10-e87658ffc71c |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 2  | centos-stream9-image-cron  | 4 7/12 * * * | V     | 30Gi    | centos-stream9  | centos-stream9-e6457949d4bb  |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 3  | fedora-image-cron          | 4 7/12 * * * | V     | 30Gi    | fedora          | fedora-b37907f3bbf8          |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 4  | rhel10-image-cron          | 4 7/12 * * * | V     | 30Gi    | rhel10          | rhel10-c03936a065f2          |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 5  | rhel8-image-cron           | 4 7/12 * * * | V     | 30Gi    | rhel8           | rhel8-4ccd8b6aee47           |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+
| 6  | rhel9-image-cron           | 4 7/12 * * * | V     | 30Gi    | rhel9           | rhel9-ab4ec16077fe           |
+----+----------------------------+--------------+-------+---------+-----------------+------------------------------+

+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| ID | Data Source     | Import Schedule | Ready | DV / PVC                     | DV Phase  | PVC Phase |
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+
| 1  | centos-stream10 | 4 7/12 * * *    | V     | centos-stream10-e87658ffc71c | Succeeded | Bound     |
| 2  | centos-stream9  | 4 7/12 * * *    | V     | centos-stream9-e6457949d4bb  | Succeeded | Bound     |
| 3  | fedora          | 4 7/12 * * *    | V     | fedora-b37907f3bbf8          | Succeeded | Bound     |
| 4  | rhel10          | 4 7/12 * * *    | V     | rhel10-c03936a065f2          | Succeeded | Bound     |
| 5  | rhel7           | ---             | X     | rhel7                        | Not found | Not found |
| 6  | rhel8           | 4 7/12 * * *    | V     | rhel8-4ccd8b6aee47           | Succeeded | Bound     |
| 7  | rhel9           | 4 7/12 * * *    | V     | rhel9-ab4ec16077fe           | Succeeded | Bound     |
| 8  | win10           | ---             | X     | win10                        | Not found | Not found |
| 9  | win11           | ---             | X     | win11                        | Not found | Not found |
| 10 | win2k16         | ---             | X     | win2k16                      | Not found | Not found |
| 11 | win2k19         | ---             | X     | win2k19                      | Not found | Not found |
| 12 | win2k22         | ---             | X     | win2k22                      | Not found | Not found |
| 13 | win2k25         | ---             | X     | win2k25                      | Not found | Not found | 
+----+-----------------+-----------------+-------+------------------------------+-----------+-----------+

+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| ID | Data Volume                        | POD | Bound | Ready | Access Mode | Storage | Cron | PVC                          | Phase     | Progress | Age |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 1  | default                            | X   | V     | V     | ---         | ---     |      | fedora-amber-constrictor-95  | Succeeded | 100.0%   | 3d  |
|    | fedora-amber-constrictor-95        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 2  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-2cs7h          | Succeeded | 100.0%   | 18d |
|    | mtv1-vm-61932-2cs7h                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 3  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-4cz95          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-4cz95                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 4  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-5lpt9          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-5lpt9                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 5  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-8vclm          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-8vclm                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 6  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-gr2kl          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-gr2kl                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 7  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-mwp4b          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-mwp4b                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 8  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-nncmq          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-nncmq                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 9  | default                            | X   | V     | V     | ---         | ---     |      | mtv1-vm-61932-s984h          | Succeeded | 100.0%   | 5d  |
|    | mtv1-vm-61932-s984h                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 10 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | centos-stream10-e87658ffc71c | Succeeded | 100.0%   | 3d  |
|    | centos-stream10-e87658ffc71c       |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 11 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | centos-stream9-9e58d88d8e30  | Succeeded | 100.0%   | 3d  |
|    | centos-stream9-9e58d88d8e30        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 12 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | centos-stream9-e6457949d4bb  | Succeeded | 100.0%   | 3d  |
|    | centos-stream9-e6457949d4bb        |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 13 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | fedora-b37907f3bbf8          | Succeeded | 100.0%   | 23d |
|    | fedora-b37907f3bbf8                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 14 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | rhel10-c03936a065f2          | Succeeded | 100.0%   | 23d |
|    | rhel10-c03936a065f2                |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 15 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | rhel8-4ccd8b6aee47           | Succeeded | 100.0%   | 23d |
|    | rhel8-4ccd8b6aee47                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+
| 16 | openshift-virtualization-os-images | X   | V     | V     | ---         | ---     | V    | rhel9-ab4ec16077fe           | Succeeded | 100.0%   | 23d |
|    | rhel9-ab4ec16077fe                 |     |       |       |             |         |      |                              |           |          |     |
+----+------------------------------------+-----+-------+-------+-------------+---------+------+------------------------------+-----------+----------+-----+

+----------------+
| StorageProfile |
+----------------+
| lvms-vg1       |
+----------------+


HyperConverged
--------------
- Namespace : openshift-cnv
- Name      : kubevirt-hyperconverged
- Healthy   : V
- HA        : V
- Errors    : ---

Feature Gates
- alignCPUs                   : False
- autoResourceLimits          : False
- deployKubeSecondaryDNS      : False
- deployVmConsoleProxy        : False
- disableMDevConfiguration    : False
- downwardMetrics             : False
- enableApplicationAwareQuota : False
- enableCommonBootImageImport : True
- persistentReservation       : False

Live Migration
- allowAutoConverge                 : False
- allowPostCopy                     : False
- completionTimeoutPerGiB           : 150
- completionTimeoutPerGiB           : 150
- parallelMigrationsPerCluster      : 5
- parallelOutboundMigrationsPerNode : 2
- progressTimeout                   : 150

Workload Update Strategy
- batchEvictionInterval : 1m0s
- batchEvictionSize     : 10
- workloadUpdateMethods : LiveMigrate

Virtual Machine Options
- disableFreePageReporting : False
- disableSerialConsoleLog  : True

Other Settings
- evictionStrategy           : LiveMigrate
- memoryOvercommitPercentage : 100
- vmiCPUAllocationRatio      : 10
- uninstallStrategy          : BlockUninstallIfWorkloadsExist



Network Addons Config
---------------------
- Name  : cluster
- Ready : V


+----+---------------------------------------+------------+-----+------+--------+------------+
| ID | Virtual Machine Cluster Instance Type | Size       | CPU | Numa | Memory | Huge Pages |
+----+---------------------------------------+------------+-----+------+--------+------------+
| 1  | cx1.2xlarge                           | 2xlarge    | 8   | true | 16Gi   | 2Mi        |
| 2  | cx1.2xlarge1gi                        | 2xlarge1gi | 8   | true | 16Gi   | 1Gi        |
| 3  | cx1.4xlarge                           | 4xlarge    | 16  | true | 32Gi   | 2Mi        |
| 4  | cx1.4xlarge1gi                        | 4xlarge1gi | 16  | true | 32Gi   | 1Gi        |
| 5  | cx1.8xlarge                           | 8xlarge    | 32  | true | 64Gi   | 2Mi        |
| 6  | cx1.8xlarge1gi                        | 8xlarge1gi | 32  | true | 64Gi   | 1Gi        |
| 7  | cx1.large                             | large      | 2   | true | 4Gi    | 2Mi        | 
| 8  | cx1.large1gi                          | large1gi   | 2   | true | 4Gi    | 1Gi        |
| 9  | cx1.medium                            | medium     | 1   | true | 2Gi    | 2Mi        |
| 10 | cx1.medium1gi                         | medium1gi  | 1   | true | 2Gi    | 1Gi        |
| 11 | cx1.xlarge                            | xlarge     | 4   | true | 8Gi    | 2Mi        |
| 12 | cx1.xlarge1gi                         | xlarge1gi  | 4   | true | 8Gi    | 1Gi        |
| 13 | m1.2xlarge                            | 2xlarge    | 8   | ---  | 64Gi   | 2Mi        |
| 14 | m1.2xlarge1gi                         | 2xlarge1gi | 8   | ---  | 64Gi   | 1Gi        |
| 15 | m1.4xlarge                            | 4xlarge    | 16  | ---  | 128Gi  | 2Mi        |
| 16 | m1.4xlarge1gi                         | 4xlarge1gi | 16  | ---  | 128Gi  | 1Gi        |
| 17 | m1.8xlarge                            | 8xlarge    | 32  | ---  | 256Gi  | 2Mi        |
| 18 | m1.8xlarge1gi                         | 8xlarge1gi | 32  | ---  | 256Gi  | 1Gi        |
| 19 | m1.large                              | large      | 2   | ---  | 16Gi   | 2Mi        |
| 20 | m1.large1gi                           | large1gi   | 2   | ---  | 16Gi   | 1Gi        | 
| 21 | m1.xlarge                             | xlarge     | 4   | ---  | 32Gi   | 2Mi        | 
| 22 | m1.xlarge1gi                          | xlarge1gi  | 4   | ---  | 32Gi   | 1Gi        |
| 23 | n1.2xlarge                            | 2xlarge    | 16  | ---  | 32Gi   | 1Gi        |
| 24 | n1.4xlarge                            | 4xlarge    | 32  | ---  | 64Gi   | 1Gi        |
| 25 | n1.8xlarge                            | 8xlarge    | 64  | ---  | 128Gi  | 1Gi        |
| 26 | n1.large                              | large      | 4   | ---  | 8Gi    | 1Gi        |
| 27 | n1.medium                             | medium     | 4   | ---  | 4Gi    | 1Gi        |
| 28 | n1.xlarge                             | xlarge     | 8   | ---  | 16Gi   | 1Gi        |
| 29 | o1.2xlarge                            | 2xlarge    | 8   | ---  | 32Gi   | ---        |
| 30 | o1.4xlarge                            | 4xlarge    | 16  | ---  | 64Gi   | ---        |
| 31 | o1.8xlarge                            | 8xlarge    | 32  | ---  | 128Gi  | ---        |
| 32 | o1.large                              | large      | 2   | ---  | 8Gi    | ---        |
| 33 | o1.medium                             | medium     | 1   | ---  | 4Gi    | ---        |
| 34 | o1.micro                              | micro      | 1   | ---  | 1Gi    | ---        |
| 35 | o1.nano                               | nano       | 1   | ---  | 512Mi  | ---        |
| 36 | o1.small                              | small      | 1   | ---  | 2Gi    | ---        |
| 37 | o1.xlarge                             | xlarge     | 4   | ---  | 16Gi   | ---        |
| 38 | rt1.2xlarge                           | 2xlarge    | 8   | true | 32Gi   | 1Gi        |
| 39 | rt1.4xlarge                           | 4xlarge    | 16  | true | 64Gi   | 1Gi        | 
| 40 | rt1.8xlarge                           | 8xlarge    | 32  | true | 128Gi  | 1Gi        |
| 41 | rt1.large                             | large      | 2   | true | 8Gi    | 1Gi        |
| 42 | rt1.medium                            | medium     | 1   | true | 4Gi    | 1Gi        |
| 43 | rt1.micro                             | micro      | 1   | true | 1Gi    | 1Gi        |
| 44 | rt1.small                             | small      | 1   | true | 2Gi    | 1Gi        |
| 45 | rt1.xlarge                            | xlarge     | 4   | true | 16Gi   | 1Gi        |
| 46 | u1.2xlarge                            | 2xlarge    | 8   | ---  | 32Gi   | ---        |
| 47 | u1.2xmedium                           | 2xmedium   | 2   | ---  | 4Gi    | ---        |
| 48 | u1.4xlarge                            | 4xlarge    | 16  | ---  | 64Gi   | ---        |
| 49 | u1.8xlarge                            | 8xlarge    | 32  | ---  | 128Gi  | ---        |
| 50 | u1.large                              | large      | 2   | ---  | 8Gi    | ---        |
| 51 | u1.medium                             | medium     | 1   | ---  | 4Gi    | ---        |
| 52 | u1.micro                              | micro      | 1   | ---  | 1Gi    | ---        |
| 53 | u1.nano                               | nano       | 1   | ---  | 512Mi  | ---        |
| 54 | u1.small                              | small      | 1   | ---  | 2Gi    | ---        |
| 55 | u1.xlarge                             | xlarge     | 4   | ---  | 16Gi   | ---        |
+----+---------------------------------------+------------+-----+------+--------+------------+
```

[[Back]](./README.md)