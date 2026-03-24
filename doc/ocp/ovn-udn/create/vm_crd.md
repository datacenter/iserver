# UDN and Virtual Machine - CRD

[[Back]](../README.md) [[Prev]](../overview/vm.md) [[Next]](../create/vm_task.md)

## Primary network

> [!NOTE]
> Binding `l2bridge` selects primary user defined network configured in the namespace

```
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
          - name: default
            binding:
              name: l2bridge
      networks:
      - name: default
        pod: {}
```

## Secondary network

> [!NOTE]
> Secondary user defined network triggers network attachment definition and interface is defined in "multus way"

```
spec:
  template:
    spec:
      domain:
        devices:
          interfaces:
          - name: net1
            bridge: {}
      networks:
      - name: net1
        multus:
          networkName: island/s1-l2
```

## Example 

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv3
  namespace: island
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv3
      namespace: island
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
        storageClassName: lvms-vg1
        volumeMode: Block
      source:
        http:
          url: http://my-image-server.domain.com/c8000v-universalk9_8G_serial.17.06.05.qcow2
  runStrategy: Always
  template:
    metadata:
      labels:
        app: c8kv3
        kubevirt.io/domain: c8kv3
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - cdrom:
              bus: sata
              readyOnly: true
            name: day0
          interfaces:
          - binding:
              name: l2bridge
            name: default
          - bridge: {}
            name: net1
          rng: {}
        resources:
          requests:
            memory: 4Gi
      evictionStrategy: LiveMigrate
      hostname: c8kv3
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island/s1-l2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-3
      volumes:
      - dataVolume:
          name: c8kv3
          namespace: island
        name: rootdisk
      - configMap:
          name: c8kv3-day0
          namespace: island
        name: day0
---
apiVersion: v1
data:
  iosxe_config.txt: |-
    hostname c8kv3
    ip domain name domain.com
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    username admin privilege 15 secret password
    no ip http secure-server
    crypto key generate rsa modulus 2048
    ip ssh version 2
    interface GigabitEthernet1
      ip address dhcp
      no shutdown
    interface GigabitEthernet2
      ip address dhcp
      no shutdown
    ip http secure-server
    line con 0
      length 0
    line vty 0 4
      length 0
kind: ConfigMap
metadata:
  name: c8kv3-day0
  namespace: island
```

[[Back]](../README.md) [[Prev]](../overview/vm.md) [[Next]](../create/vm_task.md)