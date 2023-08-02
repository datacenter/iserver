
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
# iserver delete ocp cluster .\samples\ocp\cluster\vcenter\devel
Input parameters verification...
vsphere-ipi ocp delete workflow...
Check installer virtual machine...
Check ocp installation state...
Destroy OCP cluster...

Run script
----------

Script filename: C:\kali\cisco\devel\iserver\templates\ocp\vsphere-ipi\files\uninstall.sh

DEBUG OpenShift Installer 4.11.3
DEBUG Built from commit 701ca84cd9616daf8bc7c126eb99d104a3bb5aa7
DEBUG Power Off Virtual Machines
DEBUG Find attached VirtualMachine on tag
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-master-0
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-master-1
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-master-2
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-worker-wg822
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-worker-djg8l
DEBUG Powered off                                   VirtualMachine=devel-zfmzp-worker-br7rt
DEBUG Delete Virtual Machines
DEBUG Find attached VirtualMachine on tag
INFO Destroyed                                     VirtualMachine=devel-zfmzp-rhcos
INFO Destroyed                                     VirtualMachine=devel-zfmzp-master-0
INFO Destroyed                                     VirtualMachine=devel-zfmzp-master-1
INFO Destroyed                                     VirtualMachine=devel-zfmzp-master-2
INFO Destroyed                                     VirtualMachine=devel-zfmzp-worker-wg822
INFO Destroyed                                     VirtualMachine=devel-zfmzp-worker-djg8l
INFO Destroyed                                     VirtualMachine=devel-zfmzp-worker-br7rt
DEBUG Delete Folder
DEBUG Find attached Folder on tag
DEBUG All folders deleted
DEBUG Delete Storage Policy
INFO Destroyed                                     StoragePolicy=openshift-storage-policy-devel-zfmzp
DEBUG Delete                                        Tag=devel-zfmzp
INFO Deleted                                       Tag=devel-zfmzp
DEBUG Delete                                        TagCategory=openshift-devel-zfmzp
INFO Deleted                                       TagCategory=openshift-devel-zfmzp
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
Virtual Machine powered off: ocp-devel-installer
The current powerState is: poweredOff
Virtual Machine destroyed: ocp-devel-installer
Completed
OCP instance deleted: Milan-Kali-Devel

Info: finished in 79747 ms and logs saved in /tmp/iserver\ba64ea48b931
```

[[Back]](./README.md)