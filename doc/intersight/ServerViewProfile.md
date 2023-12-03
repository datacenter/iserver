# Intersight Server

## profile view

```
# iserver get server --group test -v profile

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Profile [#1]
------------

+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+
| Server                        | Profile   | State      | Last Modified            | Target Platform | Policy Name                        | Class Id                   | Modification Time        | Shared | In Sync |
+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+
| comp3-p4b-eu-spdc-WZP262207UM | amd-esx83 | Associated | 2023-12-03T00:29:52.359Z | Standalone      | MLOM-and-VIC-1-Infra               | vnic.LanConnectivityPolicy | 2023-11-03T18:48:32.289Z | True   | True    | 
|                               |           |            |                          |                 | UCS-MLOM-VIC1-no-LLDP-no-PC-no-FIP | adapter.ConfigPolicy       | 2023-11-03T18:47:16.719Z | True   | True    | 
|                               |           |            |                          |                 | KVM-Mapped-DVD-then-M2             | boot.PrecisionPolicy       | 2023-11-03T16:29:50.332Z | True   | True    | 
|                               |           |            |                          |                 | dns-emea-sp-config                 | networkconfig.Policy       | 2023-11-03T15:43:50.975Z | True   | True    | 
|                               |           |            |                          |                 | comp-smtp-policy                   | smtp.Policy                | 2023-11-02T15:08:15.565Z | True   | True    | 
|                               |           |            |                          |                 | ipmi-and-sol-allowed               | deviceconnector.Policy     | 2023-11-02T15:08:15.562Z | True   | True    | 
|                               |           |            |                          |                 | ssh-enabled                        | ssh.Policy                 | 2023-11-02T15:08:15.557Z | True   | True    | 
|                               |           |            |                          |                 | emea-sp-syslogs                    | syslog.Policy              | 2023-11-02T15:08:15.551Z | True   | True    | 
|                               |           |            |                          |                 | default-local-user                 | iam.EndPointUserPolicy     | 2023-11-02T15:08:15.549Z | True   | True    | 
|                               |           |            |                          |                 | ipmi-over-vlan-enabled             | ipmioverlan.Policy         | 2023-11-02T15:08:15.547Z | True   | True    | 
|                               |           |            |                          |                 | ntp-cisco                          | ntp.Policy                 | 2023-11-02T15:08:15.546Z | True   | True    | 
|                               |           |            |                          |                 | ldap-disabled                      | iam.LdapPolicy             | 2023-11-02T15:08:15.52Z  | True   | True    | 
|                               |           |            |                          |                 | fan-control-balanced               | thermal.Policy             | 2023-11-02T15:08:15.517Z | True   | True    | 
|                               |           |            |                          |                 | M2-MRAID-boot                      | storage.StoragePolicy      | 2023-11-02T15:08:15.515Z | True   | True    | 
|                               |           |            |                          |                 | bios-default-settings              | bios.Policy                | 2023-11-02T15:08:15.515Z | True   | True    | 
|                               |           |            |                          |                 | vKVM-enabled-not-tunneled          | kvm.Policy                 | 2023-11-02T15:08:15.511Z | True   | True    | 
|                               |           |            |                          |                 | c225-firmware-latest               | firmware.Policy            | 2023-11-02T15:08:15.509Z | True   | True    | 
|                               |           |            |                          |                 | sol-enabled-on-com0                | sol.Policy                 | 2023-11-02T15:08:15.508Z | True   | True    | 
|                               |           |            |                          |                 | comp-snmp-policy                   | snmp.Policy                | 2023-11-02T15:08:15.503Z | True   | True    | 
+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v profile

{
    "duration": 16083,
    "isctl": {
        "read": true,
        "calls": 5,
        "success": 5,
        "failed": 0,
        "total_time": 13773
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
        "read": true,
        "lines": 24
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:27:31.817395	True	2846	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:27:33.961911	True	2140	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:27:36.193691	True	2156	12	isctl get compute blade   -o json --top 100
2023-12-03 15:27:39.005451	True	2769	1	isctl get server profile --filter "AssignedServer/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')" --expand "ConfigChangeDetails" -o json --top 100
2023-12-03 15:27:43.185900	True	3862	19	isctl get search searchitem --filter "IndexMotypes eq 'policy.AbstractPolicy' and Profiles/any(a:a/Moid eq '653fc09477696e31016b8e53')"  -o json --top 100
```

[[Back]](./ServerInventory.md)