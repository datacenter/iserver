# OpenShift - Bare Metal Cluster Life Cycle Management

## Create cluster

Steps
- check OpenShift Console API access
- check web server access and file upload
- check server Redfish access
- create cluster API request in OpenShift Console
- optional CNI manifests upload
- generated ISO download from OpenShift Console
- ISO upload to web server
- server configuration of virtual media, boot order followed with reboot
- wait until all servers discovered by OpenShift Console
- extra OpenShift Console tasks
    - change hostname
    - add ntp source
    - define ingress and api vips
- wait until cluster reaches ready to install state
- initiate installation via REST API
- wait until installation finishes
- umount/eject virtual media, change boot order
- delete iso

## Example output

```
# iserver create ocp cluster bm --dir <directory-name>
Checking openshift API...
Checking user input...
Cluster created: bm1 [uuid]
Cluster install config cni patched: Cilium
Infra created: uuid
Manifest created: cluster-network-03-cilium-ciliumconfigs-crd.yaml
Manifest created: cluster-network-06-cilium-00000-cilium-namespace.yaml
Manifest created: cluster-network-06-cilium-00001-cilium-olm-serviceaccount.yaml
Manifest created: cluster-network-06-cilium-00002-cilium-olm-deployment.yaml
Manifest created: cluster-network-06-cilium-00003-cilium-olm-service.yaml
Manifest created: cluster-network-06-cilium-00004-cilium-olm-leader-election-role.yaml
Manifest created: cluster-network-06-cilium-00005-cilium-olm-role.yaml
Manifest created: cluster-network-06-cilium-00006-leader-election-rolebinding.yaml
Manifest created: cluster-network-06-cilium-00007-cilium-olm-rolebinding.yaml
Manifest created: cluster-network-06-cilium-00008-cilium-cilium-olm-clusterrole.yaml
Manifest created: cluster-network-06-cilium-00009-cilium-cilium-clusterrole.yaml
Manifest created: cluster-network-06-cilium-00010-cilium-cilium-olm-clusterrolebinding.yaml
Manifest created: cluster-network-06-cilium-00011-cilium-cilium-clusterrolebinding.yaml
Manifest created: cluster-network-06-cilium-00012-cilium-operatorgroup.yaml
Manifest created: cluster-network-06-cilium-00013-cilium-subscription.yaml
Manifest created: cluster-network-06-cilium-00014-cilium.v1.13.0-x32540df-clusterserviceversion.yaml
Manifest created: cluster-network-07-cilium-ciliumconfig.yaml
Download ISO...
Upload iso to web server...
ISO uploaded
Redfish vmedia mapping created successfuly: <server-ip>
Redfish boot source set to cd successful: <server-ip>
Server booted: <server-ip>
Wait for all the servers discovered...
Change hostnames...
Update ntp with <ntp-ip>...
Wait for cluster ready to be installed...
Start installation request...
Wait for installation started...
Redfish vmedia eject successful: <server-ip>
Redfish boot source set to hdd successful: <server-ip>
Progress |###                             | 10/100
Host <server-ip> status changed to installing
Progress |###                             | 10/100
Host <server-ip> status changed to installing-in-progress
Progress |######################          | 69/100
Host <server-ip> status changed to installed
Progress |################################| 100/100
Installation finished...
Delete iso from web server...
Collecting cluster information...

Cluster console access
----------------------
URL      : https://<console-url>
Username : kubeadmin
Password : <temporary-kubeadmin-passowrd>
```