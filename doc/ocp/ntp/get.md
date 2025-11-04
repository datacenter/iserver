# Network Time Protocol (NTP) - Get

## Workflow

- get chrony machine config (/etc/chrony.conf)
- get actual machine chrony config from every cluster node
- get chrony state on every cluster node

## Example

```
# iserver get ocp ntp --cluster bm1

OpenShift Workflow - Get ntp configuration and state
====================================================

OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Collecting data...


Chrony Machine Configuration
----------------------------

Machine config: 50-masters-chrony-configuration
Node: bm1-1, bm1-2, bm1-3
Path: /etc/chrony.conf
~~~

pool 0.rhel.pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
logdir /var/log/chrony
server mail.roundowl.tk iburst
server excalibur.prolixium.com iburst
server dns02.wsrs.net iburst
server ntp.emenders.nl iburst
server 86-80-166-233.fixed.kpn.net iburst
server ams.gw iburst
server 62.204.66.235 iburst
server connected.by.freedominter.net iburst
server ntp.domain.com iburst
server 172-233-38-176.ip.linodeusercontent.com iburst
server 244792.fornex.cloud iburst
server time1.panq.nl iburst
server 145-53-74-170.fixed.kpn.net iburst
server leontp3.office.panq.nl iburst
server cloud.74.158.71.206.macarne.com iburst
server host-h.in-w1d1-a.v4.dfn.nl iburst
server ntp01.pingless.com iburst
server 45.9.2.181 iburst
server ntp01.cobytes.io iburst
server leontp1.office.panq.nl iburst
server 193.123.56.220 iburst
server arethusa.tweakers.net iburst
~~~

Machine config: 50-workers-chrony-configuration
Node: bm1-1, bm1-2, bm1-3
Path: /etc/chrony.conf
~~~

pool 0.rhel.pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
logdir /var/log/chrony
server mail.roundowl.tk iburst
server excalibur.prolixium.com iburst
server dns02.wsrs.net iburst
server ntp.emenders.nl iburst
server 86-80-166-233.fixed.kpn.net iburst
server ams.gw iburst
server 62.204.66.235 iburst
server connected.by.freedominter.net iburst
server ntp.domain.com iburst
server 172-233-38-176.ip.linodeusercontent.com iburst
server 244792.fornex.cloud iburst
server time1.panq.nl iburst
server 145-53-74-170.fixed.kpn.net iburst
server leontp3.office.panq.nl iburst
server cloud.74.158.71.206.macarne.com iburst
server host-h.in-w1d1-a.v4.dfn.nl iburst
server ntp01.pingless.com iburst
server 45.9.2.181 iburst
server ntp01.cobytes.io iburst
server leontp1.office.panq.nl iburst
server 193.123.56.220 iburst
server arethusa.tweakers.net iburst
~~~

Chrony Configuration
--------------------

Configuration the same on all nodes

~~~

pool 0.rhel.pool.ntp.org iburst
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
logdir /var/log/chrony
server mail.roundowl.tk iburst
server excalibur.prolixium.com iburst
server dns02.wsrs.net iburst
server ntp.emenders.nl iburst
server 86-80-166-233.fixed.kpn.net iburst
server ams.gw iburst
server 62.204.66.235 iburst
server connected.by.freedominter.net iburst
server ntp.domain.com iburst
server 172-233-38-176.ip.linodeusercontent.com iburst
server 244792.fornex.cloud iburst
server time1.panq.nl iburst
server 145-53-74-170.fixed.kpn.net iburst
server leontp3.office.panq.nl iburst
server cloud.74.158.71.206.macarne.com iburst
server host-h.in-w1d1-a.v4.dfn.nl iburst
server ntp01.pingless.com iburst
server 45.9.2.181 iburst
server ntp01.cobytes.io iburst
server leontp1.office.panq.nl iburst
server 193.123.56.220 iburst
server arethusa.tweakers.net iburst
~~~

+-------+--------+------------------------------+---------+---------------+---------------------+
| Node  | Status | Reference                    | Stratum | Time          | Delay               |
+-------+--------+------------------------------+---------+---------------+---------------------+
| bm1-1 | Normal | ReferenceId (ntp.domain.com) | 2       | Sat Oct 25 10 | 0.026142275 seconds |
+-------+--------+------------------------------+---------+---------------+---------------------+
| bm1-2 | Normal | ReferenceId (ntp.domain.com) | 2       | Sat Oct 25 10 | 0.026739482 seconds |
+-------+--------+------------------------------+---------+---------------+---------------------+
| bm1-3 | Normal | ReferenceId (ntp.domain.com) | 2       | Sat Oct 25 10 | 0.026882902 seconds |
+-------+--------+------------------------------+---------+---------------+---------------------+
```

[[Back]](./README.md)