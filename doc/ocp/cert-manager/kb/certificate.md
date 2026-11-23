# Cert Manager - Certificate

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/usage/certificate/)

`Certificate` custom resource represents a human readable definition of a certificate request incl. `spec.issuerRef` reference to [issuer](./issuer.md). cert-manager uses this input to generate a private key and CertificateRequest resource in order to obtain a signed certificate from an `Issuer`. The signed certificate and private key are then stored in the specified `spec.secretName` resource. cert-manager will ensure that the certificate is auto-renewed before it expires and re-issued if requested.

## Example

Requirement: `ClusterIssuer` is defined and ready as explained [here](./cluster_issuer.md)

```
$ oc get clusterissuers.cert-manager.io 
NAME             READY   AGE
cilium-root-ca   True    21h
```

```
$ oc get secret -n cert-manager cilium-root-ca -o yaml
apiVersion: v1
data:
  tls.crt: <<< certificate >>> 
  tls.key: <<< rsa private key >>> 
kind: Secret
metadata:
  name: cilium-root-ca
  namespace: cert-manager
type: kubernetes.io/tls
```

Create `Certificate` object definition with issuerRef pointing to `ClusterIssuer` object

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: test-cert
  namespace: default
spec:
  commonName: abc
  isCA: false
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: cilium-root-ca
  secretName: test-cert
```

Triggered workflow
- rsa private key generated that will end up in `Secret` and will be used to sign CSR
- `CertificateRequest` object created that includes CSR
- `Secret` object created with signing ca, generated certificate and private key
- updated status of `Certificate` based on generated certificate

### CertificateRequest

`CertificateRequest` object created automatically and associated/owned by `Certificate` object. 

spec.request contains Certificate Signing Request (CSR) which is a structured block of encoded text sent to a Certificate Authority (CA) to apply for a digital SSL/TLS certificate. It contains your organization's identifying details (cn), the public key to be certified, and is digitally signed by your private key.

```
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=abc
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:cd:93:ba:f2:0e:75:37:c5:94:5e:8e:29:d0:00:
                    a1:fd:07:d8:69:a2:1b:f9:23:b9:11:84:ce:fb:79:
                    e1:0b:a3:01:c9:b3:24:8d:58:7c:e7:89:30:a6:df:
                    5b:64:a7:89:05:86:f9:44:71:0c:21:99:4a:9d:c7:
                    b3:e5:d2:9c:f3:6c:d3:59:10:39:ee:ad:8e:46:85:
                    d8:7b:54:3f:44:3c:d4:c6:24:94:18:5a:61:6c:d1:
                    5d:07:f6:1c:5d:9a:1f:9d:c1:b9:be:ad:a1:ea:3f:
                    4c:45:33:e4:0f:50:6b:f6:f9:1b:1b:7c:64:f3:db:
                    5d:96:77:76:90:08:26:d0:5d:c7:00:80:a9:80:59:
                    65:b3:1b:6a:f6:80:38:4a:aa:bb:73:e7:d1:b1:1b:
                    35:f2:70:23:2b:4f:c3:54:f8:9f:a9:44:a4:65:f2:
                    d3:38:7b:e8:7f:53:16:de:bf:a4:0a:51:59:46:e3:
                    3a:b4:e2:83:bc:4d:62:79:ae:c6:96:4b:ba:3f:1b:
                    c5:38:5f:ef:4f:b0:b7:b5:9f:96:be:1d:26:ac:a7:
                    19:23:f9:9a:f1:36:46:e2:c5:8e:64:d6:5e:33:41:
                    f7:4c:1f:94:04:a1:c2:2f:dc:7d:eb:b5:43:1e:97:
                    86:51:ef:7a:5f:7c:9f:f2:6d:31:f4:90:d2:b4:7d:
                    1d:fd
                Exponent: 65537 (0x10001)
        Attributes:
            Requested Extensions:
                X509v3 Key Usage: critical
                    Digital Signature, Key Encipherment
    Signature Algorithm: sha256WithRSAEncryption
    Signature Value:
        be:99:e3:dd:2c:3f:24:d9:a6:0e:18:b5:cd:e5:30:3b:6d:8f:
        ff:08:6f:b0:02:7a:3a:32:d9:0b:8f:35:4d:4a:2a:ff:f9:a3:
        06:39:02:8f:37:1a:4f:94:27:7c:6f:3c:9f:51:d3:74:ea:e6:
        f0:26:ca:41:c3:ef:1b:9a:52:ae:8a:35:63:10:2f:0d:ff:08:
        b3:3f:f9:b7:a2:47:a0:fd:65:fe:c4:14:64:27:e2:cc:c6:6d:
        5e:72:91:3e:a4:35:1f:a7:b3:70:3a:4b:d4:8c:91:f0:74:05:
        44:01:ff:c4:ff:15:7b:89:95:82:b5:8a:de:b7:98:f6:ee:6c:
        cb:46:fa:0f:c3:d6:fd:d7:17:37:d0:89:84:5f:33:a7:75:5f:
        2a:50:6d:fc:15:ae:b0:35:90:3d:a9:e5:82:81:4d:ce:1b:5c:
        56:66:8d:f7:47:8d:9e:69:10:71:7d:9b:da:13:fe:df:b6:86:
        c7:25:76:ac:1e:a6:71:4a:f2:06:90:4e:21:6e:8f:99:99:a5:
        b9:e8:ed:78:5e:65:e9:02:55:77:55:c5:90:5a:74:c8:98:5c:
        31:44:d1:a4:1d:5c:ca:40:32:24:97:c4:52:a0:7f:9e:f8:e7:
        93:f9:39:61:fa:b9:e5:77:2b:ef:b8:00:77:0f:dc:a6:b1:3f:
        06:bd:cc:a8
