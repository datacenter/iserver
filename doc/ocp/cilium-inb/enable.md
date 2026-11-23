# Cilium Isovalent Network Bridge - Enable feature

## Workflow

- check cilium cni operator state
- check current cilium configuration 
- check inb access via ssh
- upload mesh certificate and key to inb
- generate and upload inb initial configuration
- run installation
- create private network
- add cluster mesh connection with inb

## Requirements

- Isovalent network bridge vm deployed and ssh accessible
- Private network [enabled](../cilium-pnet/enable.md)
- Cluster mesh [enabled](../cilium-mesh/enable.md)

## Expected outcome

![InbOverview](../images/inb/feature_overview.png)

- Isovalent network bridge initiated
- Cluster mesh established
- Isovalent network bridge k8s and linux connectors created
- Private network created (if not already exists)

## Configurable options

```
# iserver set ocp cilium inb --mode feature
  --cluster TEXT       Cluster Name
  --ip TEXT            Inb ip address
  --username TEXT      Inb ssh username
  --password TEXT      Inb ssh password
  --mesh-id INTEGER    Cluster mesh id
  --mesh-name TEXT     Cluster mesh name
  --mesh-port INTEGER  Cluster mesh port
  --cidr TEXT          POD cidr
  --pnet TEXT          Private network name
  --nic TEXT           VM network interface name
  --gateway TEXT       VM network gateway
  --no-confirm         Confirmation mode
```

## Non-configurable defaults

```
{
    "namespace": "cilium",
    "package": "clife",
    "secret": "cilium-ca-root"
}
```

## Example

```
# iserver set ocp cilium inb \
    --cluster bm3 \
    --mode feature \
    --ip 10.10.20.20 \
    --username admin \
    --password pass123 \
    --mesh-id 2 \
    --mesh-name inb1 \
    --mesh-port 32380 \
    --cidr 172.17.0.0/16 \
    --pnet vm-network \
    --nic ens224 \
    --gateway 10.10.30.254/28 \
    --no-confirm
  
OpenShift Workflow - Cilium - Initialize Isovalent Network Bridge
=================================================================

OpenShift Cluster: bm3
Cilium CNI
Cluster mesh enabled
Private network enabled

Validate input parameters
-------------------------
SSH access to inb successful
Inb interface IP addresses collected
nic ens224 found
no ip address configured
Private network already defined: vm-network
inb pod cidr does not overlap with cluster pod cidr
Cluster reinit detected
Create inb linux handler
Linux connector bm3-inb1

Generate inb config
-------------------
remote cluster ip as any worker node ip
remote cluster name from spec:cluster:name
remote cluster port from spec:clustermesh:apiserver:nodePort
tunnel port from spec:tunnelPort
health port from spec:clusterHealthPort

~~~
cluster:
  id: 2
  name: inb1
clusterHealthPort: 9940
host:
  ip: 10.10.20.20
hubble:
  timescape:
    namespace: cilium
ipam:
  podCIDR: "172.17.0.0/16"
privateNetworks:
- interface:
    name: ens224
  name: vm-network
  routes:
  - destination: 0.0.0.0/0
    gateway: 10.10.30.254
  subnets:
  - 10.10.30.0/24
remoteClusters:
- ips:
  - 10.10.10.10
  name: ocp
  port: 32379
tunnelPort: 4789

~~~
config.yaml uploaded to inb

Upload CA certificate
---------------------
Get cilium ca secret: cilium/cilium-ca-root
ca.crt uploaded to inb
ca.key uploaded to inb

Initialize inb
--------------
Sit tight...
inb kubernetes api successful

Completed tasks
- Isovalent network bridge initiated
- Cluster mesh established
- Isovalent network bridge k8s and linux connectors created
```
[[Back]](./README.md)