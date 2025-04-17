# Intersight Server

## mem view

```
# iserver get server --group test -v mem

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Memory [#108]
-------------

+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server    | Oper     | Presence | Id | Array | Bank | Location   | Capacity | Clock | Form Factor | Type | Model    | Serial |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+
| Server132 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-39 | SN-66  |
| Server132 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-79 | SN-32  |
| Server132 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-32 | SN-41  |
| Server132 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-84 | SN-98  |
| Server132 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-62 | SN-29  |
| Server132 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-47 | SN-58  |
| Server132 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-78 | SN-88  |
| Server132 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-69 | SN-71  |
| Server132 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-35 | SN-70  |
| Server132 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-89 | SN-76  |
| Server132 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-48 | SN-40  |
| Server132 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-63 | SN-67  |
| Server106 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-68 | SN-69  |
| Server106 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-92 | SN-97  |
| Server106 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-57 | SN-57  |
| Server106 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-36 | SN-54  |
| Server106 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-52 | SN-50  |
| Server106 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-85 | SN-49  |
| Server106 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-12 | SN-19  |
| Server106 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-47 | SN-65  |
| Server106 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-81 | SN-64  |
| Server106 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-73 | SN-85  |
| Server106 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-85 | SN-67  |
| Server106 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-69 | SN-50  |
| Server802 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-26 | SN-40  |
| Server802 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-68 | SN-58  |
| Server802 | operable | equipped | 5  | 1     | 0    | DIMM_C1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-29 | SN-89  |
| Server802 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-15 | SN-48  |
| Server802 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-20 | SN-98  |
| Server802 | operable | equipped | 11 | 1     | 0    | DIMM_F1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-96 | SN-27  |
| Server802 | operable | equipped | 13 | 1     | 0    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-58 | SN-66  |
| Server802 | operable | equipped | 15 | 1     | 0    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-32 | SN-28  |
| Server802 | operable | equipped | 17 | 1     | 0    | DIMM_J1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-92 | SN-35  |
| Server802 | operable | equipped | 19 | 1     | 0    | DIMM_K1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-77 | SN-51  |
| Server802 | operable | equipped | 21 | 1     | 0    | DIMM_L1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-67 | SN-74  |
| Server802 | operable | equipped | 23 | 1     | 0    | DIMM_M1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-53 | SN-28  |
| Server277 | operable | equipped | 2  | 1     | 0    | DIMM_P1_A2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-78 | SN-32  |
| Server277 | operable | equipped | 4  | 1     | 0    | DIMM_P1_B2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-85  |
| Server277 | operable | equipped | 6  | 1     | 0    | DIMM_P1_C2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-87 | SN-37  |
| Server277 | operable | equipped | 8  | 1     | 0    | DIMM_P1_D2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-14 | SN-12  |
| Server277 | operable | equipped | 10 | 1     | 0    | DIMM_P1_E2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-21 | SN-20  |
| Server277 | operable | equipped | 12 | 1     | 0    | DIMM_P1_F2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-13 | SN-11  |
| Server277 | operable | equipped | 14 | 1     | 0    | DIMM_P1_G2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-28 | SN-98  |
| Server277 | operable | equipped | 16 | 1     | 0    | DIMM_P1_H2 | 64 [GiB] | 3200  | DIMM        | DDR4 | Model-44 | SN-45  |
| Server819 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-21 | SN-63  |
| Server819 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-10 | SN-30  |
| Server819 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-49 | SN-20  |
| Server819 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-54 | SN-77  |
| Server819 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-64 | SN-79  |
| Server819 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-61 | SN-62  |
| Server819 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-42 | SN-58  |
| Server819 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-38 | SN-99  |
| Server819 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-10 | SN-58  |
| Server819 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-89 | SN-84  |
| Server819 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-49 | SN-54  |
| Server819 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-50 | SN-26  |
| Server819 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-47 | SN-31  |
| Server819 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-31 | SN-71  |
| Server819 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-95 | SN-46  |
| Server819 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-24 | SN-38  |
| Server142 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-59 | SN-30  |
| Server142 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-68 | SN-62  |
| Server142 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-78 | SN-47  |
| Server142 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-53 | SN-39  |
| Server142 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-56 | SN-47  |
| Server142 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-59 | SN-40  |
| Server142 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-51 | SN-32  |
| Server142 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-71 | SN-24  |
| Server142 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-76 | SN-85  |
| Server142 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-54 | SN-44  |
| Server142 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-33 | SN-95  |
| Server142 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-49 | SN-24  |
| Server142 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-79 | SN-53  |
| Server142 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-76 | SN-38  |
| Server142 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-38 | SN-90  |
| Server142 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-86 | SN-60  |
| Server360 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-37 | SN-15  |
| Server360 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-55 | SN-93  |
| Server360 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-33 | SN-64  |
| Server360 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-51 | SN-99  |
| Server360 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-37 | SN-95  |
| Server360 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-48 | SN-71  |
| Server360 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-99 | SN-82  |
| Server360 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-92 | SN-77  |
| Server360 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-82 | SN-25  |
| Server360 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-84 | SN-23  |
| Server360 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-25 | SN-78  |
| Server360 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-25 | SN-21  |
| Server360 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-24 | SN-57  |
| Server360 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-26 | SN-86  |
| Server360 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-38 | SN-39  |
| Server360 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-49 | SN-83  |
| Server281 | operable | equipped | 1  | 1     | 0    | DIMM_A1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-63 | SN-18  |
| Server281 | operable | equipped | 2  | 1     | 0    | DIMM_A2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-94 | SN-42  |
| Server281 | operable | equipped | 3  | 1     | 0    | DIMM_B1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-69 | SN-43  |
| Server281 | operable | equipped | 4  | 1     | 0    | DIMM_B2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-41 | SN-15  |
| Server281 | operable | equipped | 7  | 1     | 0    | DIMM_D1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-50 | SN-78  |
| Server281 | operable | equipped | 8  | 1     | 0    | DIMM_D2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-93 | SN-20  |
| Server281 | operable | equipped | 9  | 1     | 0    | DIMM_E1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-81 | SN-22  |
| Server281 | operable | equipped | 10 | 1     | 0    | DIMM_E2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-92 | SN-78  |
| Server281 | operable | equipped | 13 | 1     | 1    | DIMM_G1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-64 | SN-76  |
| Server281 | operable | equipped | 14 | 1     | 1    | DIMM_G2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-95 | SN-62  |
| Server281 | operable | equipped | 15 | 1     | 1    | DIMM_H1    | 32 [GiB] | 2933  | DIMM        | DDR4 | Model-82 | SN-34  |
| Server281 | operable | equipped | 16 | 1     | 1    | DIMM_H2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-95 | SN-56  |
| Server281 | operable | equipped | 19 | 1     | 1    | DIMM_K1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-89 | SN-77  |
| Server281 | operable | equipped | 20 | 1     | 1    | DIMM_K2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-77 | SN-65  |
| Server281 | operable | equipped | 21 | 1     | 1    | DIMM_L1    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-88 | SN-51  |
| Server281 | operable | equipped | 22 | 1     | 1    | DIMM_L2    | 32 [GiB] | 2666  | DIMM        | DDR4 | Model-97 | SN-69  |
+-----------+----------+----------+----+-------+------+------------+----------+-------+-------------+------+----------+--------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)