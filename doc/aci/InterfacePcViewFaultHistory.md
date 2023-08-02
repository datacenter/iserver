# Node Interface - Port Channel (PC)

## Fault history view

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Port Channel - Fault Records last 10y [#451]
------------------------------------------------------

+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                   | Created Time                  | Lifecycle        | Description                                                                     |
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-08-17T11:30:43.731+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-08-17T11:32:55.812+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2021-08-17T11:35:03.427+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2021-08-17T12:35:04.128+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:38:32.853+02:00 | soaking          | Port is down, reason being init(connected), used by EPG on node 2205 of fabric  | 
|                      |           |      |       |                         |                               |                  | ACI2-EU-SPDC with hostname bl2205-eu-spdc                                       | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-09-22T17:38:32.887+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:40:53.117+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-09-22T17:40:53.117+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-09-22T17:47:42.064+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-09-22T17:47:46.500+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0532 | interface-physical-down | 2021-09-22T17:49:53.196+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2021-09-22T17:49:53.197+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0532 | interface-physical-down | 2021-09-22T18:49:53.810+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2021-09-22T18:49:53.811+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-10-14T19:08:40.557+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-14T19:08:40.542+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-10-14T19:10:40.741+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-14T19:10:40.740+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:11:45.225+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:11:46.696+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:11:49.918+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2021-10-28T22:14:18.644+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:16:34.832+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:16:50.435+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:16:51.690+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:16:54.396+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:18:16.217+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2021-10-28T22:20:18.699+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:55:51.428+02:00 | soaking          | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:56:00.127+02:00 | soaking-clearing | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F1192 | config-failure          | 2021-11-09T10:56:21.101+02:00 |                  | Port-channel(po1) membership configuration failure for eth1/25                  | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-10T14:39:02.512+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-10T14:39:09.643+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-10T14:41:37.269+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-10T14:43:40.821+02:00 | soaking          | Port is down, reason:init(connected), used by:Discovery                         | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-10T14:43:51.163+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-10T14:46:07.314+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2021-12-10T14:49:58.300+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2021-12-10T14:50:06.197+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2021-12-10T14:50:22.547+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2021-12-10T14:50:29.698+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2021-12-10T14:50:45.976+02:00 | soaking          | Port is down, reason:init(connected), used by:Discovery                         | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2021-12-10T14:51:10.930+02:00 | soaking          | Port is down, reason:init(connected), used by:Discovery                         | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2021-12-10T14:53:07.388+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2021-12-10T14:53:37.377+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-10T15:46:08.025+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2021-12-13T21:13:14.732+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2021-12-13T21:15:20.759+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2021-12-13T22:15:22.438+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-13T23:11:41.237+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-13T23:11:51.062+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2021-12-13T23:13:53.311+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2021-12-14T00:11:17.354+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2021-12-14T00:13:24.123+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2021-12-14T00:13:54.125+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2021-12-14T01:13:24.717+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:00:59.193+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:03:01.186+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:11:21.296+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2021-12-16T13:13:31.285+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:16:40.144+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:19:01.340+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:26:54.400+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-16T13:29:01.425+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:33:31.150+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:35:31.483+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2021-12-16T13:43:04.415+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-16T13:45:31.569+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:47:52.615+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:50:01.645+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2021-12-16T13:57:26.251+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2021-12-16T13:59:31.694+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2021-12-16T14:45:32.127+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2021-12-16T14:59:32.469+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Crit | F0532 | interface-physical-down | 2021-12-17T13:15:50.357+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-14T00:01:03.417+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-01-14T00:01:03.453+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-01-14T00:01:03.441+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-01-14T00:01:03.406+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-01-14T00:01:03.390+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2022-01-14T00:01:03.428+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2022-01-14T00:01:57.074+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-14T00:02:02.560+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-01-14T00:02:03.304+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-01-14T00:02:04.723+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-01-14T00:02:06.174+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-01-14T00:03:18.677+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-14T00:04:18.690+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-01-14T00:04:18.691+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2022-01-14T00:04:18.691+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-01-14T00:04:18.689+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0532 | interface-physical-down | 2022-01-14T00:04:18.690+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-14T01:04:19.291+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-01-14T01:04:19.293+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2022-01-14T01:04:19.292+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-01-14T01:04:19.290+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0532 | interface-physical-down | 2022-01-14T01:04:19.291+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2022-01-19T20:48:05.536+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2022-01-19T20:50:14.787+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Crit | F0532 | interface-physical-down | 2022-01-19T20:50:17.109+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0532 | interface-physical-down | 2022-01-19T20:52:44.803+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0532 | interface-physical-down | 2022-01-19T21:52:45.370+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:01.835+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:01.908+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-01-27T16:48:01.889+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:01.855+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-01-27T16:48:01.811+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:01.874+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-01-27T16:48:52.343+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:58.669+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-01-27T16:48:58.439+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-01-27T16:49:00.464+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-01-27T16:49:03.165+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-01-27T16:50:16.839+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-27T16:51:16.846+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-01-27T16:51:16.848+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-01-27T16:51:16.846+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2022-01-27T16:51:16.845+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-01-27T16:51:16.847+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F1192 | config-failure          | 2022-01-27T17:50:33.428+02:00 | soaking          | Port-channel(po3) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F1192 | config-failure          | 2022-01-27T17:50:43.291+02:00 | soaking-clearing | Port-channel(po3) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-01-27T17:50:56.220+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-01-27T17:51:17.489+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-01-27T17:51:17.490+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-01-27T17:51:17.489+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2022-01-27T17:51:17.488+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-01-27T17:51:17.490+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F1192 | config-failure          | 2022-01-27T17:52:47.496+02:00 | retaining        | Port-channel(po3) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-01-27T17:53:17.502+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F1192 | config-failure          | 2022-01-27T18:52:48.006+02:00 |                  | Port-channel(po3) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-01-27T18:53:18.011+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.277+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.249+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-04-22T15:56:36.204+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.236+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.262+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-04-22T15:56:36.223+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:26.664+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:32.219+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:33.138+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:34.175+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-04-22T15:57:35.987+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-04-22T15:57:35.370+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.172+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.171+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-04-22T15:59:51.168+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.170+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.172+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-04-22T15:59:51.169+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.990+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.989+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-04-22T16:59:51.987+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.988+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.989+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-04-22T16:59:51.988+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.869+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.921+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-05-09T23:40:41.193+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.844+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.896+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-05-09T23:40:41.963+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.178+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.178+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-05-09T23:43:11.177+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.177+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.178+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-05-09T23:43:11.179+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:05.540+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:05.579+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-05-09T23:48:07.413+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:07.992+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:08.997+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-05-09T23:48:14.213+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:11.286+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:11.287+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-05-09T23:50:11.285+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:11.286+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:11.288+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-05-09T23:50:41.289+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:11.895+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:11.895+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-05-10T00:50:11.893+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:11.894+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:11.896+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-05-10T00:50:41.898+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-06-08T16:22:54.011+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-06-08T16:25:20.688+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:43.984+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:44.025+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-06-13T12:13:44.055+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:44.041+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:44.077+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-06-13T12:13:44.006+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:40.412+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:41.509+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:41.312+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:42.148+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-13T12:14:51.436+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-06-13T12:15:58.774+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.786+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.784+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.786+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.787+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-06-13T12:16:58.785+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.392+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.391+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.392+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.393+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-06-13T13:16:59.391+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-06-13T21:38:32.057+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-06-13T21:40:34.397+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-06-13T22:40:34.955+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:13:05.029+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:15:19.688+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-06-18T12:16:53.846+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-18T12:19:19.718+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-06-18T13:19:20.518+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-07-07T12:11:09.027+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-07-07T12:13:09.967+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-07-07T13:37:49.756+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-07-07T13:40:11.095+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-07-07T14:40:11.641+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-07-15T19:29:47.985+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-07-15T19:32:11.774+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-07-15T19:40:07.301+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-07-15T19:42:11.877+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-07-15T20:42:12.417+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-07-19T10:26:51.757+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-07-19T10:27:03.011+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-07-19T10:28:26.657+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-07-19T10:28:37.901+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-07-19T10:28:54.878+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-07-19T10:29:04.199+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-07-19T10:29:06.267+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F1192 | config-failure          | 2022-07-19T10:30:27.836+02:00 | soaking          | Port-channel(po5) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-07-19T10:30:28.035+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F1192 | config-failure          | 2022-07-19T10:30:42.138+02:00 | soaking-clearing | Port-channel(po5) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-07-19T10:30:55.123+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2022-07-19T10:31:04.228+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-07-19T10:31:34.239+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2022-07-19T10:33:04.241+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | --   | F1192 | config-failure          | 2022-07-19T10:33:04.237+02:00 | retaining        | Port-channel(po5) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-07-19T10:38:56.869+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F1192 | config-failure          | 2022-07-19T10:38:56.602+02:00 | soaking          | Port-channel(po6) membership configuration failure for eth1/12                  | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F1192 | config-failure          | 2022-07-19T10:39:12.210+02:00 | soaking-clearing | Port-channel(po6) membership configuration failure for eth1/12                  | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-07-19T10:39:22.157+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-07-19T10:41:34.315+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F1192 | config-failure          | 2022-07-19T10:41:34.313+02:00 | retaining        | Port-channel(po6) membership configuration failure for eth1/12                  | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-07-19T11:11:25.032+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-07-19T11:12:13.047+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F1192 | config-failure          | 2022-07-19T11:12:13.040+02:00 |                  | Port-channel(po6) membership configuration failure for eth1/12                  | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2022-07-19T11:31:04.766+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-07-19T11:31:34.769+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2022-07-19T11:33:04.784+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | --   | F1192 | config-failure          | 2022-07-19T11:33:04.781+02:00 |                  | Port-channel(po5) membership configuration failure for eth1/19                  | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-07-19T12:11:44.992+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-07-19T12:11:55.695+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-07-19T12:14:05.318+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-07-19T13:14:06.655+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-07-19T13:46:03.216+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-07-19T13:46:13.551+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2022-07-19T13:48:02.520+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-07-19T13:48:16.635+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-07-19T13:48:27.900+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-07-19T13:50:37.541+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-07-19T14:50:38.462+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-09-01T14:28:59.042+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2022-09-01T14:31:28.874+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.651+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.584+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-09-14T23:56:03.621+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.638+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.596+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:03.609+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:57.434+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:57.790+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:57.349+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2022-09-14T23:56:59.870+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2022-09-14T23:57:01.119+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-09-14T23:58:19.022+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.033+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.031+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.033+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.031+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-09-14T23:59:19.032+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.748+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.746+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.748+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.747+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2022-09-15T00:59:19.747+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-09-22T16:06:58.187+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2022-09-22T16:09:16.206+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-09-22T16:40:03.476+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2022-09-22T16:42:16.606+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-10-05T23:51:39.242+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-10-05T23:54:04.266+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2022-10-05T23:55:29.263+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-10-05T23:57:34.587+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2022-10-06T00:57:35.130+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Crit | F0532 | interface-physical-down | 2023-03-02T16:59:59.841+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2023-03-02T17:02:28.903+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0532 | interface-physical-down | 2023-03-02T18:02:29.559+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.417+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.454+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.442+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Crit | F0532 | interface-physical-down | 2023-03-02T20:49:49.485+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.470+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-03-02T20:49:49.429+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:36.752+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:37.889+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:39.897+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Crit | F0532 | interface-physical-down | 2023-03-02T20:50:41.766+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:41.863+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-03-02T20:50:47.858+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.629+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.631+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.630+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0532 | interface-physical-down | 2023-03-02T20:52:49.632+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.631+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-03-02T20:52:49.630+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.188+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.190+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.189+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0532 | interface-physical-down | 2023-03-02T21:52:50.191+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.190+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-03-02T21:52:50.188+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-03-03T01:54:59.291+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-03-03T01:57:22.953+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-03-03T02:05:59.920+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-03-03T02:08:23.072+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:19:27.603+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:21:53.202+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-03-03T02:30:07.889+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-03T02:32:23.297+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-03-03T03:08:24.082+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-03-03T03:32:24.448+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-03-03T10:37:56.847+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-03-03T10:39:59.955+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-03-03T10:48:48.398+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-03-03T10:51:00.178+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-03-03T11:51:01.016+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-03-03T12:12:52.462+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-03-03T12:15:01.432+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-03-03T12:23:45.254+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-03-03T12:26:01.532+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-03-03T13:26:02.175+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Crit | F0532 | interface-physical-down | 2023-04-12T18:25:22.404+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Crit | F0532 | interface-physical-down | 2023-04-12T18:27:25.051+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-04-27T12:04:40.201+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-04-27T12:04:47.679+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-04-27T12:06:49.341+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-04-27T12:06:49.340+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-04-27T12:13:26.594+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-04-27T12:13:35.356+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-04-27T12:15:49.423+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-04-27T12:15:49.421+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-04-27T13:15:50.335+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-04-27T13:15:50.334+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.206+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-05-30T21:08:36.255+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.231+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.243+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.219+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-05-30T21:08:36.272+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:29.180+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:33.766+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:34.986+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:38.288+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-05-30T21:09:38.381+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-05-30T21:10:51.386+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.397+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.399+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.399+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.398+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-05-30T21:11:51.400+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.954+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.955+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.955+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.954+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-05-30T22:11:51.956+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-04T18:38:23.626+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2023-06-04T18:40:28.940+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-04T18:48:31.969+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-04T18:50:59.036+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-04T18:55:25.115+02:00 | raised-clearing  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2023-06-04T18:57:29.186+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2023-06-04T19:57:30.149+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-07T11:56:52.510+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-07T11:57:06.889+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-07T11:59:16.898+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-07T11:59:16.897+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-07T17:03:04.193+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-07T17:05:24.652+02:00 | raised           | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-07T18:12:47.268+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-07T18:14:55.994+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-07T18:23:25.642+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-07T18:25:26.090+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-06-07T18:50:05.474+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-06-07T18:52:26.911+02:00 | raised           | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-06-07T19:00:37.556+02:00 | raised-clearing  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-06-07T19:02:57.905+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-07T19:25:28.519+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-06-07T20:02:59.833+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.855+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-12T11:30:18.822+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.841+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.809+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.795+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-06-12T11:30:18.870+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:16.856+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:21.555+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:21.636+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:24.807+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Warn | F0546 | interface-physical-down | 2023-06-12T11:31:24.526+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Crit | F0532 | interface-physical-down | 2023-06-12T11:31:26.482+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.562+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2023-06-12T11:33:33.561+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.562+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.560+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.560+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-06-12T11:33:33.563+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.173+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0532 | interface-physical-down | 2023-06-12T12:33:35.173+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.173+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.172+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.172+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-06-12T12:33:35.174+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.479+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.505+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.545+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.533+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2023-06-18T09:46:23.516+02:00 | soaking          | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-06-18T09:46:23.492+02:00 | soaking          | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:18.553+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:19.580+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:22.784+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | Crit | F0532 | interface-physical-down | 2023-06-18T09:47:22.681+02:00 | soaking-clearing | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:22.985+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | Warn | F0546 | interface-physical-down | 2023-06-18T09:47:29.645+02:00 | soaking-clearing | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.647+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.648+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.650+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.649+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2023-06-18T09:49:38.649+02:00 | retaining        | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-06-18T09:49:38.647+02:00 | retaining        | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po1       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.134+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po2       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.135+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po3       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.136+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po4       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.136+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
| pod-1/bl2205-eu-spdc | po5       | --   | F0532 | interface-physical-down | 2023-06-18T10:49:39.135+02:00 |                  | Port is down, reason being noOperMembers(connected), used by EPG on node 2205   | 
|                      |           |      |       |                         |                               |                  | of fabric ACI2-EU-SPDC with hostname bl2205-eu-spdc                             | 
| pod-1/bl2205-eu-spdc | po6       | --   | F0546 | interface-physical-down | 2023-06-18T10:49:39.134+02:00 |                  | Port is down, reason:noOperMembers(connected), used by:Discovery                | 
+----------------------+-----------+------+-------+-------------------------+-------------------------------+------------------+---------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci intf pc
    --apic apic21
    --when any
    --node bl2205-eu-spdc
    --view hfault

{
    "duration": 4227,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 402,
        "disconnect_time": 0,
        "mo_time": 2073,
        "total_time": 2475
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

True	402	-	connect apic21o.emea-sp.cisco.com:443
True	313	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	473	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	313	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vpcDom query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	307	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/vlanCktEp
True	667	451	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/pcAggrIf query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./InterfacePc.md)