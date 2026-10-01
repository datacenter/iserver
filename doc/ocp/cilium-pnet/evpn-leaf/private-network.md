## Private network

[[Back]](./README.md) [[Next]](./kube-app.md)

>[!NOTE]
>The private network subnets can overlap, in this deployment example they do not.

Network name | Subnet | VNI
--- | --- | ---
red | 10.0.100.0/24 | 66100
blue | 10.0.200.0/24 | 66200

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: red
spec:
  vni: 66100
  subnets:
    - name: subnet0
      cidrv4: 10.0.100.0/24
      routes:
        - destination: 0.0.0.0/0
          gateway: EVPN
```

```yaml
apiVersion: isovalent.com/v1alpha1
kind: ClusterwidePrivateNetwork
metadata:
  name: blue
spec:
  vni: 66200
  subnets:
    - name: subnet0
      cidrv4: 10.0.200.0/24
      routes:
        - destination: 0.0.0.0/0
          gateway: EVPN
```

[[Back]](./README.md) [[Next]](./kube-app.md)