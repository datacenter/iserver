## Hubble Timescape UI

[[Back]](../README.md)

Hubble Timescape UI is a web-based user interface that you can use to visualize and explore the data collected by Hubble Timescape. Hubble Timescape UI is enabled by default starting from Hubble Timescape v1.7.1.

## Cilium configuration

>[!NOTE]
>Example below uses timescape with tls as [here](./configuration-hubble-timescape-tls.md)

```yaml
spec:
  hubble:
    enabled: true
    timescape:
      enabled: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: root-ca
        certValidityDuration: 1
        enabled: true
        method: certmanager
      enabled: true
```

## UI access

Timescape UI is running inside hubble timescape pod

```
$ oc get pod -n cilium
NAME                       READY   STATUS        RESTARTS        AGE
hubble-timescape-0         2/2     Running       0               6h18m
```

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

## TLS UI

If you want to access Hubble Timescape UI with https, one option is exposing via `Ingress`.

```yaml
spec:
  hubble:
    timescape:
      enabled: true
      ui:
        ingress:
          annotations:
            cert-manager.io/cluster-issuer: root-ca
          enabled: true
          hosts:
          - hubble-timescape-cilium.apps.bm1.ocp.domain.com
          tls:
          - hosts:
            - hubble-timescape-cilium.apps.bm1.ocp.domain.com
            secretName: hubble-timescape-ui-ingress-cert
      useStreamAPI: true
    tls:
      auto:
        certManagerIssuerRef:
          group: cert-manager.io
          kind: ClusterIssuer
          name: root-ca
        certValidityDuration: 1
        enabled: true
        method: certmanager
      enabled: true
```

Since in this example [cert manager](../../cert-manager/README.md) is used, ingress annotation will automatically issue a certificate based on the configured host and store it in the specified secret.

```
$ oc get certificates -n cilium hubble-timescape-ui-ingress-cert
NAME                               READY   SECRET                             AGE
hubble-timescape-ui-ingress-cert   True    hubble-timescape-ui-ingress-cert   15m
```

```yaml
spec:
  dnsNames:
  - hubble-timescape-cilium.apps.bm1.ocp.domain.com
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: root-ca
  secretName: hubble-timescape-ui-ingress-cert
  usages:
  - digital signature
  - key encipherment
```

`Ingress` object is created based on CiliumConfiguration

```
$ oc get ingress -A
NAMESPACE   NAME                  CLASS    HOSTS                                               ADDRESS                                   PORTS     AGE
cilium      hubble-timescape-ui   <none>   hubble-timescape-cilium.apps.bm1.ocp.domain.com     router-default.apps.bm1.ocp.domain.com    80, 443   5h27m
```

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    cert-manager.io/cluster-issuer: root-ca
  name: hubble-timescape-ui
  namespace: cilium
  ownerReferences:
  - apiVersion: cilium.io/v1alpha1
    kind: CiliumConfig
    name: ciliumconfig
spec:
  rules:
  - host: hubble-timescape-cilium.apps.bm1.ocp.domain.com
    http:
      paths:
      - backend:
          service:
            name: hubble-timescape
            port:
              name: ui
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - hubble-timescape-cilium.apps.bm1.ocp.domain.com
    secretName: hubble-timescape-ui-ingress-cert
status:
  loadBalancer:
    ingress:
    - hostname: router-default.apps.bm1.ocp.domain.com
```

`Route` object triggered by Ingress

```
$ oc get route -n cilium
NAME                        HOST/PORT                                                PATH   SERVICES           PORT   TERMINATION     WILDCARD
hubble-timescape-ui-65r9m   hubble-timescape-cilium.apps.bm1.ocp.domain.com          /      hubble-timescape   ui     edge/Redirect   None
```

```yaml
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  annotations:
    cert-manager.io/cluster-issuer: root-ca
  name: hubble-timescape-ui-65r9m
  namespace: cilium
  ownerReferences:
  - apiVersion: networking.k8s.io/v1
    controller: true
    kind: Ingress
    name: hubble-timescape-ui
spec:
  host: hubble-timescape-cilium.apps.bm1.ocp.domain.com
  path: /
  port:
    targetPort: ui
  tls:
    certificate: |
      -----BEGIN CERTIFICATE-----
      As in Secret object cilium/hubble-timescape-ui-ingress-cert data:tls.crt
      -----END CERTIFICATE-----
    insecureEdgeTerminationPolicy: Redirect
    key: |
      -----BEGIN RSA PRIVATE KEY-----
      As in Secret object cilium/hubble-timescape-ui-ingress-cert data:tls.key
      -----END RSA PRIVATE KEY-----
    termination: edge
  to:
    kind: Service
    name: hubble-timescape
    weight: 100
  wildcardPolicy: None
status:
  ingress:
  - conditions:
    - lastTransitionTime: "2026-07-15T14:42:51Z"
      status: "True"
      type: Admitted
    host: hubble-timescape-cilium.apps.bm1.ocp.domain.com
    routerCanonicalHostname: router-default.apps.bm1.ocp.domain.com
    routerName: default
    wildcardPolicy: None
```

[[Back]](../README.md)