# Servers Inventory Summary

Get servers' summary information.

Use command options for servers' filtering and information shown in summary.

Use -o|--output for desired output format.

## Base output

```
# iserver get summary

Selected servers count: 103

Type
- Rack  : 93
- Blade : 10

Models
- HXAF220C-M5SN             : 4
- HXAF240C-M5SX             : 3
- PowerEdge R650            : 1
- ProLiant DL360 Gen10 Plus : 1
- SE-NODE-G2                : 3
- UCSB-B200-M4              : 4
- UCSB-B200-M5              : 4
- UCSC-C220-M4S             : 26
- UCSC-C220-M5SX            : 26
- UCSC-C225-M6S             : 2
- UCSC-C240-M4S             : 3
- UCSC-C240-M4SX            : 5
- UCSC-C240-M5SN            : 6
- UCSC-C240-M5SX            : 11
- UCSC-C245-M6SX            : 2
- UCSC-C3K-M4SRB            : 2

Power
- On  : 75
- Off : 28

Maximum
- CpuSockets : 2
- CpuCores   : 128
- CpuThreads : 256
- Memory     : 768

Health
- Healthy  : 83
- Warning  : 10
- Critical : 10

Locator
- On  : 1
- Off : 102

Management Mode
- Standalone : 80
- UCSM       : 23

Last Workflows Summary
- Running                   : 0
- Success                   : 0
- Failed                    : 0
- Servers with workflows    : 0
- Servers with no workflows : 103

Workflow Names
```

## Extended output

```
# iserver get summary -c all

Selected servers count: 103

Type
- Rack  : 93
- Blade : 10

Models
- HXAF220C-M5SN             : 4
- HXAF240C-M5SX             : 3
- PowerEdge R650            : 1
- ProLiant DL360 Gen10 Plus : 1
- SE-NODE-G2                : 3
- UCSB-B200-M4              : 4
- UCSB-B200-M5              : 4
- UCSC-C220-M4S             : 26
- UCSC-C220-M5SX            : 26
- UCSC-C225-M6S             : 2
- UCSC-C240-M4S             : 3
- UCSC-C240-M4SX            : 5
- UCSC-C240-M5SN            : 6
- UCSC-C240-M5SX            : 11
- UCSC-C245-M6SX            : 2
- UCSC-C3K-M4SRB            : 2

Power
- On  : 75
- Off : 28

Maximum
- CpuSockets          : 2
- CpuCores            : 128
- CpuThreads          : 256
- Memory              : 768
- Storage Controllers : 12
- Total Disk Capacity : 31.58 [TB]
- HDD Count           : 21
- HDD Capacity        : 25.18 [TB]
- SSD Count           : 11
- SSD Capacity        : 31.58 [TB]
- PCI Devices         : 11

Health
- Healthy  : 83
- Warning  : 10
- Critical : 10

Locator
- On  : 1
- Off : 102

Management Mode
- Standalone : 80
- UCSM       : 23

Server Fans
- All up    : 69
- Some down : 34

Server Psus
- All up    : 91
- Some down : 12

PCI Models
-                                                                  : 6
- 00MNMV                                                           : 2
- 04TRD3                                                           : 1
- 0FGNRW                                                           : 1
- 0MHFHK                                                           : 1
- Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) : 1
- Cisco UCS VIC 1387 MLOM                                          : 1
- Intel Unknown Device                                             : 1
- Intel X550 LOM                                                   : 45
- Intel XL710-QDA2 Dual Port 40Gb QSFP converged NIC               : 2
- Intel(R) I350 1 Gbps Network Controller                          : 27
- K53978-004                                                       : 1
- LSI MegaRAID SAS 3108                                            : 7
- N2XX-AIPCI01                                                     : 16
- P26463-B21                                                       : 1
- SSDPE21K375GAW                                                   : 7
- SSDPE2KX010T8K                                                   : 36
- UCS-C3K-M4RAID                                                   : 2
- UCS-M2-HWRAID                                                    : 4
- UCS-NVMEI4-I1920                                                 : 8
- UCSB-MRAID12G                                                    : 4
- UCSB-MRAID12G-HE                                                 : 4
- UCSC-C3260-SIOC                                                  : 2
- UCSC-GPU-A16                                                     : 1
- UCSC-GPU-T4-16                                                   : 1
- UCSC-M-V100-04                                                   : 4
- UCSC-MLOM-C100-04                                                : 1
- UCSC-MLOM-C25Q-04                                                : 27
- UCSC-MLOM-C40Q-03                                                : 8
- UCSC-MLOM-CSC-02                                                 : 31
- UCSC-MRAID12G                                                    : 27
- UCSC-NVMEHW-H1600                                                : 3
- UCSC-PCIE-C25Q-04                                                : 7
- UCSC-PCIE-CSC-02                                                 : 3
- UCSC-PCIE-ID10GF                                                 : 1
- UCSC-PCIE-ID25GF                                                 : 30
- UCSC-PCIE-ID40GF                                                 : 12
- UCSC-PCIE-IQ10GF                                                 : 69
- UCSC-RAID-M5                                                     : 34
- UCSC-RAID-M5HD                                                   : 11
- UCSC-RAID-M6SD                                                   : 2
- UCSC-RAID-M6T                                                    : 2
- UCSC-SAS-M5HD                                                    : 3

Firmware
- 2.55       : 1
- 4.0(4b)    : 3
- 4.0(4e)    : 1
- 4.1(1f)    : 1
- 4.1(2f)    : 20
- 4.1(2g)    : 10
- 4.1(2k)    : 7
- 4.1(3b)    : 2
- 4.1(3c)    : 1
- 4.1(3d)    : 28
- 4.1(3f)    : 6
- 4.1(3i)    : 1
- 4.2(1a)    : 4
- 4.2(1c)    : 4
- 4.2(2a)    : 12
- 4.2(2f)    : 1
- 5.10.00.00 : 1

Last Workflows Summary
- Running                   : 0
- Success                   : 0
- Failed                    : 0
- Servers with workflows    : 0
- Servers with no workflows : 103

Workflow Names
```

