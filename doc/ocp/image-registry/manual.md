# Local Image Registry

[[Back]](../Operations.md)

## Default state (disabled)

On platforms that do not provide shareable object storage, like bare metal, the OpenShift Image Registry Operator bootstraps itself as Removed.

```
$ oc get configs.imageregistry/cluster -o yaml
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  logLevel: Normal
  managementState: Removed
  observedConfig: null
  operatorLogLevel: Normal
  proxy: {}
  replicas: 1
  requests:
    read:
      maxWaitInQueue: 0s
    write:
      maxWaitInQueue: 0s
  rolloutStrategy: RollingUpdate
  storage: {}
  unsupportedConfigOverrides: null
```

No internal image registry pod

```
$ oc get pod -n openshift-image-registry -l docker-registry=default
No resources found in openshift-image-registry namespace.
```

## Configuration

Prerequisites: 
- persistent storage provisioned e.g., LVM, ODF
- storage class defined

Edit image registry configuration
- change spec.managementState to 'Managed'
- change spec.rolloutStrategy to 'Recreate' (for block storage type)
- change spec.storage to 

```
spec:
  storage:
    pvc:
      claim:
```

The expected configuration state after the change

```
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  managementState: Managed
  observedConfig: null
  operatorLogLevel: Normal
  proxy: {}
  replicas: 1
  requests:
    read:
      maxWaitInQueue: 0s
    write:
      maxWaitInQueue: 0s
  rolloutStrategy: Recreate
  storage:
    managementState: Managed
    pvc:
      claim: image-registry-storage
  unsupportedConfigOverrides: null
```

The configuration change did not define the pvc name that defaults to image-registry-storage value. The PVC is automatically created. Things can go wrong if there is no default storage class. In such or other cases, you can predefine the PVC manually e.g.,

```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: image-registry-storage
  namespace: openshift-image-registry
spec:
  storageClassName: lvms-vg1
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
```

## Desired state

```
$ oc get pod -n openshift-image-registry -l docker-registry=default
NAME                              READY   STATUS    RESTARTS   AGE
image-registry-5f99897d4d-vcdwg   1/1     Running   0          134m

$ oc get pvc -n openshift-image-registry
NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
image-registry-storage   Bound    pvc-d3151f47-31e8-4396-bd6b-b684d6868918   30Gi       RWO            lvms-vg1       <unset>                 136m

$ oc get service -n openshift-image-registry
NAME                      TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)     AGE
image-registry            ClusterIP   172.30.235.98   <none>        5000/TCP    135m
image-registry-operator   ClusterIP   None            <none>        60000/TCP   49d
```

## Access

By default local image registry is only accessible within the cluster using ClusterIP service. 

```
$ curl -k https://image-registry.openshift-image-registry.svc:5000
$
```

There is no route defined.

```
$ oc get route -n openshift-image-registry
No resources found in openshift-image-registry namespace.
```

Edit image registry configuration and enable default route

```
$ oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
```

```
$ oc get route -n openshift-image-registry
NAME            HOST/PORT                                                               PATH   SERVICES         PORT    TERMINATION   WILDCARD
default-route   default-route-openshift-image-registry.apps.bm3.ocp.domain.com                 image-registry   <all>   reencrypt     None
```

```
$ curl -k https://default-route-openshift-image-registry.apps.bm3.domain.com
$
```

## Docker login

Get non-kubeadmin user token

```
$ oc login -u kali -p password https://api.bm3.domain.com:6443
Login successful.

You have access to 90 projects, the list has been suppressed. You can list all projects with 'oc projects'

Using project "default".

$ oc whoami
kali

$ oc whoami -t
this-is-the-token
```

Login to registry

```
# docker login -u kali -p this-is-the-token default-route-openshift-image-registry.apps.bm3.domain.com
WARNING! Using --password via the CLI is insecure. Use --password-stdin.
Error response from daemon: Get "https://default-route-openshift-image-registry.apps.bm3.domain.com/v2/": tls: failed to verify certificate: x509: certificate signed by unknown authority
```

Get ingress certificate

```
$ oc get po -n openshift-authentication
NAME                               READY   STATUS    RESTARTS   AGE
oauth-openshift-7f88d54d88-2ftwc   1/1     Running   0          50d
oauth-openshift-7f88d54d88-6frl2   1/1     Running   0          50d
oauth-openshift-7f88d54d88-87dtk   1/1     Running   0          50d

$ oc rsh -n openshift-authentication oauth-openshift-7f88d54d88-2ftwc cat /run/secrets/kubernetes.io/serviceaccount/ca.crt > /tmp/ingress-ca.crt
```

Copy the ingress-ca.crt to the ca-trust directory and trust it

```
# cp /tmp/ingress-ca.crt /etc/pki/ca-trust/source/anchors/
# ls /etc/pki/ca-trust/source/anchors/
ingress-ca.crt
# update-ca-trust
# systemctl restart docker
```

```
# docker login -u kali -p this-is-the-token default-route-openshift-image-registry.apps.bm3.domain.com
Login Succeeded
```

## Image push

```
FROM alpine:latest
ENTRYPOINT ["sh","-c", "echo Hello World!;sleep 3600"]
```

```
# docker build -t default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world:v1 .
[+] Building 23.4s (5/5) FINISHED
...
 => => naming to default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world:v1                     0.0s
```

```
# docker image ls | grep hello
default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world   v1   eb002f26c3f9   2 days ago      8.44MB
```

```
# docker push default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world:v1
The push refers to repository [default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world]
7bb20cf5ef67: Pushed
v1: digest: sha256:2739d7d5f2ecbbb463c987cfb29d41721792cd563d5d5fa1689565f829bba015 size: 527
```

```
$ oc get imagestreams.image.openshift.io -n openshift my-hello-world -o yaml
apiVersion: image.openshift.io/v1
kind: ImageStream
metadata:
  creationTimestamp: "2025-12-20T09:50:06Z"
  generation: 1
  name: my-hello-world
  namespace: openshift
  resourceVersion: "26489791"
  uid: f24e2b97-198f-4b39-ae7d-cb4ff4b04794
spec:
  lookupPolicy:
    local: false
status:
  dockerImageRepository: image-registry.openshift-image-registry.svc:5000/openshift/my-hello-world
  publicDockerImageRepository: default-route-openshift-image-registry.apps.bm3.domain.com/openshift/my-hello-world
  tags:
  - items:
    - created: "2025-12-20T09:50:06Z"
      dockerImageReference: image-registry.openshift-image-registry.svc:5000/openshift/my-hello-world@sha256:2739d7d5f2ecbbb463c987cfb29d41721792cd563d5d5fa1689565f829bba015
      generation: 1
      image: sha256:2739d7d5f2ecbbb463c987cfb29d41721792cd563d5d5fa1689565f829bba015
    tag: v1
```

## Create application

```
apiVersion: v1
kind: Pod
metadata:
  name: hello
spec:
  containers:
  - image: image-registry.openshift-image-registry.svc:5000/openshift/my-hello-world:v1
    name: alpine
```

```
$ oc get pod
NAME       READY   STATUS    RESTARTS   AGE
hello      1/1     Running   0          7s
```

```
$ oc logs hello
Hello World!
```

[[Back]](../Operations.md)