# Node Protocol - ARP

## Diag view

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view diag
    --when 90d

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

BFD Event Logs last 90d [#116]
------------------------------

+---------------------+------------+----------+----------+-------------------+-------------------------------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code     | Cause             | Created Time                  | Description                                                                      |
+---------------------+------------+----------+----------+-------------------+-------------------------------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-05-31T23:11:25.702+02:00 | BFD session to neighbor 15.100.7.41 on interface vlan494 has been created        | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-05-31T23:11:25.705+02:00 | Active parameter of BFD session 1090519041 has changed Disc 1090519041           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:25.706+02:00 | Local parameter of BFD session 1090519041 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:25.707+02:00 | BFD session 1090519041 to neighbor 15.100.7.41 on interface vlan494 is down.     | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                           | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-05-31T23:11:25.712+02:00 | BFD session to neighbor 15.100.7.41 on interface vlan494 has been created        | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-05-31T23:11:25.715+02:00 | Active parameter of BFD session 1090519041 has changed Disc 1090519041           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:25.716+02:00 | Local parameter of BFD session 1090519041 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:25.717+02:00 | BFD session 1090519041 to neighbor 15.100.7.41 on interface vlan494 is down.     | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                           | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-05-31T23:11:26.041+02:00 | Local parameter of BFD session 1090519041 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4215661 | oper-state-change | 2023-05-31T23:11:26.051+02:00 | BFD session 1090519041 to neighbor 15.100.7.41 on interface vlan494 is down.     | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                           | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:16.592+02:00 | BFD session to neighbor 15.254.106.191 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:16.596+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:16.605+02:00 | BFD session to neighbor 15.254.106.191 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:16.610+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.652+02:00 | BFD session to neighbor 15.254.106.192 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.655+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.667+02:00 | BFD session to neighbor 15.254.106.192 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.670+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.640+02:00 | BFD session to neighbor 15.254.103.192 on interface vlan498 has been created     | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.642+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:19.673+02:00 | BFD session to neighbor 15.254.103.192 on interface vlan498 has been created     | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:19.676+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:22.791+02:00 | BFD session to neighbor 15.254.103.191 on interface vlan498 has been created     | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:22.795+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-05-31T23:12:22.811+02:00 | BFD session to neighbor 15.254.103.191 on interface vlan498 has been created     | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:22.815+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:28.611+02:00 | Local parameter of BFD session 1090519042 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:29.502+02:00 | BFD session 1090519042 to neighbor 15.254.106.191 on interface vlan496 is up.    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:30.590+02:00 | Local parameter of BFD session 1090519042 has changed TX(50): RX(50): ST(0),     | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.156+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.157+02:00 | Local parameter of BFD session 1090519044 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:31.169+02:00 | BFD session 1090519044 to neighbor 15.254.106.192 on interface vlan496 is up.    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.632+02:00 | Local parameter of BFD session 1090519044 has changed TX(50): RX(50): ST(2000),  | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.149+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.150+02:00 | Local parameter of BFD session 1090519042 has changed TX(50): RX(50): ST(2000),  | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.625+02:00 | Local parameter of BFD session 1090519043 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:31.163+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:31.164+02:00 | Local parameter of BFD session 1090519043 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:31.176+02:00 | BFD session 1090519043 to neighbor 15.254.103.192 on interface vlan498 is up.    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:35.626+02:00 | Local parameter of BFD session 1090519045 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208501 | oper-state-change | 2023-05-31T23:12:36.729+02:00 | BFD session 1090519045 to neighbor 15.254.103.191 on interface vlan498 is up.    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:37.626+02:00 | Local parameter of BFD session 1090519045 has changed TX(500): RX(500): ST(0),   | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-05-31T23:12:38.379+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-05-31T23:12:38.380+02:00 | Local parameter of BFD session 1090519045 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-06-07T11:38:45.783+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3), Ver(1)                                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4215661 | oper-state-change | 2023-06-07T11:38:45.785+02:00 | BFD session 1090519045 to neighbor 15.254.103.191 on interface vlan498 is down.  | 
|                     |            |          |          |                   |                               | Reason: Control Detection Time Expired.                                          | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4215661 | oper-state-change | 2023-06-07T11:38:45.833+02:00 | BFD session 1090519042 to neighbor 15.254.106.191 on interface vlan496 is down.  | 
|                     |            |          |          |                   |                               | Reason: Control Detection Time Expired.                                          | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-06-07T11:38:45.831+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3), Ver(1)                                    | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-06-07T11:38:46.232+02:00 | Local parameter of BFD session 1090519045 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-06-07T11:38:46.240+02:00 | Local parameter of BFD session 1090519042 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208500 | oper-state-change | 2023-06-07T11:38:48.252+02:00 | BFD session to neighbor has been removed                                         | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208500 | oper-state-change | 2023-06-07T11:38:48.262+02:00 | BFD session to neighbor has been removed                                         | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-06-07T11:39:19.730+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3), Ver(1)                                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4215661 | oper-state-change | 2023-06-07T11:39:19.732+02:00 | BFD session 1090519044 to neighbor 15.254.106.192 on interface vlan496 is down.  | 
|                     |            |          |          |                   |                               | Reason: Control Detection Time Expired.                                          | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-06-07T11:39:19.645+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(2000), Mult(3), Ver(1)                                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4215661 | oper-state-change | 2023-06-07T11:39:19.646+02:00 | BFD session 1090519043 to neighbor 15.254.103.192 on interface vlan498 is down.  | 
|                     |            |          |          |                   |                               | Reason: Control Detection Time Expired.                                          | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-06-07T11:39:20.245+02:00 | Local parameter of BFD session 1090519044 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-06-07T11:39:20.237+02:00 | Local parameter of BFD session 1090519043 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208500 | oper-state-change | 2023-06-07T11:39:22.262+02:00 | BFD session to neighbor has been removed                                         | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208500 | oper-state-change | 2023-06-07T11:39:22.252+02:00 | BFD session to neighbor has been removed                                         | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208500 | oper-state-change | 2023-06-07T11:40:48.262+02:00 | BFD session to neighbor has been removed                                         | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:03.038+02:00 | BFD session to neighbor 15.254.106.192 on interface vlan492 has been created     | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:03.043+02:00 | Active parameter of BFD session 1090519041 has changed Disc 1090519041           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:03.052+02:00 | BFD session to neighbor 15.254.106.192 on interface vlan492 has been created     | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:03.056+02:00 | Active parameter of BFD session 1090519041 has changed Disc 1090519041           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:05.031+02:00 | BFD session to neighbor 15.254.103.192 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:05.034+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:09.038+02:00 | BFD session to neighbor 15.254.106.191 on interface vlan492 has been created     | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:09.041+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208499 | oper-state-change | 2023-07-05T19:20:11.039+02:00 | BFD session to neighbor 15.254.103.191 on interface vlan496 has been created     | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:11.042+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:18.837+02:00 | Active parameter of BFD session 1090519042 has changed Disc 1090519042 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:18.839+02:00 | Local parameter of BFD session 1090519042 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:18.853+02:00 | BFD session 1090519042 to neighbor 15.254.103.192 on interface vlan496 is up.    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:18.847+02:00 | Active parameter of BFD session 1090519041 has changed Disc 1090519041 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:18.848+02:00 | Local parameter of BFD session 1090519041 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:18.861+02:00 | BFD session 1090519041 to neighbor 15.254.106.192 on interface vlan492 is up.    | 
| pod-1/cl201-eu-spdc | 1090519042 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:19.080+02:00 | Local parameter of BFD session 1090519042 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519041 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:19.057+02:00 | Local parameter of BFD session 1090519041 has changed TX(50): RX(50): ST(2000),  | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:20.857+02:00 | Active parameter of BFD session 1090519043 has changed Disc 1090519043 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:20.858+02:00 | Local parameter of BFD session 1090519043 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:20.864+02:00 | BFD session 1090519043 to neighbor 15.254.106.191 on interface vlan492 is up.    | 
| pod-1/cl201-eu-spdc | 1090519043 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:21.054+02:00 | Local parameter of BFD session 1090519043 has changed TX(50): RX(50): ST(2000),  | 
|                     |            |          |          |                   |                               | Mult(3), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209847 | oper-state-change | 2023-07-05T19:20:22.971+02:00 | Active parameter of BFD session 1090519044 has changed Disc 1090519044 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:22.972+02:00 | Local parameter of BFD session 1090519044 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4208501 | oper-state-change | 2023-07-05T19:20:22.979+02:00 | BFD session 1090519044 to neighbor 15.254.103.191 on interface vlan496 is up.    | 
| pod-1/cl201-eu-spdc | 1090519044 | Info     | E4209848 | oper-state-change | 2023-07-05T19:20:23.054+02:00 | Local parameter of BFD session 1090519044 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4208499 | oper-state-change | 2023-07-05T19:21:04.006+02:00 | BFD session to neighbor 15.100.7.41 on interface vlan472 has been created        | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209847 | oper-state-change | 2023-07-05T19:21:04.009+02:00 | Active parameter of BFD session 1090519045 has changed Disc 1090519045           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4209848 | oper-state-change | 2023-07-05T19:21:17.054+02:00 | Local parameter of BFD session 1090519045 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519045 | Info     | E4215661 | oper-state-change | 2023-07-05T19:21:23.058+02:00 | BFD session 1090519045 to neighbor 15.100.7.41 on interface vlan472 is down.     | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                           | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4208499 | oper-state-change | 2023-07-07T14:56:57.147+02:00 | BFD session to neighbor 15.100.103.41 on interface vlan471 has been created      | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4209847 | oper-state-change | 2023-07-07T14:56:57.150+02:00 | Active parameter of BFD session 1090519046 has changed Disc 1090519046           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:10.420+02:00 | Local parameter of BFD session 1090519046 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519046 | Info     | E4215661 | oper-state-change | 2023-07-07T14:57:16.424+02:00 | BFD session 1090519046 to neighbor 15.100.103.41 on interface vlan471 is down.   | 
|                     |            |          |          |                   |                               | Reason: No Diagnostic.                                                           | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4208499 | oper-state-change | 2023-07-07T14:57:19.188+02:00 | BFD session to neighbor 15.254.133.55 on interface vlan473 has been created      | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209847 | oper-state-change | 2023-07-07T14:57:19.197+02:00 | Active parameter of BFD session 1090519047 has changed Disc 1090519047           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:32.416+02:00 | Local parameter of BFD session 1090519047 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(0), Mult(3), Ver(1), Auth Type(No authentication)                             | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4208501 | oper-state-change | 2023-07-07T14:57:32.473+02:00 | BFD session 1090519047 to neighbor 15.254.133.55 on interface vlan473 is up.     | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209847 | oper-state-change | 2023-07-07T14:57:34.349+02:00 | Active parameter of BFD session 1090519047 has changed Disc 1090519047 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:34.351+02:00 | Local parameter of BFD session 1090519047 has changed TX(2000): RX(2000):        | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519047 | Info     | E4209848 | oper-state-change | 2023-07-07T14:57:34.416+02:00 | Local parameter of BFD session 1090519047 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:35.262+02:00 | BFD session to neighbor 15.254.133.191 on interface vlan473 has been created     | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:35.265+02:00 | Active parameter of BFD session 1090519048 has changed Disc 1090519048           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:35.271+02:00 | BFD session to neighbor 15.254.133.191 on interface vlan473 has been created     | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:35.274+02:00 | Active parameter of BFD session 1090519048 has changed Disc 1090519048           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:47.822+02:00 | Active parameter of BFD session 1090519048 has changed Disc 1090519048 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209848 | oper-state-change | 2023-07-07T14:58:47.824+02:00 | Local parameter of BFD session 1090519048 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4208501 | oper-state-change | 2023-07-07T14:58:47.830+02:00 | BFD session 1090519048 to neighbor 15.254.133.191 on interface vlan473 is up.    | 
| pod-1/cl201-eu-spdc | 1090519048 | Info     | E4209848 | oper-state-change | 2023-07-07T14:58:48.351+02:00 | Local parameter of BFD session 1090519048 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4208499 | oper-state-change | 2023-07-07T14:58:53.263+02:00 | BFD session to neighbor 15.254.133.193 on interface vlan473 has been created     | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209847 | oper-state-change | 2023-07-07T14:58:53.266+02:00 | Active parameter of BFD session 1090519049 has changed Disc 1090519049           | 
|                     |            |          |          |                   |                               | TX(2000): RX(2000): ST(0), Mult(3), Ver(1)                                       | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209847 | oper-state-change | 2023-07-07T14:59:05.220+02:00 | Active parameter of BFD session 1090519049 has changed Disc 1090519049 TX(500):  | 
|                     |            |          |          |                   |                               | RX(500): ST(2000), Mult(3), Ver(1)                                               | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209848 | oper-state-change | 2023-07-07T14:59:05.222+02:00 | Local parameter of BFD session 1090519049 has changed TX(0): RX(0): ST(2000),    | 
|                     |            |          |          |                   |                               | Mult(0), Ver(1), Auth Type(No authentication)                                    | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4208501 | oper-state-change | 2023-07-07T14:59:05.228+02:00 | BFD session 1090519049 to neighbor 15.254.133.193 on interface vlan473 is up.    | 
| pod-1/cl201-eu-spdc | 1090519049 | Info     | E4209848 | oper-state-change | 2023-07-07T14:59:06.352+02:00 | Local parameter of BFD session 1090519049 has changed TX(500): RX(500):          | 
|                     |            |          |          |                   |                               | ST(2000), Mult(3), Ver(1), Auth Type(No authentication)                          | 
+---------------------+------------+----------+----------+-------------------+-------------------------------+----------------------------------------------------------------------------------+

