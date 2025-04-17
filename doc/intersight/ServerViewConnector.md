# Intersight Server

## connector view

```
# iserver get server
    --group test -v connector
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Connector [#8]
--------------

+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server    | Connection Status | Connector Version | Claimed By      | Claimed Time             | Connection Status Last Update | Platform Type | Device External IP Address |
+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server817 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.166.98.200              | 
| Server637 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.165.1.80                | 
| Server173 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.84.111.155              | 
| Server367 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCRack       | 66.2.168.104               | 
| Server932 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.231.190.34              | 
| Server732 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.71.233.151              | 
| Server578 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.62.98.236               | 
| Server439 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.200.146.151             | 
+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)