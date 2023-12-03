# Intersight Server

## Get servers in group

```
# iserver get server --group self-test

iaccount isctl (cache: off)
Select servers...
Selected servers: 2
Collect server api objects...


Server Summary [#2]
-------------------

+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name                           | Tag         | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | comp-1-p2b-eu-spdc-WZP23400AJW | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AJW | 10.58.50.41 | 2S 40C 80T | 384 [GiB] | 
| P+ H | CRi | comp-2-p2b-eu-spdc-WZP23400AK4 | psirt:ready | (R) UCSC-C240-M5SN | WZP23400AK4 | 10.58.50.42 | 2S 40C 80T | 384 [GiB] | 
+------+-----+--------------------------------+-------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```
