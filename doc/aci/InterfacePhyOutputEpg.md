# Node Interface - Physical

## EPG focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o epg

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------------------------------------------------------+------------------------------+-------------------+
| Node                | Interface | Oper | EPG                                                     | Bridge Domain                | Subnets           |
+---------------------+-----------+------+---------------------------------------------------------+------------------------------+-------------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | CNC_demo/CNC_ANP/CNC_bus                                | CNC_demo/CNC_BD1             | 10.58.24.254/27   | 
|                     |           |      | DT-EPNM/DT-EPNM/Data                                    | DT-EPNM/DT-EPNM-Data_BD      | 10.58.27.126/28   | 
|                     |           |      | DT-EPNM/DT-EPNM/Device                                  | DT-EPNM/DT-EPNM-Device_BD    | 10.58.27.142/28   | 
|                     |           |      | NXOS-HandOff_Test/TEST/EPG1                             | NXOS-HandOff_Test/BD1        | 192.168.1.1/24    | 
|                     |           |      | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | mgmt/EU-SPDC-ERSPAN-BD       | 99.99.99.254/24   | 
|                     |           |      | MPC-F5T/F5_ANP/F5_IN                                    | MPC-F5T/F5-IN_BD             | 15.2.64.254/24    | 
|                     |           |      | MPC-F5T/F5_ANP/F5_OUT                                   | MPC-F5T/F5-OUT_BD            | 15.2.10.254/24    | 
|                     |           |      | DT-EPNM/DT-EPNM/MGMT                                    | DT-EPNM/DT-EPNM-MGMT_BD      | 10.58.27.110/28   | 
|                     |           |      | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | ECMP-demo/MPC-CDC-2_BD       | 15.2.203.254/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              | P5G/P5G-F1C-NGC-N2           | 15.100.161.126/25 | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
|                     |           |      | common/Infra_ANP/PrivateIP-MGMT                         | common/Infra_BD              |                   | 
|                     |           |      | TESTING_BRUNO/UntitledAP1/SITE1                         | TESTING_BRUNO/BD2            | 192.168.1.1/24    | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | SPIN_InnoLab/SPIN-Backend_BD |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | SPIN_InnoLab/SPIN-CSR-A      |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | SPIN_InnoLab/SPIN-CSR-P      |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | SPIN_InnoLab/SPIN-CSR-P-2    |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | SPIN_InnoLab/SPIN-MGMT_BD    | 10.58.239.254/24  | 
|                     |           |      | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | SPN_IntraLab/SPN_BD1         | 192.168.0.254/24  | 
|                     |           |      | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | iks-monitoring/iks-mon_BD    |                   | 
| pod-1/bl205-eu-spdc | 1/2       | up   | CNC_demo/CNC_ANP/CNC_bus                                | CNC_demo/CNC_BD1             | 10.58.24.254/27   | 
|                     |           |      | NXOS-HandOff_Test/TEST/EPG1                             | NXOS-HandOff_Test/BD1        | 192.168.1.1/24    | 
|                     |           |      | mgmt/EU-SPDC_ANP/EU-SPDC-ERSPAN                         | mgmt/EU-SPDC-ERSPAN-BD       | 99.99.99.254/24   | 
|                     |           |      | MPC-F5T/F5_ANP/F5_IN                                    | MPC-F5T/F5-IN_BD             | 15.2.64.254/24    | 
|                     |           |      | MPC-F5T/F5_ANP/F5_OUT                                   | MPC-F5T/F5-OUT_BD            | 15.2.10.254/24    | 
|                     |           |      | ECMP-demo/AP-ECMP-demo_ANP/MPC-CDC-2                    | ECMP-demo/MPC-CDC-2_BD       | 15.2.203.254/24   | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
|                     |           |      | common/Infra_ANP/PrivateIP-MGMT                         | common/Infra_BD              |                   | 
|                     |           |      | TESTING_BRUNO/UntitledAP1/SITE1                         | TESTING_BRUNO/BD2            | 192.168.1.1/24    | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-Backend01                | SPIN_InnoLab/SPIN-Backend_BD |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-A                    | SPIN_InnoLab/SPIN-CSR-A      |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P                    | SPIN_InnoLab/SPIN-CSR-P      |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-CSR-P-2                  | SPIN_InnoLab/SPIN-CSR-P-2    |                   | 
|                     |           |      | SPIN_InnoLab/SPIN_InnoLab/SPIN-MGMT                     | SPIN_InnoLab/SPIN-MGMT_BD    | 10.58.239.254/24  | 
|                     |           |      | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | SPN_IntraLab/SPN_BD1         | 192.168.0.254/24  | 
|                     |           |      | iks-monitoring/Vitria-Monitoring_ANP/Vitria-Mon-BackEnd | iks-monitoring/iks-mon_BD    |                   | 
| pod-1/bl205-eu-spdc | 1/3       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/4       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/5       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/6       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/7       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/8       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/9       | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/10      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/11      | up   |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/12      | up   |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/13      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/14      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/15      | up   | P5G/P5G_App/P5G-Edge-Int                                | P5G/P5G-Edge-Int             | 15.100.169.1/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              | P5G/P5G-F1U-NGU-N3           | 15.100.161.254/25 | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  | P5G/P5G-N6-NAT               |                   | 
| pod-1/bl205-eu-spdc | 1/16      | up   | P5G/P5G_App/P5G-Edge-Int                                | P5G/P5G-Edge-Int             | 15.100.169.1/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              | P5G/P5G-F1C-NGC-N2           | 15.100.161.126/25 | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              | P5G/P5G-F1U-NGU-N3           | 15.100.161.254/25 | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  | P5G/P5G-N6-NAT               |                   | 
| pod-1/bl205-eu-spdc | 1/17      | down | P5G/P5G_App/P5G-Edge-Int                                | P5G/P5G-Edge-Int             | 15.100.169.1/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              | P5G/P5G-F1C-NGC-N2           | 15.100.161.126/25 | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              | P5G/P5G-F1U-NGU-N3           | 15.100.161.254/25 | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  | P5G/P5G-N6-NAT               |                   | 
| pod-1/bl205-eu-spdc | 1/18      | down | P5G/P5G_App/P5G-Edge-Int                                | P5G/P5G-Edge-Int             | 15.100.169.1/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              | P5G/P5G-F1C-NGC-N2           | 15.100.161.126/25 | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              | P5G/P5G-F1U-NGU-N3           | 15.100.161.254/25 | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
|                     |           |      | P5G/P5G_App/P5G-N6-NAT                                  | P5G/P5G-N6-NAT               |                   | 
| pod-1/bl205-eu-spdc | 1/19      | up   | P5G/P5G_App/P5G-Edge-Int                                | P5G/P5G-Edge-Int             | 15.100.169.1/24   | 
|                     |           |      | P5G/P5G_App/P5G-F1C-NGC-N2                              | P5G/P5G-F1C-NGC-N2           | 15.100.161.126/25 | 
|                     |           |      | P5G/P5G_App/P5G-F1U-NGU-N3                              | P5G/P5G-F1U-NGU-N3           | 15.100.161.254/25 | 
|                     |           |      | P5G/P5G_App/P5G-mgmt                                    | P5G/P5G-mgmt                 | 10.58.24.158/27   | 
| pod-1/bl205-eu-spdc | 1/20      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/21      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/22      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/23      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/24      | up   |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/25      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/26      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/27      | up   | SPN_IntraLab/SPN_Connect_ANP/TEST1                      | SPN_IntraLab/SPN_BD1         | 192.168.0.254/24  | 
| pod-1/bl205-eu-spdc | 1/28      | up   |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/29      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/30      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/31      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/32      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/33      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/34      | down |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/35      | up   |                                                         |                              |                   | 
| pod-1/bl205-eu-spdc | 1/36      | up   |                                                         |                              |                   | 
+---------------------+-----------+------+---------------------------------------------------------+------------------------------+-------------------+
```

[[Back]](./InterfacePhy.md)