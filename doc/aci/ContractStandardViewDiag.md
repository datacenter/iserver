# Standard Contract

## Diag view

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view diag

Apic: apic21 (mode:online, cache:off)

Standard Contract - Faults [#0]
-------------------------------
None

Standard Contract - Fault Records last 10y [#0]
-----------------------------------------------
None

Standard Contract - Event Logs last 10y [#0]
--------------------------------------------
None

Standard Contract - Audit Logs last 10y [#45]
---------------------------------------------

+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| Standard Contract | Sev  | Code     | Cause      | Created Time                  | Description               | Change Set                                                                   |
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T21:45:12.493+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T21:45:10.489+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T21:45:04.986+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T21:44:41.850+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T21:44:38.145+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T21:44:38.145+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T19:55:32.418+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T19:55:30.254+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T19:55:24.308+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T19:47:22.410+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T19:47:20.428+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T19:47:20.428+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T19:31:53.256+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T19:31:52.050+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T19:31:47.242+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T19:31:33.340+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T19:31:29.696+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T19:31:29.696+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T16:58:51.148+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T16:58:50.069+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T16:58:34.630+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T16:58:18.577+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T16:58:14.735+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T16:58:14.734+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T16:03:51.921+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T16:03:51.741+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T16:03:45.856+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T16:03:03.084+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T16:02:59.805+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T16:02:59.804+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-12T12:35:45.053+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-12T12:35:44.708+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-12T12:35:38.677+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-12T12:35:11.013+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-12T12:35:08.730+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-12T12:35:08.730+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-06T20:34:48.900+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-06T20:34:47.640+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-06T20:34:43.248+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213651 | transition | 2022-12-06T20:34:24.098+02:00 | BrCP k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213696 | transition | 2022-12-06T20:34:20.269+02:00 | RsSubjFiltAtt any deleted |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213702 | transition | 2022-12-06T20:34:20.269+02:00 | Subj k8s_tn_bm deleted    |                                                                              | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213694 | transition | 2022-12-05T12:50:55.127+02:00 | RsSubjFiltAtt any created | action:permit, annotation:orchestrator:terraform, priorityOverride:default,  | 
|                   |      |          |            |                               |                           | tnVzFilterName:any, userdom::all:common:                                     | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213700 | transition | 2022-12-05T12:50:55.050+02:00 | Subj k8s_tn_bm created    | annotation:orchestrator:terraform, consMatchT:AtleastOne, name:k8s_tn_bm,    | 
|                   |      |          |            |                               |                           | prio:unspecified, provMatchT:AtleastOne, revFltPorts:yes,                    | 
|                   |      |          |            |                               |                           | targetDscp:unspecified, userdom::all:common:                                 | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
| k8s/k8s_tn_bm     | Info | E4213649 | transition | 2022-12-05T12:50:53.781+02:00 | BrCP k8s_tn_bm created    | annotation:orchestrator:terraform, intent:install, name:k8s_tn_bm,           | 
|                   |      |          |            |                               |                           | prio:unspecified, scope:global, targetDscp:unspecified, userdom::all:common: | 
+-------------------+------+----------+------------+-------------------------------+---------------------------+------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci contract standard
    --apic apic21
    --name k8s/k8s_tn_bm
    --when any
    --view diag

{
    "duration": 5987,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 466,
        "disconnect_time": 0,
        "mo_time": 4842,
        "total_time": 5308
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

True	466	-	connect apic21o.emea-sp.cisco.com:443
True	390	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	403	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzRsSubjFiltAtt
True	515	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=vzEntry
True	459	0	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=faults,no-scoped,subtree
True	940	9	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	985	6	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
True	1150	456	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree-include=audit-logs,no-scoped,subtree&order-by=aaaModLR.created|desc&page=0&page-size=1000
```

[[Back]](./ContractStandard.md)