# SSH Access

[[Back]](../Operations.md)

OpenShift cluster nodes are by default SSH accessible using public key authentication. In case of Assisted Installer based installation, only one ssh public key can be defined and more keys can be defined as day2 task. 

> [!CAUTION]
> Direct modification of `authorized_keys` file is not the right way of controlling ssh access. `core` is **the only** supported username.

## Knowledge Base

- [SSH key management via MachineConfig](./kb/mc.md)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp ssh | get ssh public keys | [Link](./get.md)
iserver set ocp ssh | add ssh public key | [Link](./create_key.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp ssh | delete ssh public key | [Link](./delete_key.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)