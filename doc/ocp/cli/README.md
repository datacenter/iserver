# CLI Tools

Some day2 operations workflows depend on cli tools such as helm, virtctl, cilium or hubble. These cli tools are expected to be available and working on the management node as defined in cluster [connector](../Access.md).

Command | Intent | Details
--- | --- | ---
iserver get ocp connector -v cli | check cli tools | [Link](./get.md)
iserver set ocp cli-cilium | add cilium cli | [Link](./cilium.md)
iserver set ocp cli-helm | add helm cli | [Link](./helm.md)
iserver set ocp cli-hubble | add hubble cli | [Link](./hubble.md)
iserver set ocp cli-virtctl | add virtctl cli | [Link](./virtctl.md)

[[Back]](../Operations.md)