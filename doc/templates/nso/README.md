# Network Services Orchestrator

Uses REST API calls to provide the state and control on NSO instances.

## Features

- [Device](./Device.md)
- [NFVO CFP](./NfvoCfp.md)
- [CNFO CFP](./CnfoCfp.md)

## API authentication

iserver interacts with NSO using REST API. API endpoint and authentication details must be configured.

```
$ iserver set nso ncs --name kali --ip 10.58.28.207 --username admin --password admin
NCS authentication successful
NCS entry created: kali
```

Multiple ncs named instances are supported.

```
$ iserver get nso ncs

+------------+---------------+--------------+------+----------+----------+----------+----------+
| Name       | REST Protocol | IP           | Port | Username | Password | RESTCONF | NFVO     |
+------------+---------------+--------------+------+----------+----------+----------+----------+
| cvim-pod4a | http          | 10.58.51.131 | 8080 | admin    | ******   | True     | etsi:4.x |
| kali       | http          | 10.58.28.207 | 8080 | admin    | ******   | True     | None     |
| vimercate  | http          | 10.58.28.230 | 8080 | admin    | ******   | True     | None     |
+------------+---------------+--------------+------+----------+----------+----------+----------+
```

The pre-configured ncs name can be passed on every command run. Last used ncs name becomes default one.

```
$ iserver get nso device --ncs vimercate
NCS: vimercate

Device [#14]
------------

+------------------------+--------------------------------+------------+--------+-------------------------------+----------+
| Name                   | Address                        | AuthGroup  | Type   | NED                           | State    |
+------------------------+--------------------------------+------------+--------+-------------------------------+----------+
| APIC_MILAN0            | apic21o-eu-spdc.cisco.com:None | APIC_MILAN | APIC   | generic:cisco-apicdc-gen-3.19 | unlocked |
| Berlin                 | berlin.emea-sp.cisco.com:None  | berlin     | IOS-XR | cli:cisco-iosxr-cli-7.52      | unlocked |
| cat8-tpo               | 10.58.29.84:30003              | vnf        | IOS-XE | cli:cisco-ios-cli-6.99        | unlocked |
| cat8k0                 | 127.0.0.1:10022                | default    | IOS-XE | cli:cisco-ios-cli-6.99        | unlocked |
| cat8k1                 | 127.0.0.1:10023                | default    | IOS-XE | cli:cisco-ios-cli-6.99        | unlocked |
| cat8kv-17.09.04-eugene | 10.62.189.118:22               | milan      | IOS-XE | cli:cisco-ios-cli-6.99        | unlocked |
| cnfm-bm2-kc            | 10.58.29.83:31318              | cnfm       | CNFM   | netconf:cnfm-nc-1.2           | unlocked |
| cnfm-bm2-sa            | 10.58.29.83:30780              | cnfm       | CNFM   | netconf:cnfm-nc-1.2           | unlocked |
| cnfm-sa-role-2         | 10.58.29.84:31555              | default    | CNFM   | netconf:cnfm-nc-1.2           | unlocked |
| cnfm-tpo               | 10.58.29.84:30835              | cnfm       | CNFM   | netconf:cnfm-nc-1.2           | unlocked |
| junos-0                | 127.0.0.1:12024                | default    | Junos  | netconf:juniper-junos-nc-4.14 | unlocked |
| junos-1                | 127.0.0.1:12025                | default    | Junos  | netconf:juniper-junos-nc-4.14 | unlocked |
| xr0                    | 127.0.0.1:10022                | default    | IOS-XR | cli:cisco-iosxr-cli-7.52      | unlocked |
| xrv                    | 10.50.16.161:None              | xrv        | IOS-XR | cli:cisco-iosxr-cli-7.52      | unlocked |
+------------------------+--------------------------------+------------+--------+-------------------------------+----------+
```

[[Back]](../../README.md)