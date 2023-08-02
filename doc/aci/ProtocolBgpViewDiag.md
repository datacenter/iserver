# Node Protocol - BGP

## Diag view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view diag --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Faults [#0]
--------------------------
None

Protocol BGP - Fault Records [#101]
-----------------------------------

+---------------------+------+-------+-----------------------------+-------------------------------+------------------+--------------------------+------------------+----------------------------------------------------+
| Node                | Sev  | Code  | Cause                       | Created Time                  | Lifecycle        | Domain                   | Nbr              | Description                                        |
+---------------------+------+-------+-----------------------------+-------------------------------+------------------+--------------------------+------------------+----------------------------------------------------+
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T22:20:31.546+02:00 | soaking          | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Closing | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T22:22:49.165+02:00 | raised           | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T22:43:33.422+02:00 | raised-clearing  | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T22:45:49.630+02:00 | retaining        | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:03:57.328+02:00 | soaking          | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:03:57.306+02:00 | soaking          | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:03:57.290+02:00 | soaking          | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:13.967+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:13.954+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:14.774+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:17.251+02:00 | soaking-clearing | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:17.228+02:00 | soaking-clearing | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:05:18.719+02:00 | soaking-clearing | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:16.321+02:00 | raised           | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:16.320+02:00 | raised           | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:16.320+02:00 | raised           | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:25.562+02:00 | raised-clearing  | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:28.063+02:00 | raised-clearing  | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:06:53.575+02:00 | raised-clearing  | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:07:46.210+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:07:46.210+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:07:46.209+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:08:46.207+02:00 | retaining        | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:08:46.206+02:00 | retaining        | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-05-31T23:09:16.218+02:00 | retaining        | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:07:47.168+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:07:47.168+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:07:47.167+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:08:47.164+02:00 |                  | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:08:47.164+02:00 |                  | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-01T00:09:17.160+02:00 |                  | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:04:52.561+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Closing | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:05:29.929+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Closing | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:05:39.506+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Closing | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:06:54.304+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:07:54.325+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-06T12:07:54.324+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:43.550+02:00 | soaking          | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:43.538+02:00 | soaking          | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:48.793+02:00 | soaking          | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:48.776+02:00 | soaking          | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:55.586+02:00 | soaking-clearing | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:36:55.277+02:00 | soaking-clearing | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:37:02.952+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:37:03.152+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:37:03.080+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:38:12.989+02:00 | soaking-clearing | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:38:22.358+02:00 | soaking-clearing | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:38:56.643+02:00 | retaining        | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:38:56.643+02:00 | retaining        | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:39:26.614+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:39:26.613+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:39:26.613+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:40:26.572+02:00 | retaining        | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T10:40:26.571+02:00 | retaining        | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T11:38:57.112+02:00 |                  | overlay-1                | 172.16.11.1/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T11:38:57.111+02:00 |                  | overlay-1                | 172.16.11.228/32 | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T11:40:27.136+02:00 |                  | overlay-1                | 172.31.3.35/32   | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T11:40:27.135+02:00 |                  | overlay-1                | 15.16.3.1/32     | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-06-12T16:29:45.108+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T16:32:00.145+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-06-12T17:32:00.762+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T15:52:12.099+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T15:52:12.096+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:51:28.535+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:51:28.525+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:51:28.515+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:53:48.343+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:53:48.343+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:53:48.342+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:54:03.641+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-10T16:56:18.356+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-10T17:56:19.039+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:52:49.304+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:52:50.372+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:54:45.708+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:54:45.686+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:54:45.676+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:56:46.595+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:56:46.595+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:56:46.594+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T11:58:46.229+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:00:46.239+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:04:07.895+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:04:09.486+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:04:12.034+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Closing | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:29:01.818+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:29:01.777+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:29:01.746+02:00 | soaking          | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:31:16.528+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:31:16.527+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:31:16.527+02:00 | raised           | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:31:41.727+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:31:53.729+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | Warn | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:32:01.729+02:00 | raised-clearing  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:33:46.555+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:34:16.552+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T12:34:16.551+02:00 | retaining        | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T13:33:47.133+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T13:34:17.130+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3/32    | BGP peer is not established, current state Idle    | 
| pod-1/rl301-eu-spdc | --   | F0299 | protocol-bgp-adjacency-down | 2023-07-14T13:34:17.128+02:00 |                  | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2/32    | BGP peer is not established, current state Idle    | 
+---------------------+------+-------+-----------------------------+-------------------------------+------------------+--------------------------+------------------+----------------------------------------------------+

Protocol BGP - Event Logs [#246]
--------------------------------

+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| Node                | Sev  | Code     | Cause                  | Created Time                  | Description                              | Domain                         | Nbr              |
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T22:20:31.550+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Closing                               |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208056 | oper-state-change      | 2023-05-31T22:20:36.558+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T22:20:36.556+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T22:43:33.429+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T22:43:33.426+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208092 | admin-state-change     | 2023-05-31T22:57:45.040+02:00 | BGP instance is administratively         | --                             | --               | 
|                     |      |          |                        |                               | Enabled                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:28.742+02:00 | BGP domain operational state is changed  | overlay-1                      | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:44.150+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:44.097+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:44.075+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:47.766+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:47.585+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:47.445+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:48.675+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:48.427+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:48.339+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:49.302+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:49.198+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:49.191+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:03:51.922+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:03:51.919+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:03:51.909+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.655+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.614+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.593+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.564+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.448+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.433+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.429+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.422+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.417+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:53.412+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:54.993+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:55.107+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:55.074+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:55.058+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:03:55.016+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:03:57.332+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:03:57.309+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:03:57.293+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:03:57.287+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:03:57.285+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.763+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.753+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.743+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.733+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.722+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.709+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.699+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.688+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.681+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.674+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.667+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.661+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.654+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:01.646+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:04.923+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:04.908+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:05.967+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:05.416+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:05.408+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:05.045+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:04:05.003+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:05:10.583+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:05:10.574+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-05-31T23:05:11.140+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:13.970+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:13.957+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:14.776+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:16.539+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:16.534+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:16.530+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:17.255+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:17.254+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:17.233+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:17.231+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:17.225+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:17.220+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:17.213+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:05:18.724+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:05:18.722+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:06:25.568+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:06:25.566+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:06:28.070+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:06:28.067+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-05-31T23:06:53.580+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-05-31T23:06:53.578+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208095 | oper-state-change      | 2023-06-06T12:04:52.574+02:00 | Last session reset by us,                | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | major:Holdtimer Expired minor:None       |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:04:52.565+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Closing                               |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208056 | oper-state-change      | 2023-06-06T12:04:57.573+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:04:57.571+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208095 | oper-state-change      | 2023-06-06T12:05:29.939+02:00 | Last session reset by us,                | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | major:Holdtimer Expired minor:None       |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:05:29.932+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Closing                               |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208056 | oper-state-change      | 2023-06-06T12:05:34.958+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:05:34.957+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208095 | oper-state-change      | 2023-06-06T12:05:39.517+02:00 | Last session reset by us,                | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | major:Holdtimer Expired minor:None       |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:05:39.510+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Closing                               |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208056 | oper-state-change      | 2023-06-06T12:05:44.517+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-06T12:05:44.516+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.573+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.536+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.247+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.241+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.082+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:41.077+02:00 | BGP domain operational state is changed  | SPIN_InnoLab:SPIN_RDC3_VRF     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:43.554+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:43.544+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.437+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.386+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.264+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.229+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.214+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:43.207+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:48.799+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:48.783+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:50.654+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:50.645+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:51.577+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:51.564+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:51.525+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:51.520+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:52.978+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:52.773+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:52.765+02:00 | BGP domain operational state is changed  | mgmt:EU-SPDC-ERSPAN-VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:52.223+02:00 | BGP domain operational state is changed  | UC3-CL2023-Demo:default        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:52.173+02:00 | BGP domain operational state is changed  | management                     | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:53.763+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:53.754+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:53.553+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:53.188+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:53.176+02:00 | BGP domain operational state is changed  | common:Infra_BGP_VRF           | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:54.527+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:36:54.519+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:54.298+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:36:54.243+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:36:55.594+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:55.591+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:36:55.315+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.228/32 | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:36:55.286+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:36:55.282+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.16.11.1/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:55.203+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:36:56.021+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:02.957+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:03.160+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:03.089+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.835+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.827+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.821+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.813+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.806+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.798+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.790+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.781+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.776+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.772+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.767+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.762+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.757+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:06.752+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:06.350+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:06.335+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:37:06.321+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.441+02:00 | BGP domain operational state is changed  | ECMP-demo:MPC-RDC-3_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.437+02:00 | BGP domain operational state is changed  | common:Infra_privIP_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.433+02:00 | BGP domain operational state is changed  | mgmt:inb                       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.430+02:00 | BGP domain operational state is changed  | SPN_IntraLab:SPN_VRF1          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.072+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-OUT_VRF             | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.067+02:00 | BGP domain operational state is changed  | MPC-F5T:F5-IN_VRF              | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-06-12T10:37:09.046+02:00 | BGP domain operational state is changed  | ECMP-demo:INT-ext_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:38:12.994+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:38:12.992+02:00 | BGP peer operational state is changed    | overlay-1                      | 15.16.3.1/32     | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T10:38:22.365+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T10:38:22.363+02:00 | BGP peer operational state is changed    | overlay-1                      | 172.31.3.35/32   | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-06-12T16:29:45.115+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-06-12T16:29:45.113+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:29:10.996+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:29:10.895+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:29:10.867+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:49:54.611+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:49:54.521+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T15:49:54.473+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:45:13.502+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:45:13.390+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:45:13.292+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.682+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.583+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.573+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.562+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.556+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.539+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.529+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:51:28.518+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.336+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.255+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.233+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:28.226+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:31.379+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:31.316+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-10T16:51:31.286+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-07-10T16:54:03.668+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-10T16:54:03.656+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-13T13:05:59.373+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-13T13:05:59.272+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-13T13:05:59.255+02:00 | BGP domain operational state is changed  | MPC:MPC-sPBR-IN_VRF            | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:17.692+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:17.556+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:17.538+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.764+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.723+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.718+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.712+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.703+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.697+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.689+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:54:45.679+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.489+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.475+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.460+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T11:54:45.455+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-07-14T11:58:46.234+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T11:58:46.232+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:04:09.635+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Closing                               |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:00.837+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:00.755+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:00.714+02:00 | BGP domain operational state is changed  | MPC-E:MPC-Residential-R3DC_VRF | --               | 
|                     |      |          |                        |                               | to Down                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.845+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.823+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.803+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.783+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.759+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:29:01.749+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Idle                                  |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:01.742+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:01.631+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:01.620+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-OUT_VRF       | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:03.678+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:03.555+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T12:29:03.540+02:00 | BGP domain operational state is changed  | MPC-E:MPC-E-sPBR-IN_VRF        | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-07-14T12:31:41.733+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:31:41.730+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.1/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-07-14T12:31:53.736+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:31:53.733+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.3/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208093 | oper-state-established | 2023-07-14T12:32:01.736+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208055 | oper-state-change      | 2023-07-14T12:32:01.734+02:00 | BGP peer operational state is changed    | MPC-E:MPC-E-sPBR-OUT_VRF       | 172.24.3.2/32    | 
|                     |      |          |                        |                               | to Established                           |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T15:14:38.260+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T15:14:38.174+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
| pod-1/rl301-eu-spdc | Info | E4208053 | oper-state-change      | 2023-07-14T15:14:38.147+02:00 | BGP domain operational state is changed  | MPC-E:CU-DU-Infra_VRF          | --               | 
|                     |      |          |                        |                               | to Up                                    |                                |                  | 
+---------------------+------+----------+------------------------+-------------------------------+------------------------------------------+--------------------------------+------------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view diag --when 90d

{
    "duration": 4061,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 390,
        "disconnect_time": 0,
        "mo_time": 1877,
        "total_time": 2267
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

True	390	-	connect apic11o.emea-sp.cisco.com:443
True	302	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	284	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query rsp-subtree-include=faults,no-scoped,subtree
True	665	411	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	626	815	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolBgp.md)