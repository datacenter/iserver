# OpenShift Container Platform (OCP)

## Delete OCP Cluster from vCenter

Example:

```
# iserver delete ocp cluster .\samples\ocp\cluster\vcenter\devel
```

where the directory must contain cluster definition and pull secret. That's all you need to do.

Delete workflow:
- access installer virtual machine
- run './openshift-install destroy cluster --log-level debug --dir install' command
- destroy installer virtual machine

```
# iserver delete ocp cluster <dir>
Input parameters verification...
vsphere-ipi ocp delete workflow...
Check installer virtual machine...
Check ocp installation state...
Destroy OCP cluster...

Run script
----------

Script filename: <path>

DEBUG OpenShift Installer <version>
DEBUG Built from commit <id>
DEBUG Power Off Virtual Machines
DEBUG Find attached VirtualMachine on tag
DEBUG Powered off                                   VirtualMachine=<vm-base>-master-0
DEBUG Powered off                                   VirtualMachine=<vm-base>-master-1
DEBUG Powered off                                   VirtualMachine=<vm-base>-master-2
DEBUG Powered off                                   VirtualMachine=<vm-base>-worker-wg822
DEBUG Powered off                                   VirtualMachine=<vm-base>-worker-djg8l
DEBUG Powered off                                   VirtualMachine=<vm-base>-worker-br7rt
DEBUG Delete Virtual Machines
DEBUG Find attached VirtualMachine on tag
INFO Destroyed                                     VirtualMachine=<vm-base>-rhcos
INFO Destroyed                                     VirtualMachine=<vm-base>-master-0
INFO Destroyed                                     VirtualMachine=<vm-base>-master-1
INFO Destroyed                                     VirtualMachine=<vm-base>-master-2
INFO Destroyed                                     VirtualMachine=<vm-base>-worker-wg822
INFO Destroyed                                     VirtualMachine=<vm-base>-worker-djg8l
INFO Destroyed                                     VirtualMachine=<vm-base>-worker-br7rt
DEBUG Delete Folder
DEBUG Find attached Folder on tag
DEBUG All folders deleted
DEBUG Delete Storage Policy
INFO Destroyed                                     StoragePolicy=openshift-storage-policy-<vm-base>
DEBUG Delete                                        Tag=<vm-base>
INFO Deleted                                       Tag=<vm-base>
DEBUG Delete                                        TagCategory=openshift-<vm-base>
INFO Deleted                                       TagCategory=openshift-<vm-base>
DEBUG Purging asset "Metadata" from disk
DEBUG Purging asset "Master Ignition Customization Check" from disk
DEBUG Purging asset "Worker Ignition Customization Check" from disk
DEBUG Purging asset "Terraform Variables" from disk
DEBUG Purging asset "Kubeconfig Admin Client" from disk
DEBUG Purging asset "Kubeadmin Password" from disk
DEBUG Purging asset "Certificate (journal-gatewayd)" from disk
DEBUG Purging asset "Cluster" from disk
INFO Time elapsed: 53s
The current powerState is: poweredOn
Virtual Machine powered off: <name>
The current powerState is: poweredOff
Virtual Machine destroyed: <name>
Completed
OCP instance deleted: <name>
```

[[Back]](../VcenterCluster.md)