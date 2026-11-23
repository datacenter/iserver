# Container Virtualization Operator - Create instance

[[Back]](../README.md) [[Next]](./operator.md) [[iserver-way]](../create_instance.md)

The OpenShift `HyperConverged` CRD is the primary configuration resource for OpenShift Virtualization, managed by the HyperConverged Cluster Operator (HCO). It acts as a unified entry point to deploy, manage, and configure underlying components like KubeVirt, Containerized Data Importer (CDI), and network addons

## HyperConverged

~~~
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  annotations:
    deployOVS: 'false'
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec: {}
~~~

## Expected outcome

![InstanceCreate](../../images/cnv/instance_create.png)

```
$ oc get all -n openshift-cnv
NAME                                                      READY   STATUS    RESTARTS      AGE
pod/aaq-operator-5f8fcf4c95-6rp5z                         1/1     Running   0             6m51s
pod/bridge-marker-bqfnq                                   1/1     Running   0             94s
pod/bridge-marker-dccjp                                   1/1     Running   0             94s
pod/bridge-marker-kf7tg                                   1/1     Running   0             94s
pod/cdi-apiserver-5845fc877c-sb8fk                        1/1     Running   0             93s
pod/cdi-deployment-696b859c75-85s7n                       1/1     Running   0             93s
pod/cdi-operator-779d4d6b99-6ztdf                         1/1     Running   0             6m52s
pod/cdi-uploadproxy-59fcfd678d-k4n8l                      1/1     Running   0             93s
pod/cluster-network-addons-operator-7c86f7b694-zkhwf      2/2     Running   0             6m52s
pod/hco-operator-85c475c948-hzskl                         1/1     Running   0             6m53s
pod/hco-webhook-5f5989c8b5-r7b9w                          1/1     Running   0             6m52s
pod/hostpath-provisioner-operator-6dff86844f-4rtxr        1/1     Running   0             6m51s
pod/hyperconverged-cluster-cli-download-d6854d5b6-5wtgr   1/1     Running   0             6m52s
pod/kube-cni-linux-bridge-plugin-25zm7                    1/1     Running   0             94s
pod/kube-cni-linux-bridge-plugin-7rcxg                    1/1     Running   0             94s
pod/kube-cni-linux-bridge-plugin-dcw67                    1/1     Running   0             94s
pod/kubemacpool-cert-manager-75d6cfcc55-4mb6c             1/1     Running   0             94s
pod/kubemacpool-mac-controller-manager-7b96945856-86rv6   2/2     Running   1 (77s ago)   94s
pod/kubevirt-apiserver-proxy-5748df7566-6lngj             1/1     Running   0             59s
pod/kubevirt-apiserver-proxy-5748df7566-xkjnk             1/1     Running   0             59s
pod/kubevirt-console-plugin-6b76c7999-tdrdz               1/1     Running   0             59s
pod/kubevirt-console-plugin-6b76c7999-xxkcz               1/1     Running   0             59s
pod/kubevirt-ipam-controller-manager-7bd8bbc84d-chc7f     1/1     Running   0             94s
pod/kubevirt-ipam-controller-manager-7bd8bbc84d-q9gkp     1/1     Running   0             94s
pod/kubevirt-migration-controller-fbc5f4774-mv75k         1/1     Running   0             94s
pod/kubevirt-migration-operator-5b8d596699-kk2jj          1/1     Running   0             6m51s
pod/ssp-operator-548b9677b7-j48hh                         1/1     Running   1 (79s ago)   6m52s
pod/virt-api-5cf5fc557f-6lt8j                             1/1     Running   0             69s
pod/virt-api-5cf5fc557f-ndd5k                             1/1     Running   0             69s
pod/virt-controller-5756456f5c-4gb2h                      1/1     Running   0             44s
pod/virt-controller-5756456f5c-5p499                      1/1     Running   0             44s
pod/virt-exportproxy-744776c879-dt5k7                     1/1     Running   0             44s
pod/virt-exportproxy-744776c879-xt9p6                     1/1     Running   0             44s
pod/virt-handler-6pdwp                                    1/1     Running   0             44s
pod/virt-handler-fr8hn                                    1/1     Running   0             44s
pod/virt-handler-kgcp4                                    1/1     Running   0             44s
pod/virt-operator-b5cb558d-ctrkb                          1/1     Running   0             6m52s
pod/virt-operator-b5cb558d-rq9pr                          1/1     Running   0             6m52s
pod/virt-template-validator-7b788ffbb6-8hjq9              1/1     Running   0             59s
pod/virt-template-validator-7b788ffbb6-rjjp9              1/1     Running   0             59s

NAME                                                         TYPE        CLUSTER-IP        EXTERNAL-IP   PORT(S)    AGE
service/cdi-api                                              ClusterIP   172.244.62.229    <none>        443/TCP    93s
service/cdi-prometheus-metrics                               ClusterIP   172.244.149.120   <none>        8443/TCP   93s
service/cdi-uploadproxy                                      ClusterIP   172.244.72.213    <none>        443/TCP    93s
service/cluster-network-addons-operator-prometheus-metrics   ClusterIP   172.244.254.152   <none>        8443/TCP   94s
service/hco-webhook-service                                  ClusterIP   172.244.252.69    <none>        4343/TCP   6m53s
service/hostpath-provisioner-operator-service                ClusterIP   172.244.169.153   <none>        9443/TCP   6m53s
service/hyperconverged-cluster-cli-download                  ClusterIP   172.244.243.11    <none>        8080/TCP   95s
service/hyperconverged-cluster-webhook-operator-metrics      ClusterIP   172.244.124.179   <none>        8443/TCP   6m50s
service/kubemacpool-service                                  ClusterIP   172.244.185.92    <none>        443/TCP    94s
service/kubevirt-apiserver-proxy-service                     ClusterIP   172.244.169.101   <none>        8080/TCP   95s
service/kubevirt-console-plugin-service                      ClusterIP   172.244.201.98    <none>        9443/TCP   95s
service/kubevirt-hyperconverged-operator-metrics             ClusterIP   172.244.152.249   <none>        8443/TCP   6m51s
service/kubevirt-ipam-controller-webhook-service             ClusterIP   172.244.146.35    <none>        443/TCP    94s
service/kubevirt-migration-prometheus                        ClusterIP   172.244.246.151   <none>        8443/TCP   94s
service/kubevirt-operator-webhook                            ClusterIP   172.244.46.157    <none>        443/TCP    74s
service/kubevirt-prometheus-metrics                          ClusterIP   None              <none>        443/TCP    74s
service/ssp-operator-metrics                                 ClusterIP   172.244.164.252   <none>        443/TCP    6m51s
service/ssp-operator-service                                 ClusterIP   172.244.71.128    <none>        9443/TCP   6m53s
service/template-validator-metrics                           ClusterIP   172.244.126.219   <none>        443/TCP    59s
service/virt-api                                             ClusterIP   172.244.225.48    <none>        443/TCP    74s
service/virt-exportproxy                                     ClusterIP   172.244.234.18    <none>        443/TCP    74s
service/virt-template-validator                              ClusterIP   172.244.77.77     <none>        443/TCP    59s

NAME                                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/bridge-marker                  3         3         3       3            3           kubernetes.io/os=linux   94s
daemonset.apps/kube-cni-linux-bridge-plugin   3         3         3       3            3           kubernetes.io/os=linux   94s
daemonset.apps/virt-handler                   3         3         3       3            3           kubernetes.io/os=linux   44s

NAME                                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/aaq-operator                          1/1     1            1           6m51s
deployment.apps/cdi-apiserver                         1/1     1            1           93s
deployment.apps/cdi-deployment                        1/1     1            1           93s
deployment.apps/cdi-operator                          1/1     1            1           6m52s
deployment.apps/cdi-uploadproxy                       1/1     1            1           93s
deployment.apps/cluster-network-addons-operator       1/1     1            1           6m52s
deployment.apps/hco-operator                          1/1     1            1           6m53s
deployment.apps/hco-webhook                           1/1     1            1           6m52s
deployment.apps/hostpath-provisioner-operator         1/1     1            1           6m51s
deployment.apps/hyperconverged-cluster-cli-download   1/1     1            1           6m52s
deployment.apps/kubemacpool-cert-manager              1/1     1            1           94s
deployment.apps/kubemacpool-mac-controller-manager    1/1     1            1           94s
deployment.apps/kubevirt-apiserver-proxy              2/2     2            2           59s
deployment.apps/kubevirt-console-plugin               2/2     2            2           59s
deployment.apps/kubevirt-ipam-controller-manager      2/2     2            2           94s
deployment.apps/kubevirt-migration-controller         1/1     1            1           94s
deployment.apps/kubevirt-migration-operator           1/1     1            1           6m51s
deployment.apps/ssp-operator                          1/1     1            1           6m52s
deployment.apps/virt-api                              2/2     2            2           69s
deployment.apps/virt-controller                       2/2     2            2           44s
deployment.apps/virt-exportproxy                      2/2     2            2           44s
deployment.apps/virt-operator                         2/2     2            2           6m52s
deployment.apps/virt-template-validator               2/2     2            2           59s

NAME                                                            DESIRED   CURRENT   READY   AGE
replicaset.apps/aaq-operator-5f8fcf4c95                         1         1         1       6m51s
replicaset.apps/cdi-apiserver-5845fc877c                        1         1         1       93s
replicaset.apps/cdi-deployment-696b859c75                       1         1         1       93s
replicaset.apps/cdi-operator-779d4d6b99                         1         1         1       6m52s
replicaset.apps/cdi-uploadproxy-59fcfd678d                      1         1         1       93s
replicaset.apps/cluster-network-addons-operator-7c86f7b694      1         1         1       6m52s
replicaset.apps/hco-operator-85c475c948                         1         1         1       6m53s
replicaset.apps/hco-webhook-5f5989c8b5                          1         1         1       6m52s
replicaset.apps/hostpath-provisioner-operator-6dff86844f        1         1         1       6m51s
replicaset.apps/hyperconverged-cluster-cli-download-d6854d5b6   1         1         1       6m52s
replicaset.apps/kubemacpool-cert-manager-75d6cfcc55             1         1         1       94s
replicaset.apps/kubemacpool-mac-controller-manager-7b96945856   1         1         1       94s
replicaset.apps/kubevirt-apiserver-proxy-5748df7566             2         2         2       59s
replicaset.apps/kubevirt-console-plugin-6b76c7999               2         2         2       59s
replicaset.apps/kubevirt-ipam-controller-manager-7bd8bbc84d     2         2         2       94s
replicaset.apps/kubevirt-migration-controller-fbc5f4774         1         1         1       94s
replicaset.apps/kubevirt-migration-operator-5b8d596699          1         1         1       6m51s
replicaset.apps/ssp-operator-548b9677b7                         1         1         1       6m52s
replicaset.apps/virt-api-5cf5fc557f                             2         2         2       69s
replicaset.apps/virt-controller-5756456f5c                      2         2         2       44s
replicaset.apps/virt-exportproxy-744776c879                     2         2         2       44s
replicaset.apps/virt-operator-b5cb558d                          2         2         2       6m52s
replicaset.apps/virt-template-validator-7b788ffbb6              2         2         2       59s

NAME                                                           HOST/PORT                                                                          PATH   SERVICES                              PORT    TERMINATION          WILDCARD
route.route.openshift.io/cdi-uploadproxy                       cdi-uploadproxy-openshift-cnv.apps.bm1.ocp.domain.com.com                              cdi-uploadproxy                       <all>   reencrypt/Redirect   None
route.route.openshift.io/hyperconverged-cluster-cli-download   hyperconverged-cluster-cli-download-openshift-cnv.apps.bm1.ocp.domain.com.com          hyperconverged-cluster-cli-download   8080    edge/Redirect        None
route.route.openshift.io/virt-exportproxy                      virt-exportproxy-openshift-cnv.apps.bm1.ocp.domain.com.com                             virt-exportproxy                      <all>   reencrypt/Redirect   None

NAME                                                     AGE
hyperconverged.hco.kubevirt.io/kubevirt-hyperconverged   95s

NAME                                                    AGE   PHASE
kubevirt.kubevirt.io/kubevirt-kubevirt-hyperconverged   95s   Deployed
```

[[Back]](../README.md) [[Next]](./operator.md) [[iserver-way]](../create_instance.md)