```

Status contains both sigining CA and generated certificate

```
$ oc get certificaterequests.cert-manager.io 
NAME          APPROVED   DENIED   READY   ISSUER           REQUESTER                                         AGE
test-cert-1   True                True    cilium-root-ca   system:serviceaccount:cert-manager:cert-manager   5s
```

```
$ oc get certificaterequests.cert-manager.io -n default test-cert-1 -o yaml
apiVersion: cert-manager.io/v1
kind: CertificateRequest
metadata:
  annotations:
    cert-manager.io/certificate-name: test-cert
    cert-manager.io/certificate-revision: "1"
    cert-manager.io/private-key-secret-name: test-cert-8q57z
  name: test-cert-1
  namespace: default
  ownerReferences:
  - apiVersion: cert-manager.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: Certificate
    name: test-cert
spec:
  groups:
  - system:serviceaccounts
  - system:serviceaccounts:cert-manager
  - system:authenticated
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: cilium-root-ca
  request: <<< csr >>>
  username: system:serviceaccount:cert-manager:cert-manager
status:
  ca: <<< signing ca >>> 
  certificate: <<< generated cert >>>
  conditions:
  - lastTransitionTime: "2026-06-26T06:30:06Z"
    message: Certificate request has been approved by cert-manager.io
    reason: cert-manager.io
    status: "True"
    type: Approved
  - lastTransitionTime: "2026-06-26T06:30:06Z"
    message: Certificate fetched from issuer successfully
    reason: Issued
    status: "True"
    type: Ready
```

### Certificate

The status of `Certificate` object shows the readiness condition and validity/renewal timestamps

```
$ oc get certificate test-cert -o yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  creationTimestamp: "2026-06-26T06:30:06Z"
  generation: 1
  name: test-cert
  namespace: default
  resourceVersion: "135936084"
  uid: 4ad040a2-4261-4d6a-8b64-fa5b0049871f
spec:
  commonName: abc
  isCA: false
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: cilium-root-ca
  secretName: test-cert
status:
  conditions:
  - lastTransitionTime: "2026-06-26T06:30:07Z"
    message: Certificate is up to date and has not expired
    observedGeneration: 1
    reason: Ready
    status: "True"
    type: Ready
  notAfter: "2026-09-24T06:30:06Z"
  notBefore: "2026-06-26T06:30:06Z"
  renewalTime: "2026-08-25T06:30:06Z"
  revision: 1
```

### Secret

The signing CA, certificate, and private key are stored in `Secret` object created by cert-manager

```
$ oc get secret
NAME        TYPE                DATA   AGE
test-cert   kubernetes.io/tls   3      6m59s
```

```
$ oc get secret test-cert -o yaml
apiVersion: v1
data:
  ca.crt: <<< signing ca >>> 
  tls.crt: <<< generated cert >>> 
  tls.key: <<< rsa private key >>>
kind: Secret
metadata:
  annotations:
    cert-manager.io/alt-names: ""
    cert-manager.io/certificate-name: test-cert
    cert-manager.io/common-name: abc
    cert-manager.io/ip-sans: ""
    cert-manager.io/issuer-group: cert-manager.io
    cert-manager.io/issuer-kind: ClusterIssuer
    cert-manager.io/issuer-name: cilium-root-ca
    cert-manager.io/uri-sans: ""
  creationTimestamp: "2026-06-26T06:30:06Z"
  labels:
    controller.cert-manager.io/fao: "true"
  name: test-cert
  namespace: default
type: kubernetes.io/tls
```

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/usage/certificate/)