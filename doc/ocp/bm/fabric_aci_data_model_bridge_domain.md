# ACI Fabric - Data model

## Bridge Domain

Used when controller.bgp.enabled:false.

Property | Type | Default | Values
--- | --- | --- | ---
managed | bool | true | true/false
enabled | bool | true | true/false
shared | bool | false | true/false
name | string | mo_name-domain | any
gateway | string | server.interface.gateway | cidr

Notes:
- managed mode 'true' for object that can be created, updated and deleted
- managed mode 'false' for object that is read-only
- shared mode 'false' for object fully mananged by single workflow
- shared mode 'true' for object shared between workflows or non-workflows
- delete workflow expects that managed object can be deleted with no references once configurations are deleted. otherwise error is raised unless object is marked as shared.

![General](../images/aci_data_model_bd_general.png)

![L3](../images/aci_data_model_bd_l3.png)