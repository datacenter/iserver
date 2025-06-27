# ACI Fabric - Data model

## Interface Policy Link Level

Property | Type | Default | Values
--- | --- | --- | ---
managed | bool | true | true/false
enabled | bool | true | true/false
shared | bool | false | true/false
name | string | tenant-mo_name-domain | any
auto | string | on | on/off/enforce
media | string | auto | auto/sfp10gtx
debounce | int | 100 | ge 0
delay | int | 0 | ge 0
emi | bool | false | true/false

Notes:
- managed mode 'true' for object that can be created, updated and deleted
- managed mode 'false' for object that is read-only
- shared mode 'false' for object fully mananged by single workflow
- shared mode 'true' for object shared between workflows or non-workflows
- delete workflow expects that managed object can be deleted with no references once configurations are deleted. otherwise error is raised unless object is marked as shared.

![APIC](../images/aci_data_model_link_level.png)