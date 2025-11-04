# OpenShift Installation with Assisted Installer

## Problem statement

OpenShift assisted installer is great deployment option provided by RedHat. At the same time
- trust that network configuration matches the OpenShift cluster configuration (bonding, IP address, VLAN, etc)
- does not support Cilium CNI from UI level
- manual configuration of the servers boot from generated ISO
- UI click-through inputs and interaction i.e. no full automation
- several post installation steps may be required

Note: while UI supports OVNKubernetes CNI only, assisted installer REST API supports other CNIs

[Back](../BareMetalCluster.md)