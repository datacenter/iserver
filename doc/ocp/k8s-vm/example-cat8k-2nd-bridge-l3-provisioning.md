# Cat8000v: extra interface in l3 bridge (multus)

[[Back]](./example-bridge.md) [[KubeVirt Networking]](./example-cat8k-2nd-bridge-l3-kubevirt.md)

## Provision

> [!NOTE]
> Bridge is created on the node where virtual machine is scheduled on

```
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: c8kv1-data
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
            "address": "15.20.20.20/24",
            "gateway": "15.20.20.254"
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
    interface GigabitEthernet2
      ip address 15.20.20.20 255.255.255.0
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
            url: "http://image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2"
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
          - name: nic1
            bridge: {}
          rng: {}
        resources:
          requests:
            memory: 4Gi
      hostname: c8kv1
      evictionStrategy: LiveMigrate
      networks:
      - name: default
        pod: {}
      - name: nic1
        multus:
          networkName: default/c8kv1-data
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

> [!CAUTION]
> Bridge may not be deleted when NAD is deleted 

```
# sudo ip link delete br1 type bridge
```

## Launcher POD

```
$ oc get pod virt-launcher-c8kv1-xxx -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    descheduler.alpha.kubernetes.io/request-evict-only: ""
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "portmap",
          "interface": "eth0",
          "ips": [
              "10.128.3.137"
          ],
          "mac": "46:95:4e:3d:23:9d",
          "default": true,
          "dns": {},
          "gateway": [
              "10.128.3.26"
          ]
      },{
          "name": "default/test",
          "interface": "podbaffdcb099b",
          "ips": [
              "15.20.20.20"
          ],
          "mac": "02:21:66:00:00:01",
          "dns": {},
          "gateway": [
              "15.20.20.254"
          ]
      }]
    k8s.v1.cni.cncf.io/networks: '[{"name":"test","namespace":"default","mac":"02:21:66:00:00:01","interface":"podbaffdcb099b"}]'
```

## Cat8000v

```
c8kv1#show ip int br
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.0.2.2        YES DHCP   up                    up
GigabitEthernet2       15.20.20.20     YES TFTP   up                    up
```

```
c8kv1#show arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  15.20.20.20             -   0221.6600.0001  ARPA   GigabitEthernet2
Internet  15.20.20.254          236   128b.9ed1.a27d  ARPA   GigabitEthernet2
```

```
c8kv1#show ip route vrf Mgmt-intf
S*    0.0.0.0/0 [254/0] via 10.0.2.1
      10.0.0.0/8 is variably subnetted, 3 subnets, 2 masks
C        10.0.2.0/24 is directly connected, GigabitEthernet1
S        10.0.2.1/32 [254/0] via 10.0.2.1, GigabitEthernet1
L        10.0.2.2/32 is directly connected, GigabitEthernet1
```

```
c8kv1#show ip route
Gateway of last resort is not set

      15.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        15.20.20.0/24 is directly connected, GigabitEthernet2
L        15.20.20.20/32 is directly connected, GigabitEthernet2
```

[[Back]](./example-bridge.md) [[KubeVirt Networking]](./example-cat8k-2nd-bridge-l3-kubevirt.md)