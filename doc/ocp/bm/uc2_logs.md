# OpenShift Cluster with Cilium CNI

Main workflow logs
- define cluster with Cilium CNI via RedHat Console API
- upload manifests
- download generated ISO
- boot server from ISO
- wait for server calling-home to RedHat's cloud
- initiate cluster

```
Cluster created: my-cluster [cluster-id]
Cluster install config cni patched: Cilium
Infra created: infra-id
Manifest created: rbac.authorization.k8s.io_v1_clusterrolebinding_clife-metrics-auth-rolebinding.yaml
Manifest created: apiextensions.k8s.io_v1_customresourcedefinition_ciliumconfigs.cilium.io.yaml
Manifest created: apps_v1_deployment_clife-controller-manager.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-metrics-reader.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-admin-role.yaml
Manifest created: subscription.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-manager-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrolebinding_clife-manager-rolebinding.yaml
Manifest created: v1_namespace_cilium.yaml
Manifest created: rbac.authorization.k8s.io_v1_rolebinding_clife-leader-election-rolebinding.yaml
Manifest created: v1_serviceaccount_clife-controller-manager.yaml
Manifest created: v1_service_clife-metrics.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-metrics-auth-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_role_clife-leader-election-role.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-viewer-role.yaml
Manifest created: ciliumconfig.yaml
Manifest created: operatorgroup.yaml
Manifest created: rbac.authorization.k8s.io_v1_clusterrole_clife-ciliumconfig-editor-role.yaml
Download ISO...
Redfish vmedia mapping created successfuly: 10.5.5.1
Redfish boot source set to cd successful: 10.5.5.1
Power cycle: 10.5.5.1
Server booted: 10.5.5.1
Wait for all the servers discovered...
Change hostnames and roles
- Server [10.5.5.1] hostname [sno] role [auto-assign]
REST API successful
Update ntp [ntp.domain.com]
REST API successful
Wait for cluster ready to be installed...
Start installation request...
Wait for installation started [cluster-id]...
Status changed to preparing-for-installation
Status changed to installing
Cluster reached desired state: installing
Changing servers to boot from hdd with optional vmedia eject
- 10.5.5.1
	Skipping vmedia eject for full iso
	Server boot source override set to hdd successful

Host 10.5.5.1 status changed to installing

Host 10.5.5.1 status changed to installing-in-progress

Host 10.5.5.1 status changed to installed

Installation finished...
Redfish vmedia eject successful: 10.5.5.1
Collecting cluster information...

Cluster console access
----------------------
URL      : https://console-openshift-console.apps.my-cluster.ocp.domain.com
Username : kubeadmin
Password : password


Kubeconfig
----------

apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0...
    server: https://api.my-cluster.ocp.domain.com:6443
  name: my-cluster
contexts:
- context:
    cluster: my-cluster
    user: admin
  name: admin
current-context: admin
kind: Config
preferences: {}
users:
- name: admin
  user:
    client-certificate-data: LS0...
    client-key-data: LS0...

Create ocp connector: my-cluster
Ocp connector created
Kubeadmin updated
SSH public key updated
SSH access configured in connector
Helm and virtctl access configured in connector
Check ssh access...
Prepare kubeconfig...
Kubeconfig upload successful
Kubeconfig chmod successful
```

[Back](./uc2.md)