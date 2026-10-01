# Cat8000v: management in pod network

[[Back]](./README.md) [[KubeVirt Networking]](./example-cat8k-pod-kubevirt.md)

## Overview

Provisioning
- cat8000v instance: 1 vCPU, 4G memory, 10G disk (pvc) from http-sourced image 
- single interface management (GigabitEthernet1) configured with DHCP and connected to Kubernetes POD network
- cat8000v instance has different IP and MAC than virt-launcher POD due to masquerade mode

Packet forwarding
  - kubernetes managed incl. network polic and observability
  - egress: POD IP translated to node's IP address
  - ingress: kubernetes service

Check kubevirt networking details [here](./example-cat8k-pod-kubevirt.md)

[Masquerade mode](https://kubevirt.io/user-guide/network/interfaces_and_networks/#masquerade)

> In masquerade mode, KubeVirt allocates internal IP addresses to virtual machines and hides them behind NAT. All the traffic exiting virtual machines is "source NAT'ed" using pod IP addresses; thus, cluster workloads should use the pod's IP address to contact the VM over this interface. This IP address is reported in the VMI's status.interfaces. A guest operating system should be configured to use DHCP to acquire IPv4 addresses.

> To allow the VM to live-migrate or hard restart (both cause the VM to run on a different pod, with a different IP address) and still be reachable, it should be exposed by a Kubernetes service.

## Provision

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: c8kv1-day0
  namespace: default
data:
  iosxe_config.txt: |-
    hostname c8kv1
    ip domain name my-domain.com
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    username admin privilege 15 secret password
    no ip http secure-server
    crypto key generate rsa modulus 2048
    ip ssh version 2
    vrf definition Mgmt-intf
      address-family ipv4
      exit-address-family
    interface GigabitEthernet1
      vrf forwarding Mgmt-intf
      ip address dhcp
      no shutdown
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
---
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: default
  labels:
    app: c8kv1
spec:
  dataVolumeTemplates:
    - apiVersion: cdi.kubevirt.io/v1beta1
      kind: DataVolume
      metadata:
        name: c8kv1
        namespace: default
      spec:
        pvc:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 10G
          volumeMode: Block
        source:
          http:
            url: "http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2"
  running: true
  template:
    metadata:
      labels:
        kubevirt.io/domain: c8kv1
        special: c8kv1
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - name: rootdisk
            disk:
              bus: virtio
          - name: cdromdisk
            cdrom:
              readOnly: True
              bus: sata
          interfaces:
          - masquerade: {}
            name: default
          rng: {}
        resources:
          requests:
            memory: 4Gi
      hostname: c8kv1
      evictionStrategy: LiveMigrate
      networks:
      - name: default
        pod: {}
      volumes:
        - name: rootdisk
          dataVolume:
            name: c8kv1
            namespace: default
        - name: cdromdisk
          configMap:
            name: c8kv1-day0
---
apiVersion: v1
kind: Service
metadata:
  name: c8kv1-ssh
  namespace: default
spec:
  externalTrafficPolicy: Cluster
  ports:
  - port: 22
    protocol: TCP
    targetPort: 22
  selector:
    special: c8kv1
  type: NodePort
```

## Launcher POD

```
$ oc get pod virt-launcher-c8kv1-xxx -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "portmap",
          "interface": "eth0",
          "ips": [
              "10.128.1.24"
          ],
          "mac": "d6:17:85:c9:76:16",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.1.92"
          ]
      }]
```

## Cat8000v

```
c8kv1#show ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.2        YES DHCP   up                    up
```

```
c8kv1#show arp vrf Mgmt-intf
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.0.2.1                0   0200.0000.0000  ARPA   GigabitEthernet1
Internet  10.0.2.2                -   0221.6600.0002  ARPA   GigabitEthernet1
```

```
c8kv1#show ip route vrf Mgmt-intf
S*    0.0.0.0/0 [254/0] via 10.0.2.1
      10.0.0.0/8 is variably subnetted, 3 subnets, 2 masks
C        10.0.2.0/24 is directly connected, GigabitEthernet1
S        10.0.2.1/32 [254/0] via 10.0.2.1, GigabitEthernet1
L        10.0.2.2/32 is directly connected, GigabitEthernet1
```

[[Back]](./README.md) [[KubeVirt Networking]](./example-cat8k-pod-kubevirt.md)