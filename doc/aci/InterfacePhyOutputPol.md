# Node Interface - Physical

## Policy focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o pol

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
| Node                | Interface | Oper | Type | Policy Group Type | Policy Group Name       | Link Level     | Link Flap | CDP         | MCP         | LLDP         | STP     |
+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
| pod-1/bl205-eu-spdc | 1/1       | up   | leaf | infraAccBndlGrp   | UCSB1-FI-A_PolGrp       | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/2       | up   | leaf | infraAccBndlGrp   | UCSB1-FI-B_PolGrp       | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/3       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/4       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/5       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/6       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/7       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/8       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/9       | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/10      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/11      | up   | leaf | infraAccBndlGrp   | HX1-FI-A_PolGrp         | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/12      | up   | leaf | infraAccBndlGrp   | HX1-FI-B_PolGrp         | Inherit        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/13      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/14      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/15      | up   | leaf | infraAccPortGrp   | P5G-CU-PCIe1-A_PolGrp   | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/16      | up   | leaf | infraAccPortGrp   | P5G-CU-PCIe2-A_PolGrp   | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/17      | down | leaf | infraAccPortGrp   | P5G-Core-PCIe1-A_PolGrp | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/18      | down | leaf | infraAccPortGrp   | P5G-Core-PCIe2-A_PolGrp | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/19      | up   | leaf | infraAccPortGrp   | P5G-Core-MLOM-1_PolGrp  | Inherit        | default   | default     | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/20      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/21      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/22      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/23      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/24      | up   | leaf | infraAccPortGrp   | Infra-BGP_PolGrp        | default        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/25      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/26      | down | leaf |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/27      | up   | leaf | infraAccBndlGrp   | SPN_PolGrp              | 10G-fix        | default   | CDP_enable  | default     | LLDP_enable  | default | 
| pod-1/bl205-eu-spdc | 1/28      | up   | leaf | infraAccPortGrp   | SR-Demo-CDC-2-vlan      | fabric-inherit | default   | cdp-enabled | mcp-enabled | lldp-enabled | default | 
| pod-1/bl205-eu-spdc | 1/29      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/30      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/31      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/32      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/33      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/34      | down | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/35      | up   | fab  |                   |                         |                |           |             |             |              |         | 
| pod-1/bl205-eu-spdc | 1/36      | up   | fab  |                   |                         |                |           |             |             |              |         | 
+---------------------+-----------+------+------+-------------------+-------------------------+----------------+-----------+-------------+-------------+--------------+---------+
```

[[Back]](./InterfacePhy.md)