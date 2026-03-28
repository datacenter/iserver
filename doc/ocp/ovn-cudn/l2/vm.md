# CUDN w/L2 Topology - Step 4: Virtual Machine

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)

## Connection to POD CIDR

- Virtual Machine **may** connect to Kubernetes POD CIDR as primary interface
- if it does, the default route is via this interface

## Connection to primary CUDN w/l2 topology

- Virtual Machine **may** connect to cudn as primary interface
- [namespace](./namespace.md) must be labeled as primary enabled
- [cudn](./cudn.md) must be configured with role:Primary
- the cudn/nad name is not explicitly defined, `l2bridge` binding value is used instead

```
  template:
    spec:
      domain:
        devices:
          interfaces:
          - binding:
              name: l2bridge
            name: default
      networks:
      - name: default
        pod: {}
```

## Connection to secondary CUDN w/l2 topology

- Virtual Machine **may** connect to cudn and that can be localnet
- no namespace label required
- [cudn](./cudn.md) must be configured with role:Secondary
- secondary interface name mapped to Multus network using NAD reference

```
  template:
    spec:
      domain:
        devices:
          interfaces:
          - bridge: {}
            name: net1
      networks:
      - multus:
          networkName: island-v1/vsl2
        name: net1
```

## CIDR example

```
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: c8kv1
  namespace: island-v1
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      name: c8kv1
      namespace: island-v1
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
        app: c8kv1
        kubevirt.io/domain: c8kv1
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
      hostname: c8kv1
      networks:
      - name: default
        pod: {}
      - multus:
          networkName: island-v1/vsl2
        name: net1
      nodeSelector:
        kubernetes.io/hostname: bm1-1
      volumes:
      - dataVolume:
          name: c8kv1
          namespace: island-v1
        name: rootdisk
      - configMap:
          name: c8kv1-day0
          namespace: island-v1
        name: day0
```

## Virtual Machine state example

```
+----+-------------+-------+-----+-----+---------------------+-------+-------------------------------------------+-----------------------+---------+
| ID | VM Instance | Node  | CPU | Mem | Disk                | PVC   | Interface                                 | Svc                   | State   |
+----+-------------+-------+-----+-----+---------------------+-------+-------------------------------------------+-----------------------+---------+
| 1  | island-v1   | bm1-1 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv1 | [default] 66.66.0.21 (pod:l2bridge)       | NodePort:TCP/22:30759 | Running |
|    | c8kv1       |       |     |     | day0                | ---   | [net1] 66.66.1.11 (multus:island-v1/vsl2) |                       |         |
+----+-------------+-------+-----+-----+---------------------+-------+-------------------------------------------+-----------------------+---------+
```

[[Back]](./overview.md) [[Prev](./pod.md)] [[Next]](./task.md)