# Cat8000v: management in l3 bridge (multus)

[[Back]](./README.md) [[KubeVirt Networking]](./example-cat8k-bridge-l3-kubevirt.md)

## Overview

Provisioning
- cat8000v instance: 1 vCPU, 4G memory, 10G disk (pvc) from http-sourced image 
- single interface management (GigabitEthernet1) configured with DHCP and connected to bridge
- bridge created with NetworkAttachmentDefinition (NAD) 
- virt-laucher POD IP address not relevant for virtual machine IP forwarding

Packet forwarding
  - kubernetes unmanaged (ships-in-the-night)
  - service, network policy and observability not possible
  - egress: cat8000v sends the traffic via linux bridge hosted on kubernetes node's host level. The bridge can act as L3 hop (this example) but could also be deployed in L2 mode with first hop gateway from virtual machine perspective being outside of kubernetes cluster
  - ingress: L3 or L2 depending on how bridge is configured

Check kubevirt networking details [here](./example-cat8k-bridge-l3-kubevirt.md)

[Bridge mode](https://kubevirt.io/user-guide/network/interfaces_and_networks/#bridge)

> In bridge mode, virtual machines are connected to the network backend through a linux "bridge". The pod network IPv4 address (if exists) is delegated to the virtual machine via DHCPv4. The virtual machine should be configured to use DHCP to acquire IPv4 addresses.

> If a specific MAC address is not configured in the virtual machine interface spec the MAC address from the relevant pod interface is delegated to the virtual machine.

## Provision

> [!NOTE]
> Linux bridge and static ipam configured via NAD. DHCP-based IP address configuration on virtual machine level

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: c8kv1-management
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "bridge",
      "name": "br1",
      "bridge": "br1",
      "isDefaultGateway": true,
      "isMasq": true,
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "15.25.25.25/24",
            "gateway": "15.25.25.254"
          }
        ]
      }
    }
---
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
          - name: nic1
            bridge: {}
          rng: {}
        resources:
          requests:
            memory: 4Gi
      hostname: c8kv1
      evictionStrategy: LiveMigrate
      networks:
      - name: nic1
        multus:
          networkName: default/c8kv1-management
      volumes:
        - name: rootdisk
          dataVolume:
            name: c8kv1
            namespace: default
        - name: cdromdisk
          configMap:
            name: c8kv1-day0
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
              "10.128.0.170"
          ],
          "mac": "ca:f9:12:b3:f5:a9",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.1.92"
          ]
      },{
          "name": "default/test5",
          "interface": "podbaffdcb099b",
          "ips": [
              "15.25.25.25"
          ],
          "mac": "02:21:66:00:00:05",
          "dns": {},
          "gateway": [
              "15.25.25.254"
          ]
      }]
    k8s.v1.cni.cncf.io/networks: '[
      {
        "name":"test5",
        "namespace":"default",
        "mac":"02:21:66:00:00:05",
        "interface":"podbaffdcb099b"
      }
    ]'
```

## Cat8000v

```
c8kv1#show ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       15.25.25.25     YES DHCP   up                    up
```

```
c8kv1#show arp vrf Mgmt-intf
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  15.25.25.25             -   0221.6600.0005  ARPA   GigabitEthernet1
Internet  15.25.25.254            2   7a44.f009.2b16  ARPA   GigabitEthernet1
```

```
c8kv1#show ip route vrf Mgmt-intf
S*    0.0.0.0/0 [254/0] via 15.25.25.254
      15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        15.25.25.0/24 is directly connected, GigabitEthernet1
L        15.25.25.25/32 is directly connected, GigabitEthernet1
```

[[Back]](./README.md) [[KubeVirt Networking]](./example-cat8k-bridge-l3-kubevirt.md)