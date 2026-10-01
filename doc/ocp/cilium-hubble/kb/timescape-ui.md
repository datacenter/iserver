# Timescape UI

[[Back]](../README.md)

Timescape UI is running inside hubble timescape integrated as in [here](./configuration-hubble-timescape-no-tls.md). 

Unless you want local port forwarding, you need to expose it for external access

```
$ oc expose service -n cilium hubble-timescape --port 8000
route.route.openshift.io/hubble-timescape exposed
```

```
$ oc get route -n cilium
NAME               HOST/PORT                                                PATH   SERVICES           PORT   TERMINATION   WILDCARD
hubble-timescape   hubble-timescape-cilium.apps.bm1.ocp.domain.com                 hubble-timescape   8000                 None
```

![UI](../../images/hubble/timescape-ui.png)

[[Back]](../README.md)