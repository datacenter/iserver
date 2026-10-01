# Trident - Create instance

[[Back]](../README.md) [[Next]](./operator.md) [[iserver-way]](../create_instance.md)

## TridentOrchestrator

~~~
apiVersion: trident.netapp.io/v1
kind: TridentOrchestrator
metadata:
  name: trident
spec:
  IPv6: false
  debug: true
  imagePullSecrets: []
  imageRegistry: ''
  namespace: trident
  nodePrep: []
  silenceAutosupport: false
~~~

## Expected outcome

![InstanceCreate](../../images/trident/instance_create.png)

```
$ oc get all -n trident
NAME                                      READY   STATUS    RESTARTS   AGE
pod/trident-controller-7f78d7cb96-6gt8z   6/6     Running   0          48s
pod/trident-node-linux-7cjx4              2/2     Running   0          48s
pod/trident-node-linux-b4d8b              2/2     Running   0          48s
pod/trident-node-linux-rp9dm              2/2     Running   0          48s

NAME                  TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                       AGE
service/trident-csi   ClusterIP   172.244.213.7   <none>        34571/TCP,9220/TCP,8444/TCP   48s

NAME                                DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
daemonset.apps/trident-node-linux   3         3         3       3            3           <none>          48s

NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/trident-controller   1/1     1            1           48s

NAME                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/trident-controller-7f78d7cb96   1         1         1       48s
```

[[Back]](../README.md) [[Next]](./operator.md) [[iserver-way]](../create_instance.md)