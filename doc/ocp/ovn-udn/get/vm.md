# UDN and Virtual Machine - State

[[Back]](../README.md) [[Prev]](../create/vm_task.md) [[Next]](../overview/vm.md)

```
c8kv3#show ip int brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       66.66.0.9       YES DHCP   up                    up
GigabitEthernet2       66.66.1.4       YES DHCP   up                    up
```

```
c8kv3#show ip route
S*    0.0.0.0/0 [254/0] via 66.66.0.1
      66.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
C        66.66.0.0/24 is directly connected, GigabitEthernet1
L        66.66.0.9/32 is directly connected, GigabitEthernet1
C        66.66.1.0/24 is directly connected, GigabitEthernet2
L        66.66.1.4/32 is directly connected, GigabitEthernet2
      169.254.0.0/32 is subnetted, 1 subnets
S        169.254.1.1 [254/0] via 66.66.0.1, GigabitEthernet1
```

```
# iserver get k8s vmi --namespace island
Cluster: bm1 (type: ocp)

+----+-------------+-------+-----+-----+---------------------+-------+----------------------------------------+-----+---------+
| ID | VM Instance | Node  | CPU | Mem | Disk                | PVC   | Interface                              | Svc | State   |
+----+-------------+-------+-----+-----+---------------------+-------+----------------------------------------+-----+---------+
| 1  | island      | bm1-3 | 1   | 4Gi | rootdisk/vda - 10Gi | c8kv3 | [default] 66.66.0.9 (pod:l2bridge)     | 1   | Running |
|    | c8kv3       |       |     |     | day0                | ---   | [net1] 66.66.1.4 (multus:island/s1-l2) |     |         |
+----+-------------+-------+-----+-----+---------------------+-------+----------------------------------------+-----+---------+
```

```
# oc get pod -n island virt-launcher-c8kv3-jt9ln -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "ovn-kubernetes",
          "interface": "eth0",
          "ips": [
              "10.130.0.134"
          ],
          "mac": "0a:58:0a:82:00:86",
          "dns": {}
      },{
          "name": "ovn-kubernetes",
          "interface": "ovn-udn1",
          "ips": [
              "66.66.0.9"
          ],
          "mac": "0a:58:42:42:00:09",
          "default": true,
          "dns": {}
      },{
          "name": "island/s1-l2",
          "interface": "pod6c270ef2f25",
          "ips": [
              "66.66.1.4"
          ],
          "mac": "02:65:2b:c5:ba:09",
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks: '[{
        "name":"s1-l2",
        "namespace":"island",
        "mac":"02:65:2b:c5:ba:09",
        "interface":"pod6c270ef2f25"
    }]'
```

[[Back]](../README.md) [[Prev]](../create/pod_task.md) [[Next]](../overview/pod.md)