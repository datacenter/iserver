# NMState Operator - Enable LLDP

[[Back]](./README.md)

## Why

NMState operator provides NodeNetworkState that provides per-node per-interface state information. 

LLDP neighbor information improves operational experience however,
- LLDP is disabled by default on nmstate level and can be enabled by applying specific nncp resource
- LLDP may be enabled on the NIC firmware level
    - depends on the NIC HW type and firmware defaults
    - ethtool priv flags show lldp-on-nic settings
    - ethtool priv flags not shown in nns output
    - priv flags controlling lldp-on-nic not standard and differ per NIC type e.g. Intel 700 vs 800 series

> [!NOTE]
> If lldp is enabled on NIC level, then no lldp information is exposed at nmstate level

## Workflow

On every cluster node
- if --fw flag set, disable lldp on ethernet nic firmware level using ethtool cli
- if --lldp flag set, enable lldp on ethernet nic using nncp crd
- skip interfaces in operational down state if --skip-down flag set as nncp may fail
- wait for nncp crd to complete the configuration task
- delete nncp object unless --keep-ncp flag is used

## Requirements

- NMState operator installed and instance created
- ssh access to cluster nodes

## Expected outcome

![LLDP](../images/nmstate/lldp.png)

## Configurable options

```
# iserver set ocp nmstate --mode lldp
  --cluster TEXT              Cluster Name
  --node TEXT                 Node name
  --fw                        Disable LLDP on NIC fw level
  --keep-nncp                 Keep NNCP
  --skip-down                 Skip interfaces down
  --no-confirm                Confirmation mode
```

## Example

```
iserver set ocp nmstate --cluster bm1 --node bm1-1 --mode lldp --no-confirm

OpenShift Workflow - NMState Operator - Enable LLDP
===================================================

OpenShift Cluster: bm1

Get interface details
---------------------
- node [bm1-1]
        interface: bond0
        interface: bond0.666
        interface: cilium_vxlan
        interface: eno1
                ethtool
                lspci
                priv flags
                state
        interface: eno2
                ethtool
                lspci
                priv flags
                state
        interface: eno5
                ethtool
                lspci
                priv flags
                state
        interface: eno6
                ethtool
                lspci
                priv flags
                state
        interface: eno7
                ethtool
                lspci
                priv flags
                state
        interface: eno8
                ethtool
                lspci
                priv flags
                state
        interface: enp216s0f0
                ethtool
                lspci
                priv flags
                state
        interface: enp216s0f1
                ethtool
                lspci
                priv flags
                state
        interface: ens1f0
                ethtool
                lspci
                priv flags
                state
        interface: ens1f1
                ethtool
                lspci
                priv flags
                state
        interface: lo
Enable lldp on nmstate level [bm1-1]
Interface eno1 - enabling with nncp (enable-lldp-bm1-1-eno1)
Interface eno2 - enabling with nncp (enable-lldp-bm1-1-eno2)
Interface eno5 - enabling with nncp (enable-lldp-bm1-1-eno5)
Interface eno6 - enabling with nncp (enable-lldp-bm1-1-eno6)
Interface eno7 - enabling with nncp (enable-lldp-bm1-1-eno7)
Interface eno8 - enabling with nncp (enable-lldp-bm1-1-eno8)
Interface enp216s0f0 - enabling with nncp (enable-lldp-bm1-1-enp216s0f0)
Interface enp216s0f1 - enabling with nncp (enable-lldp-bm1-1-enp216s0f1)
Interface ens1f0 - enabling with nncp (enable-lldp-bm1-1-ens1f0)
Interface ens1f1 - enabling with nncp (enable-lldp-bm1-1-ens1f1)

+------------------------------+-------------+--------------------------+
| NNCP                         | Status      | Reason                   |
+------------------------------+-------------+--------------------------+
| enable-lldp-bm1-1-eno1       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-eno2       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-eno5       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-eno6       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-eno7       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-eno8       | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-enp216s0f0 | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-enp216s0f1 | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-ens1f0     | Progressing | ConfigurationProgressing |
| enable-lldp-bm1-1-ens1f1     | Progressing | ConfigurationProgressing |
+------------------------------+-------------+--------------------------+
Waiting for [10]: enable-lldp-bm1-1-eno1, enable-lldp-bm1-1-eno2, enable-lldp-bm1-1-eno5, enable-lldp-bm1-1-eno6, enable-lldp-bm1-1-eno7, enable-lldp-bm1-1-eno8, enable-lldp-bm1-1-enp216s0f0, enable-lldp-bm1-1-enp216s0f1, enable-lldp-bm1-1-ens1f0, enable-lldp-bm1-1-ens1f1
...

Waiting for [1]: enable-lldp-bm3-1-ens1f1

+------------------------------+-----------+------------------------+
| NNCP                         | Status    | Reason                 |
+------------------------------+-----------+------------------------+
| enable-lldp-bm3-1-eno1       | Degraded  | FailedToConfigure      |
| enable-lldp-bm3-1-eno2       | Degraded  | FailedToConfigure      |
| enable-lldp-bm3-1-eno5       | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-eno6       | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-eno7       | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-eno8       | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-enp216s0f0 | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-enp216s0f1 | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-ens1f0     | Available | SuccessfullyConfigured |
| enable-lldp-bm3-1-ens1f1     | Available | SuccessfullyConfigured |
+------------------------------+-----------+------------------------+
All policies are deleted (except for progressing if any)...
- enable-lldp-bm3-1-eno1 [Deleted]
- enable-lldp-bm3-1-eno2 [Deleted]
- enable-lldp-bm3-1-eno5 [Deleted]
- enable-lldp-bm3-1-eno6 [Deleted]
- enable-lldp-bm3-1-eno7 [Deleted]
- enable-lldp-bm3-1-eno8 [Deleted]
- enable-lldp-bm3-1-enp216s0f0 [Deleted]
- enable-lldp-bm3-1-enp216s0f1 [Deleted]
- enable-lldp-bm3-1-ens1f0 [Deleted]
- enable-lldp-bm3-1-ens1f1 [Deleted]

Completed tasks
- LLDP enabled on nmstate level
```

[[Back]](./README.md)