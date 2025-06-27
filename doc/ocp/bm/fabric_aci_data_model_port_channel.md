# ACI Fabric - Data model

## Interface Policy Port Channel

Property | Type | Default | Values
--- | --- | --- | ---
managed | bool | true | true/false
enabled | bool | true | true/false
shared | bool | false | true/false
name | string | tenant-mo_name-domain | any
mode | string | on | on/active/passive/pinning/load/explicit
min | int | 1 | ge 1
max | int | 16 | le 16
lb | string | static | static/dynamic
suspend | bool | true | true/false
graceful | bool | true | true/false
fast | bool | true | true/false
symmetric | bool | false | true/false
hash | string | null | null/dip/sip/dport/sport

Notes:
- managed mode 'true' for object that can be created, updated and deleted
- managed mode 'false' for object that is read-only
- shared mode 'false' for object fully mananged by single workflow
- shared mode 'true' for object shared between workflows or non-workflows
- delete workflow expects that managed object can be deleted with no references once configurations are deleted. otherwise error is raised unless object is marked as shared.

![APIC](../images/aci_data_model_port_channel.png)