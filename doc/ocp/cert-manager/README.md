# Certificate Manager

[[Back]](../Operations.md)

![Logo](../images/cert-manager/logo.png)

[cert-manager](https://github.com/cert-manager/cert-manager) adds certificates and certificate issuers as resource types in Kubernetes clusters, and simplifies the process of obtaining, renewing and using those certificates.

## Knowledge Base

CRDs
- [cluster issuer](./kb/cluster_issuer.md)
- [issuer](./kb/issuer.md)
- [certificate request](./kb/request.md)
- [certificate](./kb/certificate.md)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cert-manager | get cert manager state and resources | [Link](./get.md)
iserver set ocp cert-manager --mode feature | install cert manager | [Link](./enable.md)
iserver set ocp cert-manager --mode issuer | add issuer or cluster issuer | [Link](./create_issuer.md)
iserver set ocp cert-manager --mode crt | add certificate | [Link](./create_crt.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cert-manager --mode feature | uninstall cert manager | [Link](./disable.md)
iserver delete ocp cert-manager --mode issuer | delete issuer | [Link](./delete_issuer.md)
iserver delete ocp cert-manager --mode cert | delete certificate | [Link](./delete_crt.md)
iserver delete ocp cert-manager --mode wipe | wipe all crds | [Link](./wipe.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)