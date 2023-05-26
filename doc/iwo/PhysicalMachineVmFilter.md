# Intersight Workload Optimizer

## Filter by virtual machine name

```
# iserver get iwo phy --vm ibc

Summary
-------
- Active   : 3/3
- Severity : 0/0/1/2
- Current  : 3/3


+--------+-----------+-----------+-------------------------+--------------------------+---------------------------------------------+
| State  | Severity  | Staleness | Name                    | Virtual Machine Severity | Virtual Machine                             |
+--------+-----------+-----------+-------------------------+--------------------------+---------------------------------------------+
| ACTIVE | Minor (1) | CURRENT   | esx41-eu-spdc.cisco.com | 0/0/9/1                  | CSR-NAT-NF63                                | 
|        |           |           |                         |                          | Windows Server 2019 Airspan Netspan         | 
|        |           |           |                         |                          | ibc-demo-ibc-a0b852c940                     | 
|        |           |           |                         |                          | mpc-ASAv-NF61                               | 
|        |           |           |                         |                          | mpc-F5-BigIP-test                           | 
|        |           |           |                         |                          | mpc-IPS-NF42                                | 
|        |           |           |                         |                          | mpc-NAT-NF43                                | 
|        |           |           |                         |                          | mpc-e-ASAv-NF21                             | 
|        |           |           |                         |                          | mpc-e-NAT-NF23                              | 
|        |           |           |                         |                          | vanniew-iks--1-control-p-49c278b6c1         | 
+--------+-----------+-----------+-------------------------+--------------------------+---------------------------------------------+
| ACTIVE | Normal    | CURRENT   | esx51-eu-spdc.cisco.com | 0/0/19/7                 | CSR-NAT-NF13                                | 
|        |           |           |                         |                          | CSR-NAT-NF23                                | 
|        |           |           |                         |                          | CSR-NAT-NF53                                | 
|        |           |           |                         |                          | CSR-e-NAT-NF13                              | 
|        |           |           |                         |                          | CSR-e-NAT-NF23                              | 
|        |           |           |                         |                          | CSR-e-NAT-NF33                              | 
|        |           |           |                         |                          | MPC-CL-Demo-CU                              | 
|        |           |           |                         |                          | cl-bgp-6r7xm-worker-n4bdq                   | 
|        |           |           |                         |                          | ibc-demo-ibc-6dd5b97865                     | 
|        |           |           |                         |                          | mpc-ASAv-NF41                               | 
|        |           |           |                         |                          | mpc-ASAv-NF51                               | 
|        |           |           |                         |                          | mpc-F5-client                               | 
|        |           |           |                         |                          | mpc-IPS-NF12                                | 
|        |           |           |                         |                          | mpc-IPS-NF22                                | 
|        |           |           |                         |                          | mpc-IPS-NF32                                | 
|        |           |           |                         |                          | mpc-IPS-NF62                                | 
|        |           |           |                         |                          | mpc-NAT-NF13                                | 
|        |           |           |                         |                          | mpc-NAT-NF33                                | 
|        |           |           |                         |                          | mpc-e-IPS-NF32                              | 
|        |           |           |                         |                          | mpc-uc1-agent                               | 
|        |           |           |                         |                          | mpc-uc22                                    | 
|        |           |           |                         |                          | mpc-uc3-agent                               | 
|        |           |           |                         |                          | old-mpc-e-ASAv-NF11                         | 
|        |           |           |                         |                          | vCLS-db9a27aa-2489-45b4-bfaf-d98e200a4fe2   | 
|        |           |           |                         |                          | vanniew-iks--1-worker-pr-322960ac11         | 
|        |           |           |                         |                          | vimercate-default-2-worker-ced0cb5a6e       | 
+--------+-----------+-----------+-------------------------+--------------------------+---------------------------------------------+
| ACTIVE | Normal    | CURRENT   | esx52-eu-spdc.cisco.com | 0/0/5/30                 | ACIextr-C11                                 | 
|        |           |           |                         |                          | ASAv  fresh install                         | 
|        |           |           |                         |                          | ASAv-9.8.4.10-clone-full                    | 
|        |           |           |                         |                          | ASAv-9.8.4.10-config-clone                  | 
|        |           |           |                         |                          | Client-VF34                                 | 
|        |           |           |                         |                          | NDB                                         | 
|        |           |           |                         |                          | NF11_ASAv                                   | 
|        |           |           |                         |                          | NF11_CSR1K                                  | 
|        |           |           |                         |                          | NGINX-VM-CLONE                              | 
|        |           |           |                         |                          | Z-PROBE_in                                  | 
|        |           |           |                         |                          | cl-bgp-6r7xm-master-0                       | 
|        |           |           |                         |                          | ibc-demo-controlpl-8877420f2f               | 
|        |           |           |                         |                          | ibc-demo-ibc-27801251c0                     | 
|        |           |           |                         |                          | ibc-demo-ibc-545014a7e0                     | 
|        |           |           |                         |                          | loadgen-1                                   | 
|        |           |           |                         |                          | loadgen-2                                   | 
|        |           |           |                         |                          | loadgen-3                                   | 
|        |           |           |                         |                          | mpc-uc1-reflector                           | 
|        |           |           |                         |                          | mso-3.1.1i                                  | 
|        |           |           |                         |                          | old-mpc-e-ASAv-NF21                         | 
|        |           |           |                         |                          | old-mpc-e-ASAv-NF31                         | 
|        |           |           |                         |                          | open5gs-on-k8s-apiclarity                   | 
|        |           |           |                         |                          | panoptica                                   | 
|        |           |           |                         |                          | panoptica-1                                 | 
|        |           |           |                         |                          | panoptica-2                                 | 
|        |           |           |                         |                          | sPBR-client-ext                             | 
|        |           |           |                         |                          | sPBR-clients                                | 
|        |           |           |                         |                          | sPBR-clients-6R                             | 
|        |           |           |                         |                          | tpt-open5gs                                 | 
|        |           |           |                         |                          | turnkey-nginx-php-fastcgi-16.1-buster-amd64 | 
|        |           |           |                         |                          | vCLS-78b48072-4ae0-4e93-af49-95f7b6c67fb5   | 
|        |           |           |                         |                          | vanniew-iks--1-worker-pr-a8ba876a5f         | 
|        |           |           |                         |                          | vanniew-iks--2-worker-pr-7e6f447f22         | 
|        |           |           |                         |                          | vanniew-iks--2-worker-pr-dfabfc5986         | 
|        |           |           |                         |                          | vimercate-default-2-controlpl-d98e986ca5    | 
+--------+-----------+-----------+-------------------------+--------------------------+---------------------------------------------+
```