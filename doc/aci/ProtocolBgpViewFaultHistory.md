# Node Protocol - BGP

## Fault history view

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view hfault --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

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
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --view hfault --when 90d

{
    "duration": 1694,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 971,
        "total_time": 1369
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

True	398	-	connect apic11o.emea-sp.cisco.com:443
True	301	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	670	411	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolBgp.md)