Developer output

```
# iserver get summary -c all

Developer output

{
    "duration": 62795,
    "isctl": {
        "read": true,
        "calls": 158,
        "success": 158,
        "failed": 0,
        "total_time": 100114
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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
        "lines": 47
    }
}

Log: isctl
-----------

2022-12-13 17:05:28.756292	True	1754	93	isctl get compute rackunit   -o json --top 100
2022-12-13 17:05:29.573360	True	816	10	isctl get compute blade   -o json --top 100
2022-12-13 17:05:30.019067	True	396	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T17:05:29.000Z"  -o json --top 100
2022-12-13 17:05:30.170214	True	552	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 17:05:30.921943	True	1293	100	isctl get equipment fanmodule   -o json --top 100
2022-12-13 17:05:31.052240	True	868	100	isctl get equipment psu   -o json --top 100
2022-12-13 17:05:31.061214	True	1450	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 17:05:31.206893	True	1173	100	isctl get pci device   -o json --top 100
2022-12-13 17:05:31.476800	True	415	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
2022-12-13 17:05:31.758735	True	704	100	isctl get equipment psu   -o json --top 100 --skip 100
2022-12-13 17:05:31.902044	True	976	100	isctl get equipment fanmodule   -o json --top 100 --skip 100
2022-12-13 17:05:32.000617	True	791	100	isctl get pci device   -o json --top 100 --skip 100
2022-12-13 17:05:32.246967	True	487	25	isctl get equipment psu   -o json --top 100 --skip 200
2022-12-13 17:05:32.616280	True	1110	100	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100
2022-12-13 17:05:32.687670	True	685	100	isctl get pci device   -o json --top 100 --skip 200
2022-12-13 17:05:32.805537	True	900	100	isctl get equipment fanmodule   -o json --top 100 --skip 200
2022-12-13 17:05:33.013008	True	385	3	isctl get firmware runningfirmware --filter "Component eq 'system' and Type eq 'blade-controller'"  -o json --top 100 --skip 100
2022-12-13 17:05:33.551665	True	1261	100	isctl get storage controller   -o json --top 100
2022-12-13 17:05:33.836001	True	1147	100	isctl get pci device   -o json --top 100 --skip 300
2022-12-13 17:05:34.096755	True	1288	100	isctl get equipment fanmodule   -o json --top 100 --skip 300
2022-12-13 17:05:34.265136	True	1204	98	isctl get storage virtualdrive   -o json --top 100
2022-12-13 17:05:34.424235	True	585	57	isctl get pci device   -o json --top 100 --skip 400
2022-12-13 17:05:34.530449	True	976	92	isctl get storage controller   -o json --top 100 --skip 100
2022-12-13 17:05:34.928832	True	829	100	isctl get equipment fanmodule   -o json --top 100 --skip 400
2022-12-13 17:05:35.297909	True	1003	100	isctl get storage physicaldisk   -o json --top 100
2022-12-13 17:05:35.783707	True	852	100	isctl get equipment fanmodule   -o json --top 100 --skip 500
2022-12-13 17:05:36.441518	True	1140	100	isctl get storage physicaldisk   -o json --top 100 --skip 100
2022-12-13 17:05:36.665406	True	879	88	isctl get equipment fanmodule   -o json --top 100 --skip 600
2022-12-13 17:05:37.317439	True	873	100	isctl get storage physicaldisk   -o json --top 100 --skip 200
2022-12-13 17:05:38.551114	True	1229	100	isctl get storage physicaldisk   -o json --top 100 --skip 300
2022-12-13 17:05:39.949147	True	1393	100	isctl get storage physicaldisk   -o json --top 100 --skip 400
2022-12-13 17:05:41.000024	True	1044	100	isctl get storage physicaldisk   -o json --top 100 --skip 500
2022-12-13 17:05:41.400416	True	400	5	isctl get storage physicaldisk   -o json --top 100 --skip 600
2022-12-13 17:05:42.024419	True	460	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5ecf87bc6f72612d3068c346'"  -o json --top 100
2022-12-13 17:05:42.027577	True	468	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5ecf86d86f72612d3068b4bc'"  -o json --top 100
2022-12-13 17:05:42.269249	True	715	7	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5ecf82676f72612d30687409'"  -o json --top 100
2022-12-13 17:05:42.312157	True	766	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5e8c4ecd6f72612d302b11a6'"  -o json --top 100
2022-12-13 17:05:43.241556	True	429	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa045b46f72612d3086c548'"  -o json --top 100
2022-12-13 17:05:43.697334	True	449	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa0489f6f72612d30878741'"  -o json --top 100
2022-12-13 17:05:43.907793	True	410	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04a9e6f72612d30880e03'"  -o json --top 100
2022-12-13 17:05:44.236934	True	704	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04b536f72612d30883fd0'"  -o json --top 100
2022-12-13 17:05:44.757988	True	408	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04be16f72612d30886344'"  -o json --top 100
2022-12-13 17:05:45.511676	True	389	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04cb86f72612d30889bc8'"  -o json --top 100
2022-12-13 17:05:45.761578	True	402	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04dd16f72612d3088e6b1'"  -o json --top 100
2022-12-13 17:05:46.012503	True	423	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa04e6c6f72612d30890d70'"  -o json --top 100
2022-12-13 17:05:46.268924	True	388	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa051776f72612d3089d7e9'"  -o json --top 100
2022-12-13 17:05:47.071655	True	415	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa052926f72612d308a2325'"  -o json --top 100
2022-12-13 17:05:47.392546	True	461	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fa1a78b6f72612d30e49bd3'"  -o json --top 100
2022-12-13 17:05:47.411885	True	433	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9be76f72612d300a8d81'"  -o json --top 100
2022-12-13 17:05:47.650091	True	511	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9c676f72612d300a9c8d'"  -o json --top 100
2022-12-13 17:05:48.221619	True	421	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdf9cf26f72612d300aaca0'"  -o json --top 100
2022-12-13 17:05:49.003975	True	440	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfa1686f72612d300b383f'"  -o json --top 100
2022-12-13 17:05:49.038903	True	417	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfdc206f72612d30120ab4'"  -o json --top 100
2022-12-13 17:05:49.199059	True	407	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfe4666f72612d30130510'"  -o json --top 100
2022-12-13 17:05:50.080635	True	426	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fdfe7d86f72612d30136fed'"  -o json --top 100
2022-12-13 17:05:50.679131	True	483	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fe295916f72612d306438ac'"  -o json --top 100
2022-12-13 17:05:50.714011	True	432	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fe32eb66f72612d3075c96a'"  -o json --top 100
2022-12-13 17:05:50.776166	True	410	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5fe32f4d6f72612d3075db4b'"  -o json --top 100
2022-12-13 17:05:51.744933	True	472	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026a9096f72612d305e7b8b'"  -o json --top 100
2022-12-13 17:05:52.254485	True	408	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026a9976f72612d305e8e4c'"  -o json --top 100
2022-12-13 17:05:52.268316	True	401	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026aa376f72612d305ea314'"  -o json --top 100
2022-12-13 17:05:52.763082	True	424	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026aade6f72612d305eb7fd'"  -o json --top 100
2022-12-13 17:05:53.364171	True	388	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026ab6f6f72612d305ec984'"  -o json --top 100
2022-12-13 17:05:53.863207	True	424	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026ae116f72612d305f1e80'"  -o json --top 100
2022-12-13 17:05:54.196798	True	702	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026aefd6f72612d305f3c94'"  -o json --top 100
2022-12-13 17:05:54.349496	True	395	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026afe76f72612d305f5af6'"  -o json --top 100
2022-12-13 17:05:54.996442	True	446	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b0a16f72612d305f7116'"  -o json --top 100
2022-12-13 17:05:55.330089	True	708	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b2376f72612d305fa447'"  -o json --top 100
2022-12-13 17:05:55.485742	True	422	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b5846f72612d30b98bb0'"  -o json --top 100
2022-12-13 17:05:56.251222	True	685	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b6346f72612d30b997b6'"  -o json --top 100
2022-12-13 17:05:56.653101	True	406	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b9416f72612d30b9be8a'"  -o json --top 100
2022-12-13 17:05:56.677335	True	465	11	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026b8a26f72612d30b9b627'"  -o json --top 100
2022-12-13 17:05:57.061066	True	457	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026bbb86f72612d30b9e10d'"  -o json --top 100
2022-12-13 17:05:57.579386	True	472	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6026c0336f72612d30ba2932'"  -o json --top 100
2022-12-13 17:05:57.930423	True	428	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6061d69a6f72612d30c09961'"  -o json --top 100
2022-12-13 17:05:58.351355	True	442	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '606323916f72612d30e34f36'"  -o json --top 100
2022-12-13 17:05:58.704880	True	444	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '60632bb46f72612d30e4222e'"  -o json --top 100
2022-12-13 17:05:59.333065	True	467	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '60632d896f72612d30e45356'"  -o json --top 100
2022-12-13 17:05:59.591239	True	450	11	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6098fe506f72612d30e78ffb'"  -o json --top 100
2022-12-13 17:06:00.364454	True	442	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61320ad96f72612d300340e7'"  -o json --top 100
2022-12-13 17:06:00.377173	True	682	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5ecf87256f72612d3068b971'"  -o json --top 100
2022-12-13 17:06:01.098639	True	506	10	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6139bd1a6f72612d30db6982'"  -o json --top 100
2022-12-13 17:06:01.319534	True	427	7	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6141c1e76f72612d30d2b35f'"  -o json --top 100
2022-12-13 17:06:01.576186	True	397	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6141c3186f72612d30d2d8f8'"  -o json --top 100
2022-12-13 17:06:02.063244	True	451	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6141c37c6f72612d30d2e54d'"  -o json --top 100
2022-12-13 17:06:02.794186	True	407	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6141c3976f72612d30d2e7d0'"  -o json --top 100
2022-12-13 17:06:03.006962	True	419	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6169b3926f72612d30589b53'"  -o json --top 100
2022-12-13 17:06:03.238122	True	431	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6169b7086f72612d3058fe9b'"  -o json --top 100
2022-12-13 17:06:03.767292	True	451	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '616ea3296f72612d30e81fe9'"  -o json --top 100
2022-12-13 17:06:05.071741	True	962	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:05.242979	True	970	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:05.404755	True	924	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:05.642715	True	458	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:05.834578	True	429	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:05.985237	True	970	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:06.203239	True	473	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:06.572774	True	486	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:07.241555	True	813	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:07.462407	True	768	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:07.786766	True	459	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:07.838065	True	410	7	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61df0d3c6f72612d307e5a50'"  -o json --top 100
2022-12-13 17:06:07.874236	True	830	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:07.965888	True	411	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:08.716190	True	738	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:08.931397	True	378	7	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61df0df76f72612d307e6ad3'"  -o json --top 100
2022-12-13 17:06:09.147211	True	443	7	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61df11db6f72612d307ebf0f'"  -o json --top 100
2022-12-13 17:06:09.902289	True	434	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61e998396f72612d305682d9'"  -o json --top 100
2022-12-13 17:06:11.102546	True	416	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61e99b2d6f72612d3056bb7d'"  -o json --top 100
2022-12-13 17:06:11.509026	True	399	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61e99f9c6f72612d3057152d'"  -o json --top 100
2022-12-13 17:06:12.517315	True	473	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61e9a19a6f72612d30573d28'"  -o json --top 100
2022-12-13 17:06:12.680596	True	389	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61e9a40d6f72612d30576dcc'"  -o json --top 100
2022-12-13 17:06:12.728647	True	406	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61fa65ab6f72612d300ab92a'"  -o json --top 100
2022-12-13 17:06:13.682037	True	829	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:14.542247	True	722	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:14.748925	True	826	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:14.779971	True	739	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:14.965238	True	1176	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:15.472431	True	388	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:15.523398	True	868	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:15.652129	True	789	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:16.053545	True	1144	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:16.062936	True	406	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:16.135636	True	368	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:16.707928	True	415	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:17.150115	True	668	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:17.728307	True	834	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:17.891919	True	721	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100
2022-12-13 17:06:18.038908	True	755	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:18.521009	True	666	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:18.537968	True	1059	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100
2022-12-13 17:06:18.573641	True	409	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:18.812177	True	783	100	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 100
2022-12-13 17:06:19.106983	True	460	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:19.345185	True	387	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '62d157f56f72612d31c554a7'"  -o json --top 100 --skip 200
2022-12-13 17:06:19.471277	True	799	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61c35fa36f72612d3005590c'"  -o json --top 100 --skip 100
2022-12-13 17:06:20.046550	True	709	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6336f14d6f72612d31d41b72'"  -o json --top 100
2022-12-13 17:06:20.619843	True	470	4	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637b897f6f72612d39f8b9e9'"  -o json --top 100
2022-12-13 17:06:20.657013	True	388	6	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637b8a016f72612d39f8bfa7'"  -o json --top 100
2022-12-13 17:06:20.761427	True	398	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637ca8cd6f72612d3130bddc'"  -o json --top 100
2022-12-13 17:06:21.776906	True	446	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637cadbb6f72612d3130e87a'"  -o json --top 100
2022-12-13 17:06:21.887823	True	417	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637ce9916f72612d3132dcb3'"  -o json --top 100
2022-12-13 17:06:22.533689	True	466	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637d60986f72612d31377620'"  -o json --top 100
2022-12-13 17:06:22.563219	True	427	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637d63196f72612d313788d7'"  -o json --top 100
2022-12-13 17:06:23.478350	True	440	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '637f58116f72612d31490de7'"  -o json --top 100
2022-12-13 17:06:24.247066	True	424	11	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6384d44a6f72612d317bfc51'"  -o json --top 100
2022-12-13 17:06:24.303267	True	470	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '638501816f72612d317dabd7'"  -o json --top 100
2022-12-13 17:06:24.376372	True	419	13	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '638502356f72612d317db208'"  -o json --top 100
2022-12-13 17:06:25.286208	True	511	11	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '6388e7616f72612d31a41c5c'"  -o json --top 100
2022-12-13 17:06:25.755746	True	468	8	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '5efdfb7e6f72612d30e4501e'"  -o json --top 100
2022-12-13 17:06:25.852355	True	466	9	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '61bb97146f72612d301e5946'"  -o json --top 100
2022-12-13 17:06:26.394381	True	680	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:27.205197	True	856	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:27.240889	True	878	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:27.820905	True	949	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:27.852935	True	883	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:28.447517	True	697	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:28.542278	True	775	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
2022-12-13 17:06:29.187361	True	783	85	isctl get firmware runningfirmware --filter "RegisteredDevice/Moid eq '618942976f72612d309dfbe1'"  -o json --top 100
```
