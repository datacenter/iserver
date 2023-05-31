# Policy - Transceiver

## JSON

```
# iserver get aci policy transceiver --apic apic11 --name default -o json

[
    {
        "__Output": {
            "adminSt": "Red"
        },
        "adminSt": "disabled",
        "annotation": "",
        "cdMax": "2400",
        "cdMin": "-2400",
        "dacRate": "1x1",
        "dn": "uni/infra/zr-default",
        "dwdmCarrier": "100MHzFrequency",
        "fecMode": "cFEC",
        "frequency100MHz": "1931000",
        "frequency50GHz": "19310",
        "ituChannel50GHz": "61",
        "modulation": "16QAM",
        "muxponder": "1x400",
        "name": "default",
        "type": "xcvrZRIfPol",
        "transmitPower": "-190",
        "wavelength50GHz": "1552524",
        "tf": false,
        "tfTick": "",
        "typeT": "ZR",
        "l1RsSynceEthIfPolCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    },
    {
        "__Output": {
            "adminSt": "Red"
        },
        "adminSt": "disabled",
        "annotation": "",
        "cdMax": "2400",
        "cdMin": "-2400",
        "dacRate": "1x1",
        "dn": "uni/infra/zr-default",
        "dwdmCarrier": "100MHzFrequency",
        "fecMode": "cFEC",
        "frequency100MHz": "1931000",
        "frequency50GHz": "19310",
        "ituChannel50GHz": "61",
        "modulation": "16QAM",
        "muxponder": "1x400",
        "name": "default",
        "type": "xcvrZRIfPol",
        "transmitPower": "-190",
        "wavelength50GHz": "1552524",
        "tf": false,
        "tfTick": "",
        "typeT": "ZR",
        "l1RsSynceEthIfPolCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    },
    {
        "__Output": {
            "adminSt": "Red"
        },
        "adminSt": "disabled",
        "annotation": "",
        "cdMax": "13000",
        "cdMin": "-13000",
        "dacRate": "1x1.25",
        "dn": "uni/infra/zrp-default",
        "dwdmCarrier": "100MHzFrequency",
        "fecMode": "oFEC",
        "frequency100MHz": "1911500",
        "frequency50GHz": "19115",
        "ituChannel50GHz": "1",
        "modulation": "16QAM",
        "muxponder": "1x400",
        "name": "default",
        "type": "xcvrZRPIfPol",
        "transmitPower": "-190",
        "wavelength50GHz": "1528773",
        "tf": false,
        "tfTick": "",
        "typeT": "ZRP",
        "l1RsSynceEthIfPolCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    },
    {
        "__Output": {
            "adminSt": "Red"
        },
        "adminSt": "disabled",
        "annotation": "",
        "cdMax": "13000",
        "cdMin": "-13000",
        "dacRate": "1x1.25",
        "dn": "uni/infra/zrp-default",
        "dwdmCarrier": "100MHzFrequency",
        "fecMode": "oFEC",
        "frequency100MHz": "1911500",
        "frequency50GHz": "19115",
        "ituChannel50GHz": "1",
        "modulation": "16QAM",
        "muxponder": "1x400",
        "name": "default",
        "type": "xcvrZRPIfPol",
        "transmitPower": "-190",
        "wavelength50GHz": "1528773",
        "tf": false,
        "tfTick": "",
        "typeT": "ZRP",
        "l1RsSynceEthIfPolCons": [],
        "interfaces": 0,
        "nodeInterfaces": []
    }
]
```

[[Back]](./PolicyTrans.md)