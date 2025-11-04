# Networking with NMState Operator using NNCP CRD

NodeNetworkConfigurationPolicy (NNCP) exposes control of network configuration of selected node
- interface (Linux Bridge, VLAN, Bond, Ethernet)
- dns 
- route

Refer to OpenShift [documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/kubernetes_nmstate/k8s-nmstate-updating-node-network-config) for details how to define the configuration.

## HowTo

Command | Intent
--- | ---
iserver create k8s nncp --cluster my-cluster | Create single nncp based on CLI input 
iserver create k8s nncp --file input.json --cluster my-cluster | Create nncp crds based on input file 
iserver create k8s nncp --cluster my-cluster --no-create | Generate nncp body only 

## Interface Ethernet 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Enable interface with no IP address | [Link](./eth_up_none_cli.md) | [Link](./eth_up_none_json.md) | [Link](./eth_up_none_nncp.md) | [Link](./eth_up_none_outcome.md)
Disable interface with no IP address | [Link](./eth_down_none_cli.md) | [Link](./eth_down_none_json.md) | [Link](./eth_down_none_nncp.md) | [Link](./eth_down_none_outcome.md)
Configure IP address | [Link](./eth_ip_cli.md) | [Link](./eth_ip_json.md) | [Link](./eth_ip_nncp.md) | [Link](./eth_ip_outcome.md)

## Interface VLAN 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add VLAN | [Link](./vlan_add_cli.md) | [Link](./vlan_add_json.md) | [Link](./vlan_add_nncp.md) | [Link](./vlan_add_outcome.md)
Delete VLAN | [Link](./vlan_del_cli.md) | [Link](./vlan_del_json.md) | [Link](./vlan_del_nncp.md) | [Link](./vlan_del_outcome.md)

## Interface Bond

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | [Link](./bond_add_cli.md) | [Link](./bond_add_json.md) | [Link](./bond_add_nncp.md) | [Link](./bond_add_outcome.md)
Delete bond | [Link](./bond_del_cli.md) | [Link](./bond_del_json.md) | [Link](./bond_del_nncp.md) | [Link](./bond_del_outcome.md)

## Linux Bridge

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add linux bridge | [Link](./lb_add_cli.md) | [Link](./lb_add_json.md) | [Link](./lb_add_nncp.md) | [Link](./lb_add_outcome.md)
Delete linux bridge | [Link](./lb_del_cli.md) | [Link](./lb_del_json.md) | [Link](./lb_del_nncp.md) | [Link](./lb_del_outcome.md)

## Complex Scenarios

Intent | JSON | NNCP CRD | Outcome
--- | --- | --- | ---
Add linux bridge with bonded vlan upstream | [Link](./uc1_add_json.md) | [Link](./uc1_add_nncp.md) | [Link](./uc1_add_outcome.md)
Routing control | [Link](./uc2_add_json.md) | [Link](./uc2_add_nncp.md) | [Link](./uc2_add_outcome.md)

[[Back]](../Operations.md)