BFD Faults [#2]
---------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.050+02:00 | raised    | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |           | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.415+02:00 | raised    | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |           | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+-----------+----------------------------------------------------------------------------------+

BFD Fault Records last 90d [#20]
--------------------------------

+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| Node                | Session Id | Severity | Code  | Cause                       | Created Time                  | Lifecycle        | Description                                                                      |
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-05-31T23:11:25.700+02:00 | soaking          | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-05-31T23:13:32.882+02:00 | raised           | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:45.779+02:00 | soaking          | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:45.827+02:00 | soaking          | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:46.762+02:00 | soaking-clearing | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:46.772+02:00 | soaking-clearing | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:48.248+02:00 |                  | BFD session 1090519045 to neighbor 15.254.103.191 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519042 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:38:48.259+02:00 |                  | BFD session 1090519042 to neighbor 15.254.106.191 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:19.725+02:00 | soaking          | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:19.640+02:00 | soaking          | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:20.542+02:00 | soaking-clearing | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:20.532+02:00 | soaking-clearing | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519044 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:22.259+02:00 |                  | BFD session 1090519044 to neighbor 15.254.106.192 on node 201 interface vlan496  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519043 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:39:22.248+02:00 |                  | BFD session 1090519043 to neighbor 15.254.103.192 on node 201 interface vlan498  | 
|                     |            |          |       |                             |                               |                  | is down. Reason: Control Detection Time Expired.                                 | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.057+02:00 | raised-clearing  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519041 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-06-07T11:40:48.258+02:00 |                  | BFD session 1090519041 to neighbor 15.100.7.41 on node 201 interface vlan494 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:21:23.051+02:00 | soaking          | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519045 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-05T19:23:34.715+02:00 | raised           | BFD session 1090519045 to neighbor 15.100.7.41 on node 201 interface vlan472 is  | 
|                     |            |          |       |                             |                               |                  | down. Reason: No Diagnostic.                                                     | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:57:16.417+02:00 | soaking          | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |                  | is down. Reason: No Diagnostic.                                                  | 
| pod-1/cl201-eu-spdc | 1090519046 | Maj      | F1483 | protocol-bfd-adjacency-down | 2023-07-07T14:59:36.715+02:00 | raised           | BFD session 1090519046 to neighbor 15.100.103.41 on node 201 interface vlan471   | 
|                     |            |          |       |                             |                               |                  | is down. Reason: No Diagnostic.                                                  | 
+---------------------+------------+----------+-------+-----------------------------+-------------------------------+------------------+----------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci proto bfd
    --apic apic11
    --node cl201-eu-spdc
    --view diag
    --when 90d

{
    "duration": 10937,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 427,
        "disconnect_time": 0,
        "mo_time": 4724,
        "total_time": 5151
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

True	427	-	connect apic11o.emea-sp.cisco.com:443
True	380	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	423	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	362	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	1967	2215	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=faults,fault-records,no-scoped,subtree
True	1592	4050	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=event-logs,no-scoped,subtree
```

[[Back]](./ProtocolBfd.md)