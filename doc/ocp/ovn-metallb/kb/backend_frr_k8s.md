# MetalLB - Instance bgpBackend frr-k8s

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)

> [!NOTE]
> OCP4.21.4 with OVNKubernetes CNI

```
apiVersion: metallb.io/v1beta1
kind: MetalLB
metadata:
  name: metallb
  namespace: metallb-system
spec:
  bgpBackend: frr-k8s
```

Observations
- [ovn-bgp](../../ovn-bgp/README.md) **not enabled automatically**
- metallb speaker pods **without** frr
- frr deployed in dedicated pods but keep on **crashing** or **pending** depending on ovn-bgp

## Crash

```
$ oc get pod -n metallb-system
NAME             READY   STATUS                       RESTARTS        AGE
frr-k8s-dbtrt    6/7     CrashLoopBackOff             6 (3m40s ago)   9m33s
frr-k8s-f8r9r    6/7     CrashLoopBackOff             6 (3m41s ago)   9m33s
frr-k8s-m7wvp    6/7     CrashLoopBackOff             6 (3m54s ago)   9m33s
```

```
Back-off restarting failed container frr-status in pod frr-k8s-dbtrt_metallb-system(1ac97087-8917-4e60-994e-9d8e670cde59)
```

```
$ oc logs -n metallb-system frr-k8s-dbtrt -c frr-status
{"level":"error","ts":"2026-04-10T07:10:31Z","logger":"setup","msg":"could not fetch the daemon pod","error":"pods \"frr-k8s-dbtrt\" is forbidden: User \"system:serviceaccount:metallb-system:frr-k8s-daemon\" cannot get resource \"pods\" in API group \"\" in the namespace \"metallb-system\"","stacktrace":"main.main\n\t/frr-k8s/frr-tools/status/exporter.go:94\nruntime.main\n\t/usr/lib/golang/src/runtime/proc.go:283"}
```

## ovn-bgp co-existence

If [ovn-bgp](../../ovn-bgp/README.md) is pre-enabled then

```
pod/frr-k8s-gkcl4                                          0/7     Pending                      0          17m
pod/frr-k8s-rnl2d                                          0/7     Pending                      0          17m
pod/frr-k8s-t8bmj                                          0/7     Pending                      0          17m
```

with bgp port conflict since frr works in `openshift-frr-k8s` namespace

[[Back]](./instance.md) [[undefined]](./backend_undefined.md) [[native]](./backend_native.md) [[frr]](./backend_frr.md) [[frr-k8s]](./backend_frr_k8s.md)