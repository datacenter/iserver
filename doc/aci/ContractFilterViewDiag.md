# Contract Filter

## Diag view

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view diag

Apic: apic21 (mode:online, cache:off)

Contract Filter - Faults [#0]
-----------------------------
None

Contract Filter - Fault Records last 10y [#0]
---------------------------------------------
None

Contract Filter - Event Logs last 10y [#0]
------------------------------------------
None

Contract Filter - Audit Logs last 10y [#78]
-------------------------------------------

+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| Contract Filter | Sev  | Code     | Cause      | Created Time                  | Description         | Change Set                                                                     |
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T21:45:10.494+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T21:45:02.675+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T21:44:40.188+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T21:44:38.937+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T19:55:30.425+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T19:55:25.272+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T19:47:21.683+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T19:47:20.804+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T19:31:52.045+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T19:31:47.330+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T19:31:31.987+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T19:31:29.812+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T16:58:41.712+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T16:58:37.093+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T16:58:16.914+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T16:58:16.224+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T16:03:51.687+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T16:03:48.220+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T16:03:02.326+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T16:02:59.848+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-12T12:35:43.521+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-12T12:35:40.048+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-12T12:35:10.378+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-12T12:35:07.209+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-06T20:34:47.635+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-06T20:34:44.778+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-06T20:34:22.999+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-06T20:34:20.642+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-12-05T12:21:06.300+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-12-05T12:20:47.429+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-12-05T10:28:50.497+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-12-05T10:28:48.658+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-21T19:17:43.581+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-21T19:17:34.581+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-21T19:17:12.116+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-21T19:17:10.843+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-21T18:16:21.289+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-21T18:16:16.748+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-21T18:15:25.937+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-21T18:15:24.936+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-21T18:08:10.593+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-21T18:08:04.723+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-21T18:07:14.010+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-21T18:07:11.330+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-18T19:20:49.714+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-18T19:20:45.581+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-18T19:20:25.657+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-18T19:20:24.427+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-18T19:12:08.876+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-18T19:12:06.238+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-18T19:11:42.056+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-18T19:11:39.586+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-18T19:07:17.584+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-18T19:07:09.980+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-18T19:06:40.460+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-18T19:06:38.168+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-18T18:58:11.343+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-18T18:58:04.069+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-18T18:45:32.860+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-18T18:45:31.411+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-18T18:42:52.173+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-18T18:42:46.037+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-18T15:25:10.989+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-18T15:25:08.974+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-08T22:44:33.403+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-08T22:44:28.195+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-08T22:41:01.192+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-08T22:40:59.232+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-08T22:39:03.555+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-08T22:38:58.763+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-08T22:38:09.746+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-08T22:38:08.655+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-03T20:21:14.100+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-03T20:21:11.640+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213660 | transition | 2022-11-03T20:20:56.306+02:00 | Filter icmp deleted |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213657 | transition | 2022-11-03T20:20:54.544+02:00 | Entry icmp deleted  |                                                                                | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213655 | transition | 2022-11-03T20:11:21.793+02:00 | Entry icmp created  | annotation:orchestrator:terraform, applyToFrag:no, arpOpc:unspecified,         | 
|                 |      |          |            |                               |                     | dFromPort:unspecified, dToPort:unspecified, etherT:ipv4, icmpv4T:unspecified,  | 
|                 |      |          |            |                               |                     | icmpv6T:unspecified, matchDscp:unspecified, name:icmp, prot:icmp,              | 
|                 |      |          |            |                               |                     | sFromPort:unspecified, sToPort:unspecified, stateful:no, userdom::all:common:  | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
| k8s/icmp        | Info | E4213658 | transition | 2022-11-03T20:11:16.725+02:00 | Filter icmp created | annotation:orchestrator:terraform, name:icmp, userdom::all:common:             | 
+-----------------+------+----------+------------+-------------------------------+---------------------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci contract filter
    --apic apic21
    --name k8s/icmp
    --when any
    --view diag

{
    "duration": 12364,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 415,
        "disconnect_time": 0,
        "mo_time": 11442,
        "total_time": 11857
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

True	415	-	connect apic21o.emea-sp.cisco.com:443
True	364	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	356	0	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=faults,no-scoped,subtree
True	4153	0	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	3242	29	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	3327	623	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ContractFilter.md)