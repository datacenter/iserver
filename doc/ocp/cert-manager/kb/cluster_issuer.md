# Cert Manager - ClusterIssuer

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/concepts/issuer/)

`ClusterIssuer` is Kubernetes cluster-wide custom resource that represent certificate authorities (CAs) that generate signed certificates. All cert-manager [certificates](./certificate.md) require a referenced issuer that is in a ready condition to attempt to honor the signing request.

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: ca-issuer
spec:
  ca:
    secretName: ca-key-pair
```

The secret referenced by `ClusterIssuer` must be in `cert-manager` namespace

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-key-pair
  namespace: cert-manager
type: kubernetes.io/tls
data:
  tls.crt: <<< certificate >>
  tls.key: <<< rsa private key >>>
```

>[!CAUTION]
>The values in `Secret` must be base64 utf-8 encoded.

Private key example

```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwPax8+yfdiiOgiwv/Vc3YJ/kXsgLYKMfhgyzYFe0NBbI/DtQ
....
-----END RSA PRIVATE KEY-----
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-key-pair
  namespace: cilium
type: kubernetes.io/tls
data:
  tls.crt: <<< certificate >>
  tls.key: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLR...
```

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/concepts/issuer/)