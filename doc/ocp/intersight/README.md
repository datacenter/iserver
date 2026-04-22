# Cisco Intersight Plugin

[[Back]](../Operations.md)

![Overview](../images/intersight/overview.png)

## Features

- integrates powerful hardware management directly into the OpenShift Web Console
- bridges the gap between your applications and the physical servers they run on
- provides unified view of server inventory incl. health status, real-time metrics, and security advisories
- supports server power control, launch a vKVM session for deep troubleshooting, and initiate firmware upgrades
- [certified openshift operator](https://catalog.redhat.com/en/software/containers/cisco-intersight/cisco-intersight-operator/69d69c555fd95aed2e202980)

## Knowledge Base

HowTo
- [install operator](./kb/operator.md)
- [create cisco intersight instance](./kb/instance.md)
- [enable plugin](./kb/ui_plugin.md)
- [register Intersight account](./kb/register.md)

Single step
- [cli](./create_all.md)
- [task](./create_task.md)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp intersight | get state | [Link](./get.md)
iserver set ocp intersight --mode operator | install operator | [Link](./create_operator.md)
iserver set ocp intersight --mode instance | define cisco intersight instance | [Link](./create_instance.md)
iserver set ocp intersight --mode plugin | enable web console plugin | [Link](./enable_plugin.md)
iserver set ocp intersight --mode register | register intersight account | [Link](./register.md)
iserver set ocp intersight --mode all | from-zero-to-hero | [Link](./create_all.md)
iserver set ocp iotel | in task way | [Link](./create_task.md)
iserver delete ocp intersight --mode operator | uninstall operator | [Link](./delete_operator.md)
iserver delete ocp intersight --mode instance | delete cisco intersight instance | [Link](./delete_instance.md)
iserver delete ocp intersight --mode plugin | disable web console plugin | [Link](./disable_plugin.md)
iserver delete ocp intersight --mode all | delete everything | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)