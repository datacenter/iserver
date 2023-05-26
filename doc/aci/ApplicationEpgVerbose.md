# Application Endpoint Group (EPG)

## Verbose output

Get selected EPG details
- EPG properties
- Consumed and provided contracts with filters
- Bridge Domain properties and subnets
- VRF properties
- Associated L3 Outs properties
- Deployed nodes
- Endpoints

Note: All selected EPGs will be shown in verbose mode

```
# iserver get aci epg --apic apic21 --name vk8s_1 -o verbose

Apic: apic21

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | Subnets         | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+

Application EPG Properties
--------------------------
- Up                     : V
- Configuration State    : applied
- EPG Name               : vk8s_1
- Application Profile    : k8s_ANP
- Tenant                 : k8s
- Bridge Domain          : k8s/vk8s_1_BD
- Alias                  : 
- Description            : 
- Annotations            : orchestrator:terraform
- Class ID               : 49162
- Contract Exception Tag : 
- QoS Class              : unspecified
- Intra EPG Isolation    : unenforced
- Preferred Group Member : exclude
- Flood in Encapsulation : disabled
- ESG Matched            : 

Contract Consumed
-----------------
- common/k8s_vm

Standard Contracts
------------------

+---------------+--------+--------+---------+-------------+---------------+------------+
| Contract Name | Tenant | Scope  | Intent  | Target DSCP | Subject       | Filter     |
+---------------+--------+--------+---------+-------------+---------------+------------+
| k8s_vm        | common | global | install | unspecified | k8s/k8s_tn_bm | common/any | 
+---------------+--------+--------+---------+-------------+---------------+------------+

Contract Filters
----------------

+-------------+--------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| Filter Name | Tenant | Entry | Ether | ARP Flag | Proto | Fragments | Stateful | Source | Destination | Rules |
+-------------+--------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+
| any         | common | any   | ipv4  |          |       | no        | no       |        |             |       | 
+-------------+--------+-------+-------+----------+-------+-----------+----------+--------+-------------+-------+

Bridge Domain Properties
------------------------
- Name                  : vk8s_1_BD
- Tenant                : k8s
- Dn                    : uni/tn-k8s/BD-vk8s_1_BD
- Description           : Cloud_1_BD (Managed by Terraform)
- Health Score          : 100
- Type                  : regular
- Subnet Count          : 1
- VRF                   : common/Infra_VRF
- Associated L3 Outs    : 1
- Endpoints Count       : 
- Endpoint Groups Count : 


+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| Network         | Gateway      | Preferred | Virtual | Scope  | IP Data Plane Learning | IP Usage | IP Available |
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+
| 10.58.24.160/28 | 10.58.24.174 | no        | no      | public | enabled                | 10/14    | 4            | 
+-----------------+--------------+-----------+---------+--------+------------------------+----------+--------------+

VRF Properties
--------------
- Name                                  : Infra_VRF
- Tenant                                : common
- Data Plane Learning                   : enabled
- Multicast                             : permit
- Policy Control Enforcement Direction  : ingress
- Policy Control Enforcement Preference : unenforced
- Bridge Domain Enforcement Status      : no


Associated L3 Out
-----------------
No L3Out found

Deployed Nodes
--------------

+------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+
| Apic | Node Name            | Node ID | Pod ID | IP Address  | Admin State | Fabric State | Role | Model          | Serial      | Version        |
+------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+
| None | pod-1/cl2207-eu-spdc | 2207    | 1      | 10.5.240.34 | on          | active       | leaf | N9K-C9336C-FX2 | FDO23490E4G | n9000-15.2(7f) | 
| None | pod-1/cl2208-eu-spdc | 2208    | 1      | 10.5.240.35 | on          | active       | leaf | N9K-C9336C-FX2 | FDO234807ED | n9000-15.2(7f) | 
+------+----------------------+---------+--------+-------------+-------------+--------------+------+----------------+-------------+----------------+

EPG Endpoints
-------------

+----+-------------------+--------------+--------+--------+---------+------------------+
| SF | MAC Address       | IP Address   | Tenant | EPG    | Ap      | VRF              |
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:11:50 | 10.58.24.161 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:3D:19 | 10.58.24.170 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:67:1F | 10.58.24.162 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
|    |                   | 10.58.24.167 |        |        |         |                  | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:85:73 | 10.58.24.165 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:9C:81 | 10.58.24.163 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
|    |                   | 10.58.24.168 |        |        |         |                  | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:9E:D0 | 10.58.24.169 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| V  | 00:50:56:B4:D2:45 |              | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
| LV | 00:50:56:B4:EB:6A | 10.58.24.166 | k8s    | vk8s_1 | k8s_ANP | common/Infra_VRF | 
+----+-------------------+--------------+--------+--------+---------+------------------+
```

[[Back]](./ApplicationEpg.md)