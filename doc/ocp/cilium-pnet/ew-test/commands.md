# Private Network - east-west connectivity test

[[Back]](./README.md) [[Next]](./setup.md) [[Prev]](./vm6.md)

![Overview](../../images/pnet/ew.png)

## Commands cheat sheet

### Namespace

```shell
iserver create k8s ns \
    --name a \
    --kubemacpool \
    --no-confirm

iserver create k8s ns \
    --name b \
    --kubemacpool \
    --no-confirm

iserver create k8s ns \
    --name c \
    --kubemacpool \
    --no-confirm

iserver create k8s ns \
    --name d \
    --kubemacpool \
    --no-confirm
```

### Private Network

```shell
iserver set ocp cilium pnet \
    --mode network \
    --network blue \
    --cidr4 10.10.10.0/24 \
    --nad a \
    --nad b \
    --nad c \
    --no-confirm

iserver set ocp cilium pnet \
    --mode network \
    --network red \
    --cidr4 20.20.20.0/24 \
    --cidr4 20.20.21.0/24 \
    --nad b \
    --nad c \
    --nad d \
    --no-confirm
```

### Application

```shell
iserver create k8s pod \
    --namespace a \
    --name p1 \
    --template netshoot \
    --network pnet,blue,10.10.10.1 \
    --no-confirm

iserver create k8s pod \
    --namespace a \
    --name p2 \
    --template netshoot \
    --network pod \
    --network pnet,blue,10.10.10.2 \
    --no-confirm

iserver create k8s vm \
    --namespace b \
    --name vm3 \
    --template cirros \
    --network pnet,blue,10.10.10.3 \
    --no-confirm

iserver create k8s vm \
    --namespace b \
    --name vm4 \
    --template cirros \
    --network pod \
    --network pnet,blue,10.10.10.4 \
    --network pnet,red,20.20.21.4 \
    --no-confirm

iserver create k8s pod \
    --namespace c \
    --name p5 \
    --template netshoot \
    --network pnet,blue,10.10.10.5 \
    --network pnet,red,20.20.20.5 \
    --no-confirm

iserver create k8s vm \
    --namespace d \
    --name vm6 \
    --template cirros \
    --network pnet,red,20.20.20.6 \
    --network pnet,red,20.20.21.6 \
    --no-confirm
```

### Delete

```shell
iserver delete k8s vm \
    --namespace d \
    --name vm6 \
    --no-confirm

iserver delete k8s pod \
    --namespace c \
    --name p5 \
    --no-confirm

iserver delete k8s vm \
    --namespace b \
    --name vm4 \
    --no-confirm

iserver delete k8s vm \
    --namespace b \
    --name vm3 \
    --no-confirm

iserver delete k8s pod \
    --namespace a \
    --name p2 \
    --no-confirm

iserver delete k8s pod \
    --namespace a \
    --name p1 \
    --no-confirm

iserver delete ocp cilium pnet \
    --mode network \
    --network red \
    --no-confirm

iserver delete ocp cilium pnet \
    --mode network \
    --network blue \
    --no-confirm
```

[[Back]](./README.md) [[Next]](./setup.md) [[Prev]](./vm6.md)