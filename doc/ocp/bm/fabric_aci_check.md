# ACI Fabric - Check workflow

The check workflow is launched with 'iserver create ocp cluster bm --dir [directory-name] --fabric check'. Check workflow also follows successful create workflow.

The goal of check workflow is to verify if the intent as defined in fabric.json has corresponding configurations and state in ACI fabric.

## fabric.json

In case of create workflow followed with check workflow, the input file is the same.

In case of check-only workflow, i.e. when fabric.json is NOT used for create workflow; policy configuration may be skipped. In such case interface state, vlan encap and bonding state is checked.

## Examples

- [complete information](./fabric_aci_check_complete.md)
- [no controller policy](./fabric_aci_check_no_policy.md)
- [IP mismatch](./fabric_aci_check_wrong_ip.md)
- [VLAN mismatch](./fabric_aci_check_wrong_vlan.md)
- [Interface mismatch](./fabric_aci_check_wrong_interface.md)

[Back](./input_data_fabric.md)
