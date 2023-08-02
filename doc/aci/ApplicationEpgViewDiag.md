# Application Endpoint Group (EPG)

## Diag view

```
# iserver get aci epg --apic apic21 --when 60d --name vk8s_1 --view diag

Apic: apic21 (mode:online, cache:off)

EPG - Faults [#0]
-----------------
None

EPG - Fault Records last 60d [#141]
-----------------------------------

+--------------------+-----+-------+--------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| EPG                | Sev | Code  | Cause        | Created Time                  | Lifecycle        | Description                                                                     |
+--------------------+-----+-------+--------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-26T08:03:42.002+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-26T08:03:40.663+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:04:A1;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:52:08.186+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:52:07.918+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:1F:B2;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:D3:91;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:45:48.149+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E8:E7;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:45:48.063+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E7:C4;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:E8:E7;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:05:07.755+02:00 |                  | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T20:05:07.144+02:00 | soaking          | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:CE:19;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:58:05.480+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:58:05.398+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:57:05.483+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:45:92;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:57:05.396+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:45:92;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:53:05.454+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:53:05.362+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:25.450+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:25.437+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:24.716+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:24.710+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:05.433+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:52:05.349+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:51:25.410+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:51:24.670+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:75:8B;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:80:48;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:51:05.440+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:64:9A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:51:05.352+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:48:C3;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:64:9A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:08:05.030+02:00 |                  | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:11:50;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-07-12T15:08:04.268+02:00 | soaking          | In Tenant k8s, 10.58.24.161 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:32:62;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:11:50;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T14:16:10.491+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T13:50:52.650+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:48:49.835+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:48:31.869+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:47:49.823+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:47:31.823+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:46:49.854+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:46:31.846+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:45:49.878+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:45:34.813+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:45:29.841+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:45:14.898+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:44:49.940+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:44:31.742+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:49.801+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:34.812+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:29.938+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:29.933+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:14.872+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:14.861+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:14.847+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9E:D0;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:43:10.720+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T13:41:22.434+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:38:54.820+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:38:37.542+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:37:54.774+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:37:37.519+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:36:54.781+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:36:37.490+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:54.763+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:49.697+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:37.428+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:37.422+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:14.682+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:34:10.412+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:33:09.672+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:32:54.692+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:32:34.720+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:32:31.406+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:29:54.670+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:29:52.283+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:29:34.689+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:29:31.307+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T13:15:51.653+02:00 | retaining        | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:54.444+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:51.764+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:34.440+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:29.495+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:29.479+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:13:09.774+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:12:54.433+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:12:51.731+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:12:34.442+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:12:30.722+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:08:54.426+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:08:51.612+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:08:34.395+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T13:08:30.616+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T12:54:51.067+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:52:49.263+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:52:34.093+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:52:30.138+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:52:12.129+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:51:54.044+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:51:51.083+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T12:50:50.925+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:48:49.281+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:48:29.968+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:30:49.031+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:30:35.422+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:29:48.998+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T12:29:35.400+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T12:11:49.815+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:12:52.928+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:12:48.126+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:12:32.880+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:12:30.091+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T11:11:48.026+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:09:32.920+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:09:14.954+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:08:32.938+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:08:14.921+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T11:06:47.864+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:04:32.859+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T11:04:14.797+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:32.356+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:27.567+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:12.398+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:12.376+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:07.722+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:28:07.717+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:16:32.217+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:16:28.373+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T10:12:46.308+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:10:27.331+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:10:07.280+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:08:47.235+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:08:32.108+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:07:32.047+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T10:07:28.089+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:67:1F;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T09:35:15.189+02:00 | retaining        | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:32:46.687+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:32:26.819+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:30:11.719+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:30:08.977+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:29:06.760+02:00 |                  | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T09:28:51.671+02:00 | soaking          | In Tenant k8s, 10.58.24.162 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:85:73;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T09:16:14.648+02:00 |                  | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T08:16:12.903+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T08:14:10.632+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T08:13:51.668+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T08:01:12.879+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T07:59:05.502+02:00 | soaking-clearing | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | Maj | F3083 | config-error | 2023-06-07T07:58:48.220+02:00 | soaking          | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
| k8s/k8s_ANP/vk8s_1 | --  | F3083 | config-error | 2023-06-07T07:58:12.362+02:00 | retaining        | In Tenant k8s, 10.58.24.163 is detected on multiple MACs (Context: 2818048.     | 
|                    |     |       |              |                               |                  | First 3 fvCEps: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:EB:6A;         | 
|                    |     |       |              |                               |                  | uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1/cep-00:50:56:B4:9C:81;). This can happen when  | 
|                    |     |       |              |                               |                  | different MACs are sourcing traffic with the same IP due to NIC teaming,        | 
|                    |     |       |              |                               |                  | duplicate external IP configuration on external devices, ect.                   | 
+--------------------+-----+-------+--------------+-------------------------------+------------------+---------------------------------------------------------------------------------+

EPG - Event Logs last 60d [#107]
--------------------------------

+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| EPG                | Sev  | Code     | Cause      | Created Time                  | Description                                                          |
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-26T08:03:41.872+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T21:05:48.163+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.164 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:52:08.053+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:45:47.996+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:21:47.792+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.170 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:21:27.784+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.168 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:18:27.750+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.165 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T20:05:07.625+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.161 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T16:10:05.433+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.164 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:58:05.335+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:57:05.330+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:53:05.295+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:52:25.290+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:52:05.286+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:51:25.277+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:51:05.283+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-07-12T15:08:04.900+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.161 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T14:18:55.129+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.161 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T14:16:10.056+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.166 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T14:11:15.091+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.168 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:48:49.715+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:47:49.705+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:46:49.694+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:45:49.683+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:45:29.699+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:44:49.704+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:43:49.665+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:43:29.681+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:43:14.658+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:38:54.612+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:37:54.587+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:36:54.575+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:34:54.552+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:34:49.563+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:34:14.550+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:33:09.548+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:32:34.541+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:29:54.508+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:29:34.511+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:13:54.324+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:13:34.321+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:13:29.348+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:12:54.314+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:12:34.311+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:08:54.277+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T13:08:34.267+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:52:49.126+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:52:33.914+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:51:53.894+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:48:49.082+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:30:48.880+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T12:29:48.868+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T11:12:52.749+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T11:12:32.732+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T11:09:32.717+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T11:08:32.704+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T11:04:32.654+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:28:32.187+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:28:12.193+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:16:32.058+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:10:27.149+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:08:47.078+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T10:07:31.923+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T09:32:46.554+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T09:30:11.554+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T09:29:06.546+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T08:14:10.445+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:59:05.312+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:56:05.278+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:55:50.241+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:54:25.287+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:38:05.098+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:37:45.109+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:19:44.914+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:18:09.792+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T07:08:44.798+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T06:42:29.392+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T06:41:29.382+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T06:26:29.163+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T06:14:49.034+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T06:14:44.090+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:59:23.937+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:57:08.872+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:56:48.863+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:55:48.853+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:55:03.886+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:53:48.834+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:34:48.644+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:34:28.642+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:24:43.599+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:23:43.560+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:23:28.534+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:22:43.567+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T05:22:28.527+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T04:50:43.167+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T04:50:23.172+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T04:08:22.734+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:41:27.442+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:41:22.452+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:40:27.423+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:40:07.432+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:22:27.226+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:06:27.056+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:06:07.084+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T03:05:01.936+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.162 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T02:49:21.772+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+
| k8s/k8s_ANP/vk8s_1 | Info | E4209236 | transition | 2023-06-07T02:47:21.754+02:00 | IP detached. EPG: uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1. IP: 10.58.24.163 | 
+--------------------+------+----------+------------+-------------------------------+----------------------------------------------------------------------+

EPG - Audit Logs last 60d [#0]
------------------------------
None
```

Developer

```
# iserver get aci epg --apic apic21 --when 60d --name vk8s_1 --view diag

{
    "duration": 21695,
    "apic": {
        "read": true,
        "success": 7,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 6,
        "connect_time": 441,
        "disconnect_time": 0,
        "mo_time": 13375,
        "total_time": 13816
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

True	441	-	connect apic21o.emea-sp.cisco.com:443
True	527	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	424	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	375	12	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=faults,no-scoped,subtree
True	6255	3464	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	3882	4021	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1912	1873	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ApplicationEpg.md)