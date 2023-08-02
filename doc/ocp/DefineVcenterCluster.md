# OpenShift Container Platform (OCP)

## Device OCP Cluster for vCenter deployment

- Cluster definition is in yaml files that have to be in the same directory
- Single file with all sections supported
- If multiple files are used, keep section to single file

### vCenter

Requirements:
- single vcenter
- datacenter, datastore, folder and network must exist
- host_ip optional

```
vcenter:
  name: vc-eu-spdc.cisco.com
  ip: 10.58.28.18
  port: 443
  username: admin@admin.local
  password: whatever
  datacenter: eu-spdc-dc
  datastore: EU-SPDC-Datastore-WNAS
  cluster: eu-spdc-dc-A-blades
  folder: OCP-Central-CL
  host_ip: esx51-eu-spdc.cisco.com
  network: UC3-CL2023-Demo|K8S|519
```

### Installer virtual machine

- Installer virtual machine created from iso
- kickstart file generated based on user input
- Fedora recommended/supported
- ISO can be uploaded manually to datastore (skip iso.source in such case)

```
installer:
  ks:
    folder: linux-ks
    overwrite: False
  iso:
    source: C:\Users\akaliwod\Downloads\ocp\Fedora-Server-dvd-x86_64-36-1.5.iso
    destination: linux-iso/Fedora-Server-dvd-x86_64-36-1.5.iso
  vm:
    name: ocp-central-cl
    cpu: 1
    memory: 2048
    disk:
      size: 50
    ip: 10.58.24.97
    username: root
    password: cisco
```

### OCP Main Settings

- ocp.release defines the desired OCP distribution available at public [repository](https://mirror.openshift.com/pub/openshift-v4/amd64/clients/ocp)

```
ocp:
  name: Milan-Central-ACI-Calico
  installation: vsphere-ipi
  release: 4.11.3
  source: web
  cluster:
    name: cl-bgp
    domain: ocp.lan
    api_vip: 10.58.24.98
    ingress_vip: 10.58.24.99
    master:
      hyperthreading: True
      replicas: 3
      cpu: 4
      memory: 16384
      disk:
        size: 120
    worker:
      hyperthreading: True
      replicas: 3
      cpu: 4
      memory: 8192
      disk:
        size: 120
```

### HTTP Proxy

- optional
- if defined, proxy settings are used at installer virtual machine and OCP cluster definition yaml

```
proxy:
  enabled: True
  http: http://proxy.esl.cisco.com:80
  https: http://proxy.esl.cisco.com:80
  no_proxy: .cisco.com
```

### SSH Keys

- optional
- if defined, extra ssh keys are added to OCP cluster definition yaml
- multiple keys supported
- this way you can ssh-access the clusted nodes from other hosts
- otherwise, cluster nodes can be only accessed from the installer virtual machine

```
ssh:
  - 'ssh-ed25519 AAAA.. user@host'
  - 'ssh-ed25519 AAAA.. user@host'
```

### Linux Jump Host

- optional
- generation of kickstart iso image requires genisoimage application
- if it is available on the host where iserver runs then no need to define jump host
- otherwise define the jump host where genisoimage is available

```
jump:
  ip: 10.58.28.207
  username: user
  password: pass
```

### DNS Settings

- named is installed on installer virtual machine (dns.managed: True)
- this DNS server will be configured on all cluster nodes via OCP configuration yaml setting
- dns.forwarders will be configured in named
- it is mandatory to provide proper dns forwarder as OCP installation is pulling binaries from internet

```
dns:
  managed: True
  forwarders: 144.254.71.184
```

### DHCP Settings

- dhcpd is installed on the installer virtual machine
- all cluster nodes are configured with dhcp client and will get IP address from this dhcp server
- make sure to define range for master and worker nodes as well as ephemeral bootstrap virtual machine created by OCP cluster installer

```
dhcp:
  subnet: 10.58.24.96/28
  gateway: 10.58.24.109
  range: 10.58.24.100-10.58.24.106
  dns:
    servers: 144.254.71.184
    domain: cisco.com
  ntp:
    servers: 144.254.15.78
    timezone: Europe/Rome
```

### CNI

- the minimum mandatory CNI section must contain cni.type with OpenShiftSDN, OVNKubernetes, or Calico value

```
cni:
    type: OpenShiftSDN
```

- POD and Service CIDR as well as host prefix can be customized from default values

```
cni:
  type: OpenShiftSDN
  v4cidr: 10.128.0.0/14
  v4hostPrefix: 23
  v4serviceNetwork: 172.30.0.0/16
```

- in case of Calico, bgp settings can be defined

```
bgp:
  local_as: 65321
  remote_as: 50000
  peer:
  - 10.58.24.108
  - 10.58.24.109
  mesh: true
  external_ips:
  - 172.70.66.0/24
  - 172.70.66.66/32,1:128
  - 172.70.66.67/32,1:128
```

### Pull secret

- access console.redhat.com
- navigate to create new cluster, datacenter, vSphere
- download pull secret
- save it to ./secret/pull-secret.txt in the directory where yaml files are

![OcpVcenterPullSecret](images/ocp_vcenter_pull_secret.png)

[[Back]](./README.md)