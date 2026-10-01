# Private Network - Create network

[[Back]](./README.md) [[kb]](./kb/network.md)

## Workflow

- check cilium cni operator state
- check current cilium configuration
- check private network feature [enabled](./enable.md)
- create private network based on input parameters

## Example

### Single subnet with auto-generated subnet name

```
iserver set ocp cilium pnet --cluster bm1 --mode network --network pnet1 --cidr4 10.10.10.0/24
```

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: pnet1
spec:
  subnets:
  - cidrv4: 10.10.10.0/24
    name: subnet-0
```

## Configurable options

```
# iserver set ocp cilium pnet --mode network
  --cluster TEXT                  Cluster Name
  --network TEXT                  Private network name
  --subnet TEXT                   Network subnet
  --gateway TEXT                  Network gateway
  --inb TEXT                      Network bridge
  --no-confirm                    Confirmation mode
```

Notes:
- network bridge ([inb](../cilium-inb/README.md)) optional
- if gateway defined in the cidr format, then subnet is extracted automatically
- if gateway defined as ipv4 address, then subnet must be user-defined
- gateway must belong to subnet
- gateway is optional

>[!CAUTION]
>User inputs provide limited functionality compared with ClusterwidePrivateNetwork CRD 

Limitations
- ipv6 not supported
- single subnet supported
- default gateway only

## Example

```
# iserver set ocp cilium pnet --cluster bm1 --mode network --network test --gateway 10.10.10.254/24

OpenShift Workflow - Cilium Private Network - Create Private Network
====================================================================

OpenShift Cluster: bm1
Cilium cni found
Private network enabled
Private network crds found

Create Clusterwide Private Network
----------------------------------
- name: test
- cidrv4: 10.10.10.0/24
- bridge: 
- gateway: 10.10.10.254

~~~
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: test
spec:
  networkBridges: []
  routes:
  - destination: 0.0.0.0/0
    gateway: 10.10.10.254
  subnets:
  - cidr: 10.10.10.0/24

~~~

Network created

Wait for network...

Completed tasks
- Private Network created
```

[[Back]](./README.md)