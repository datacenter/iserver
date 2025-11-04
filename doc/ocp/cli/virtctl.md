# Virtctl

Add virtctl cli on the cluster [management node](../Access.md)

## Workflow

- if --url value is not defined then url defaults to https://hyperconverged-cluster-cli-download-openshift-cnv.CLUSTER-DOMAIN/amd64/linux/virtctl.tar.gz
- download tarball
- upload tarball to cluster's management node 
- unpack and prepare binary in /usr/local/bin

## Requirements

Virtualization [operator](../cnv/create_operator.md) and [instance](../cnv/create_instance.md) ready

## Expected Outcome

```
$ ssh core@10.10.10.10                                  
[core@bm1 ~]$ which virtctl
/usr/local/bin/virtctl
[core@bm1 ~]$ virtctl --help
virtctl controls virtual machine related operations on your kubernetes cluster.

Available Commands:
  addvolume         add a volume to a running VM
  adm               Administrate KubeVirt configuration.
  completion        Generate the autocompletion script for the specified shell
  console           Connect to a console of a virtual machine instance.
  create            Create a manifest for the specified Kind.
  credentials       Manipulate credentials on a virtual machine.
  expand            Return the VirtualMachine object with expanded instancetype and preference.
  expose            Expose a virtual machine instance, virtual machine, or virtual machine instance replica set as a new service.
  fslist            Return full list of filesystems available on the guest machine.
  guestfs           Start a shell into the libguestfs pod
  guestosinfo       Return guest agent info about operating system.
  help              Help about any command
  image-upload      Upload a VM image to a DataVolume/PersistentVolumeClaim.
  memory-dump       Dump the memory of a running VM to a pvc
  migrate           Migrate a virtual machine.
  migrate-cancel    Cancel migration of a virtual machine.
  pause             Pause a virtual machine
  permitted-devices List the permitted devices for vmis.
  port-forward      Forward local ports to a virtualmachine or virtualmachineinstance.
  removevolume      remove a volume from a running VM
  restart           Restart a virtual machine.
  scp               SCP files from/to a virtual machine instance.
  soft-reboot       Soft reboot a virtual machine instance
  ssh               Open a SSH connection to a virtual machine instance.
  start             Start a virtual machine.
  stop              Stop a virtual machine.
  unpause           Unpause a virtual machine
  usbredir          Redirect an USB device to a virtual machine instance.
  userlist          Return full list of logged in users on the guest machine.
  version           Print the client and server version information.
  vmexport          Export a VM volume.
  vnc               Open a vnc connection to a virtual machine instance.
```

## Configurable options

```
# iserver set ocp cli-virtctl 
  --cluster TEXT  OCP cluster name
  --url TEXT      Virtctl package url
```

## Example

```
# iserver set ocp cli-virtctl --cluster bm1


OpenShift Workflow - Install virtctl cli
========================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "url": null,
    "confirmation": true,
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok
- management node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok

Cnv operator installed
Cnv hyperconverged instance created
Check for cluster endpoint to download virtctl binary from [timeout:30]...
Wait for endpoint openshift-cnv/hyperconverged-cluster-cli-download...
Downloading virtctl binary from https://hyperconverged-cluster-cli-download-openshift-cnv.apps.bm1.domain.com/amd64/linux/virtctl.tar.gz
Uploading virtctl binary to cluster management node
Unpack
Change file flags
Virtctl binary ready to be used
Client Version: version.Info{GitVersion:"v1.4.1-75-gb3a54913fd", GitCommit:"b3a54913fdd2a892713e9de0577c8009c273ecf1", GitTreeState:"clean", BuildDate:"2025-09-25T17:03:04Z", GoVersion:"go1.22.12 (Red Hat 1.22.12-3.el9_5) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
Server Version: version.Info{GitVersion:"v1.4.1-75-gb3a54913fd", GitCommit:"b3a54913fdd2a892713e9de0577c8009c273ecf1", GitTreeState:"clean", BuildDate:"2025-09-25T16:48:58Z", GoVersion:"go1.22.12 (Red Hat 1.22.12-3.el9_5) X:strictfipsruntime", Compiler:"gc", Platform:"linux/amd64"}
```

[[Back]](./README.md)