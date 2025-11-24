# Intersight Hardware Discovery

## Overview

Problem Statement
- server definition (redfish or intersight) is used during installation and then it is gone
- no server's hardware identity on Kubernetes or Linux operational level

Every cluster node CRD with extra annotation for
- management ip
- Intersight server identity

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp imm | get node intersight annotations | [Link](./get.md)
iserver get server --ocp | get servers selected by cluster name | [Link](./server.md)
iserver set ocp imm | set node annotation with intersight server | [Link](./set.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp imm | delete nodes annotation | [Link](./delete.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)