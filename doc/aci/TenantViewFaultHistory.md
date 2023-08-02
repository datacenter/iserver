# Tenant

## Fault history view

```
# iserver get aci tenant --apic apic21 --name k8s --when any --view hfault

Apic: apic21 (mode:online, cache:off)

Tenant - Fault Records last 10y [#1000]
---------------------------------------

+--------+-----+-------+----------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| Tenant | Sev | Code  | Cause                | Created Time                  | Lifecycle        | Description                                                                      |
+--------+-----+-------+----------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| k8s    | Maj | F3083 | config-error         | 2023-07-26T08:03:42.002+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-26T08:03:40.663+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.761+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.760+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.759+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.757+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.755+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.754+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.752+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.752+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.750+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.750+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.749+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.748+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.747+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.746+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.745+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.744+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.743+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.741+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.739+02:00 |                  | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.728+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.727+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.727+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.726+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.725+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.724+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.723+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.722+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.721+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.720+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.720+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.718+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.717+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.716+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.715+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.714+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.712+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.710+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T16:47:24.708+02:00 |                  | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.274+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.273+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.272+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.271+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.270+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.268+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.268+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.267+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.266+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.266+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.265+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.264+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.263+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.261+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.261+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.260+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.259+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.258+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:40:09.257+02:00 | raised           | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.910+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.909+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.908+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.908+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.907+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.905+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.904+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.903+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.903+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.902+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.901+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.901+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.900+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.899+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.898+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.897+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.896+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.895+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:39:40.894+02:00 | raised           | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.918+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.917+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.916+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.915+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.914+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.913+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.912+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.911+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.910+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.909+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.907+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.907+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.906+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.905+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.904+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.903+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.902+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.901+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.900+02:00 | soaking          | Fault delegate: Configuration failed for node 2208 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.893+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.891+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.891+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.890+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.888+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.887+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.886+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.885+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.884+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.882+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.881+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.880+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.879+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.878+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.877+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.876+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.875+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.873+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-07-24T14:37:39.871+02:00 | soaking          | Fault delegate: Configuration failed for node 2207 due to Invalid Path           | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-10   | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:52:08.186+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:52:07.918+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:45:48.149+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E8:E7;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:45:48.063+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E8:E7;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:05:07.755+02:00 |                  | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T20:05:07.144+02:00 | soaking          | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:58:05.480+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:58:05.398+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:57:05.483+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:45:92;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:57:05.396+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:45:92;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:53:05.454+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:53:05.362+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:25.450+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:25.437+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:24.716+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:24.710+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:05.433+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:52:05.349+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:51:25.410+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:51:24.670+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:51:05.440+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:64:9A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:51:05.352+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:64:9A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:08:05.030+02:00 |                  | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:11:50;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-07-12T15:08:04.268+02:00 | soaking          | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:11:50;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.628+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.628+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.624+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.622+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.621+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:46:36.619+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:45:50.023+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:45:50.022+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:29.873+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:43:29.872+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:19:19.795+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:19:19.793+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:30.937+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:30.936+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:11.258+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:17:11.257+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:15:16.851+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T09:15:11.880+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:44.755+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:44.753+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:43.976+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:43.975+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:43.974+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:42.947+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:42.945+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:42.920+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-18T01:03:42.917+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.783+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.778+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2202        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.712+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.710+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.708+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2208 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:43.693+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2208 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:42.943+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-A_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:42.941+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/out-vl3_k8s node 2201        | 
|        |     |       |                      |                               |                  | UCSB1-FI-B_PolGrp due to Invalid Path Configuration, debug message:              | 
|        |     |       |                      |                               |                  | invalid-path: Interface does not exist;                                          | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.965+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.964+02:00 | raised           | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.963+02:00 | raised           | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.961+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 k8s_ocp_bm_5_PolGrp due to   | 
|        |     |       |                      |                               |                  | Invalid Path Configuration,Invalid VLAN Configuration, debug message:            | 
|        |     |       |                      |                               |                  | invalid-vlan: vlan-666 :Either the EpG is not associated with a domain or the    | 
|        |     |       |                      |                               |                  | domain does not have this vlan assigned to it;invalid-path: Either the           | 
|        |     |       |                      |                               |                  | EpG/L3Out is not associated with a domain or the domain does not have this       | 
|        |     |       |                      |                               |                  | interface assigned to it;                                                        | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.957+02:00 | soaking          | Fault delegate: Configuration failed for                                         | 
|        |     |       |                      |                               |                  | uni/tn-k8s/l2out-Test/instP-L2Out-ext-epg node 2207 eth1/30 due to Invalid Path  | 
|        |     |       |                      |                               |                  | Configuration,Invalid VLAN Configuration, debug message: invalid-vlan: vlan-666  | 
|        |     |       |                      |                               |                  | :Either the EpG is not associated with a domain or the domain does not have      | 
|        |     |       |                      |                               |                  | this vlan assigned to it;invalid-path: Either the EpG/L3Out is not associated    | 
|        |     |       |                      |                               |                  | with a domain or the domain does not have this interface assigned to it;         | 
| k8s    | Min | F0467 | configuration-failed | 2023-06-12T11:32:41.953+02:00 | soaking          | Fault delegate: Configuration failed for uni/tn-k8s/ap-k8s_ANP/epg-MGMT node     | 
|        |     |       |                      |                               |                  | 2207 k8s_ocp_bm_1_PolGrp due to Invalid Path Configuration,Invalid VLAN          | 
|        |     |       |                      |                               |                  | Configuration, debug message: invalid-vlan: vlan-800 :STP Segment Id not         | 
|        |     |       |                      |                               |                  | present for Encap. Either the EpG is not associated with a domain or the domain  | 
|        |     |       |                      |                               |                  | does not have this vlan assigned to it;invalid-path: vlan-800 :There is no       | 
|        |     |       |                      |                               |                  | domain, associated with both EPG and Port, that has required VLAN;               | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T14:16:10.491+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T13:50:52.650+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:49:34.853+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:49:30.154+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:49:09.836+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:48:55.882+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:48:49.835+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:48:31.869+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:47:49.823+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:47:31.823+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:46:49.854+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:46:31.846+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:49.878+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:34.813+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:29.841+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:14.898+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:14.873+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:45:10.767+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:54.968+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:54.958+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:54.926+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T13:44:52.504+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:49.945+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:49.940+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:49.826+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:49.821+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:31.742+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:14.802+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:44:10.730+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:49.801+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:34.812+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:34.796+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:29.938+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:29.933+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:29.779+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:14.872+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:14.861+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:14.847+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:14.841+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:10.720+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:43:10.705+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:54.897+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:54.875+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:52.723+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:52.708+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:34.746+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:42:30.080+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:41:54.794+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:41:52.661+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:41:34.759+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:41:31.652+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T13:41:22.434+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:40:54.790+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:40:52.627+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:40:34.729+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:40:31.605+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:39:54.808+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:39:52.596+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:39:34.787+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:39:31.569+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:38:54.820+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:38:49.804+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:38:37.542+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:38:31.565+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:37:54.774+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:37:49.756+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:37:37.519+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:37:30.025+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:36:54.781+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:36:49.761+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:36:37.490+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:36:10.461+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:54.763+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:49.697+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:37.428+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:37.422+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:14.682+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:34:10.412+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:33:09.672+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:54.692+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:54.676+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:52.360+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:34.720+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:34.688+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:31.406+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:32:31.380+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:30:34.623+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:30:31.317+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:30:14.643+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:30:10.293+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:54.670+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:52.283+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:34.689+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:34.657+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:31.307+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:31.292+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:14.637+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:29:10.252+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:28:34.634+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:28:31.242+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T13:19:21.786+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:17:14.541+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:16:54.885+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T13:15:51.653+02:00 | retaining        | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:54.444+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:51.764+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:34.440+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:29.495+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:29.479+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:14.446+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:09.774+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:13:09.759+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:12:54.433+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:12:51.731+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:12:34.442+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:12:30.722+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:08:54.426+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:08:51.612+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:08:34.395+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:08:30.616+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:07:34.455+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:07:29.583+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:01:14.299+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:01:09.375+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:54.285+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:49.414+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:49.408+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:34.284+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:34.279+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:34.268+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:29.349+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:29.338+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:29.332+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T13:00:15.333+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:59:34.307+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:59:15.318+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:58:34.229+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:58:30.335+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:58:14.221+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:58:09.283+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:57:34.227+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:57:15.251+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:56:34.207+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:56:15.221+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:55:34.282+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:55:15.189+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:54:51.067+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:54:34.248+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:54:15.158+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:53:34.225+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:53:15.126+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:49.263+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:34.093+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:34.063+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:30.138+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:30.123+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:14.090+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:12.129+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:52:12.114+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:51:54.044+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:51:51.083+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:50:50.925+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:49:50.897+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:48:49.281+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:48:29.968+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:47:34.054+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:47:14.927+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:45:34.002+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:45:29.910+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:45:13.991+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:45:11.862+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:44:50.780+02:00 | retaining        | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:29.178+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:29.172+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:13.960+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:13.955+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:13.932+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:42:11.779+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:41:33.918+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:41:09.145+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:41:09.139+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:40:56.737+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:37:20.562+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:35:13.927+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:34:56.555+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:30:49.031+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:30:35.422+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:29:48.998+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:29:35.400+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:29:20.650+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:27:13.854+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:27:08.967+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:26:53.812+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:26:53.807+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:26:33.777+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:26:29.331+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:23:20.169+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:22:33.797+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:22:29.193+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:21:33.755+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:21:29.159+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:21:13.827+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:21:13.796+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:21:11.149+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:20:56.131+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T12:11:49.815+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:06:13.572+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:06:10.707+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:53.569+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:53.557+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:49.693+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:49.688+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:13.599+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:05:10.660+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:04:53.592+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:04:53.571+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:04:49.674+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T12:04:28.636+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:56:33.457+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:56:31.429+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:55:53.442+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:55:49.394+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:55:13.454+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:55:10.372+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:54:53.472+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:54:53.460+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:54:49.392+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:54:49.376+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:51:28.467+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:51:16.232+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:50:53.334+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:50:49.218+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:49:13.363+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:49:10.169+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:48:19.162+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:46:13.300+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:45:55.068+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:40:13.247+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:40:09.898+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:53.302+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:53.279+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:48.911+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:48.906+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:28.444+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:39:15.878+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:38:53.220+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:38:48.851+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:30:28.304+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:30:15.606+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:25:18.464+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:23:08.263+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:22:48.368+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:22:32.951+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:22:30.426+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:20:18.291+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:18:08.187+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:17:52.973+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:17:48.245+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:17:48.221+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:17:18.214+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:52.964+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:52.942+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:48.161+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:30.139+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:12.963+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:08.250+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:08.226+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:08.221+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:15:08.201+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:53.013+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:53.009+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:53.004+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:52.984+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:48.175+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:48.150+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:14:15.115+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:13:08.176+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:52.928+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:52.896+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:48.126+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:48.121+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:48.107+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:12:48.056+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:32.880+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:12:30.091+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:11:48.026+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:52.868+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:50.985+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:32.920+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:32.915+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:32.895+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:29.978+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:29.971+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:09:14.954+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:52.819+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:50.954+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:32.938+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:32.913+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:32.891+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:28.089+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:28.084+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:08:14.921+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:07:32.798+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:07:29.912+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:06:47.864+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:05:52.870+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:05:50.859+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:05:32.790+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:05:29.845+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T11:05:17.847+02:00 | retaining        | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:05:07.997+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:53.849+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:32.859+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:32.843+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:28.073+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:14.797+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:08.804+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:04:08.799+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:03:52.838+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:03:50.781+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:03:32.761+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:03:29.803+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:52.839+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:52.823+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:50.753+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:32.777+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:27.995+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:02:14.747+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:01:52.750+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:01:50.722+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:01:12.786+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:01:08.717+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:00:52.774+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:00:48.023+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:00:48.016+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:00:32.721+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T11:00:07.925+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:59:53.675+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:58:32.705+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:58:29.636+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:52.803+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:52.792+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:50.619+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:50.613+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:32.706+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:27.930+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:27.924+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:57:14.586+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:55:52.763+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:55:50.543+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:55:32.690+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:55:29.540+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:54:17.539+02:00 | retaining        | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:52:07.861+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:52.632+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:52.627+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:52.525+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:32.623+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:27.905+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:27.891+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:27.886+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:27.872+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:51:14.410+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:49:52.604+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:49:35.359+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:48:52.554+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:48:35.304+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:47:52.591+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:47:35.272+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:46:52.522+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:46:35.261+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:42:17.205+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:39:47.684+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:39:29.049+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:39:17.112+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:37:12.433+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:37:07.967+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:36:47.612+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:36:32.387+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:36:28.988+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:36:28.983+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:31:16.891+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:47.467+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:32.356+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:27.567+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:27.539+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:12.398+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:12.376+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:07.722+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:28:07.717+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:26:47.451+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:26:27.450+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:24:47.412+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:24:28.622+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:22:47.402+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:22:28.551+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:20:16.537+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:17:47.406+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:17:28.379+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:16:47.359+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:16:32.217+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:16:28.373+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:16:28.357+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:12:46.308+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:12:46.305+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:11:52.181+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:11:49.203+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T10:11:46.270+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:10:27.331+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:10:27.316+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:10:07.280+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:10:07.204+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:09:32.150+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:09:32.126+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:09:13.163+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:09:13.148+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:08:47.235+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:08:32.108+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:08:32.081+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:08:13.102+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:07:52.119+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:07:32.047+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:07:28.089+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:07:13.054+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:06:52.107+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:06:13.037+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:05:52.033+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:05:13.008+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:04:52.112+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:04:12.981+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:03:52.109+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:03:12.941+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:02:52.091+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:02:12.924+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:01:32.052+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:01:12.882+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:00:52.039+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T10:00:12.850+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:59:51.962+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:59:12.820+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:52.004+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:51.994+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:48.797+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:11.976+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:11.955+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:57:09.776+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:56:51.944+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:56:12.743+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:51:51.900+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:51:48.592+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:51:11.904+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:51:09.584+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:47:51.876+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:47:48.465+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:47:11.857+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:47:09.448+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:51.822+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:46.918+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:46.821+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:33.439+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:11.864+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:46:09.435+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:45:51.890+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:45:48.416+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:45:11.840+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:45:09.383+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:43:45.415+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:41:31.799+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:41:12.277+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:40:51.778+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:40:48.255+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:40:11.780+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:40:09.254+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:39:51.822+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:39:48.225+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:39:11.759+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:39:09.209+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:38:15.279+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:36:15.240+02:00 | retaining        | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:46.725+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:31.708+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:27.136+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:27.131+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:35:15.189+02:00 | retaining        | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:11.724+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:35:09.096+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:34:51.700+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:34:48.075+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:34:11.752+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:34:11.736+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:34:09.063+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:54.037+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:31.747+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:31.735+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:27.082+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:27.066+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:11.739+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:11.728+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:09.033+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:33:09.027+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:46.687+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:31.728+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:26.819+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:26.814+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:11.692+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:32:09.005+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:31:51.740+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:31:47.987+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:31:45.063+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:31:11.669+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:31:08.977+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:51.743+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:47.961+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:11.719+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:11.708+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:08.977+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:30:08.951+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:31.629+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:26.739+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:26.712+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:11.629+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:06.766+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:06.760+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:29:06.656+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:28:51.671+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:28:51.656+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:28:47.893+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:28:11.666+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:28:08.873+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:27:51.685+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:27:47.863+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:27:11.610+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:27:08.842+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:26:51.595+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:26:47.844+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:26:11.599+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:26:08.823+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:25:51.573+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:25:47.804+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:25:44.889+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:25:11.586+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:25:08.799+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:24:46.603+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:24:32.778+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:24:11.573+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:24:08.753+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:31.570+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:26.622+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:26.596+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:11.572+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:06.618+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:06.591+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:23:06.580+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:53.740+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:46.552+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:32.712+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:26.547+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:22:14.814+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:11.587+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:11.581+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:22:08.688+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:21:46.564+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:21:32.669+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:21:11.555+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:21:08.658+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:20:46.551+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:20:32.647+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:20:11.526+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:20:08.627+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:46.499+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:31.630+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:31.607+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:26.674+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:26.655+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:26.645+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:11.520+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:19:08.598+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:18:51.518+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:18:47.584+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:18:11.507+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:18:08.566+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:17:46.481+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:17:32.561+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:17:11.508+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:17:08.552+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:16:46.481+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:16:32.518+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:16:14.648+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:16:11.495+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:16:08.527+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:15:46.458+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:15:32.492+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:15:11.494+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:15:08.479+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:14:31.469+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:14:26.480+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:14:11.533+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:14:08.459+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:13:46.529+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:13:32.448+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:13:11.489+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:13:08.424+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:12:46.474+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:12:32.416+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:12:11.460+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:12:08.397+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:11:46.429+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:11:32.386+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:11:11.453+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:11:08.362+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:46.467+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:32.354+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:11.471+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:11.459+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:08.390+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:10:08.373+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:09:46.410+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:09:32.319+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:09:11.444+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:09:08.308+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:08:46.414+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:08:32.292+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:08:11.276+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:08:08.264+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:46.388+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:31.371+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:31.246+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:11.274+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:06.448+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:06.425+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:07:06.419+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:53.253+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:46.409+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:32.228+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:26.394+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:11.328+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:11.313+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:06:08.214+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:05:46.410+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:05:32.191+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:05:11.235+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:05:08.177+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:04:51.268+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:04:47.167+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T09:04:14.286+02:00 | retaining        | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:04:11.222+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:04:08.149+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:03:51.193+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:03:47.138+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:03:11.225+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:03:08.119+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:02:46.278+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:02:32.114+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:02:11.214+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:02:08.091+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:46.288+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:46.283+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:31.247+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:31.242+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:31.230+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:31.219+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:29.095+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:29.077+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:11.209+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:01:08.074+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:00:26.312+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T09:00:08.046+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:59:46.285+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:59:32.015+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:59:11.181+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:59:08.023+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:58:46.273+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:58:31.985+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:58:11.179+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:58:07.983+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:57:26.284+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:57:07.951+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:56:26.275+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:56:07.907+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:55:26.224+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:55:07.881+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:54:26.212+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:54:07.851+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:53:26.189+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:53:07.820+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:52:26.193+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:52:07.791+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:51:26.143+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:51:07.773+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:50:26.145+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:50:07.745+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:49:26.158+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:49:07.715+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:48:26.017+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:48:07.685+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:47:26.012+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:47:07.654+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:46:25.977+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:46:07.612+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:45:25.975+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:45:07.591+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:44:25.927+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:44:07.552+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:43:25.917+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:43:07.559+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:42:25.912+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:42:07.491+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:41:25.933+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:41:13.476+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:41:05.918+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:40:52.448+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:40:25.878+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:40:07.441+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:39:25.921+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:39:07.411+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:38:25.903+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:38:07.381+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:37:25.838+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:37:10.968+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:37:07.349+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:37:07.344+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:36:25.886+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:36:07.303+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T08:33:13.381+02:00 | retaining        | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T08:32:13.348+02:00 | retaining        | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:31:10.786+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:31:10.781+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:31:07.159+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:30:50.790+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:30:50.775+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:30:46.151+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:F2:87;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:30:30.704+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:30:10.721+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:29:52.158+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3E:5F;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:29:52.153+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:29:30.704+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:28:52.092+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:28:30.705+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:50.795+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:50.709+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:46.065+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:30.684+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:10.693+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:27:07.053+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:4F:F6;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:26:52.045+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:26:30.694+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:25:52.004+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:25:30.691+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:24:51.987+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:24:30.748+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:23:51.969+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:23:30.740+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:22:51.923+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:22:10.692+02:00 |                  | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:22:10.682+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:22:06.901+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:21:50.677+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:21:50.661+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:21:30.699+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:21:30.684+02:00 | soaking          | In Tenant k8s, 10.58.24.210 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8F:9E;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:20:51.858+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:20:30.617+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:19:51.842+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:19:30.617+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:19:05.697+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:51.827+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:51.803+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:30.596+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:27.772+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:10.604+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:18:05.688+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:17:51.787+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:17:51.782+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:17:30.613+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:17:25.910+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:17:10.601+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:16:51.731+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:16:30.563+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | --  | F3083 | config-error         | 2023-06-07T08:16:12.903+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:15:51.687+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:15:30.552+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:15:06.663+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:50.600+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:45.649+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:30.541+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:27.656+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:10.632+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:14:10.608+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:13:51.668+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:13:51.653+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:13:30.542+02:00 |                  | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:13:25.866+02:00 | soaking          | In Tenant k8s, 10.58.24.195 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:3F:95;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:13:10.559+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:12:51.593+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:12:30.516+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:11:51.573+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:11:10.549+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:10:51.586+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:10:30.498+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:09:51.503+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:09:30.504+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:08:51.470+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:08:30.474+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:07:51.441+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:07:10.501+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:06:51.421+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:06:30.477+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:05:51.410+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:05:30.453+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:04:51.347+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:04:30.447+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:04:27.361+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:04:10.464+02:00 |                  | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:04:06.335+02:00 | soaking          | In Tenant k8s, 10.58.24.194 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:32:38;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_3/cep-00:50:56:B4:12:F5;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:03:50.459+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:03:48.325+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:03:30.436+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:03:25.755+02:00 | soaking          | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
| k8s    | Maj | F3083 | config-error         | 2023-06-07T08:02:50.440+02:00 |                  | In Tenant k8s, 10.58.24.211 is detected on multiple MACs (Context: 2818048.      | 
|        |     |       |                      |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:E8:11;          | 
|        |     |       |                      |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_4/cep-00:50:56:B4:8C:43;). This can happen when   | 
|        |     |       |                      |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,         | 
|        |     |       |                      |                               |                  | duplicate external IP configuration on external devices, ect.                    | 
+--------+-----+-------+----------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci tenant --apic apic21 --name k8s --when any --view hfault

{
    "duration": 16495,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 487,
        "disconnect_time": 0,
        "mo_time": 7063,
        "total_time": 7550
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	487	-	connect apic21o.emea-sp.cisco.com:443
True	623	12	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	6440	4244	apic21o.emea-sp.cisco.com:443 class fvTenant query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./Tenant.md)