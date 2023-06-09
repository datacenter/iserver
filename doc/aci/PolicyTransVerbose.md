# Policy - Transceiver

## Verbose output

```
# iserver get aci policy transceiver --apic apic11 --name default --view verbose

Apic: apic11 (mode:online, cache:off)

Transceiver Policy Properties
-----------------------------
- Policy Name                  : default
- TF                           : False
- Admin State                  : disabled
- Type                         : ZR
- Chromatic Dispersion Minimum : -2400
- Chromatic Dispersion Maximum : 2400
- DAC Rate                     : 1x1
- DWDM Carrier Grid Selector   : 100MHzFrequency
- FEC Mode                     : cFEC
- 100MHz Frequency             : 1931000
- 50GHz Frequency              : 19310
- 50GHz ITU Channel            : 61
- Modulation                   : 16QAM
- Muxponder Mode               : 1x400
- Transmit Power               : -190
- 50GHz Wavelength             : 1552524


Transceiver Policy Properties
-----------------------------
- Policy Name                  : default
- TF                           : False
- Admin State                  : disabled
- Type                         : ZR
- Chromatic Dispersion Minimum : -2400
- Chromatic Dispersion Maximum : 2400
- DAC Rate                     : 1x1
- DWDM Carrier Grid Selector   : 100MHzFrequency
- FEC Mode                     : cFEC
- 100MHz Frequency             : 1931000
- 50GHz Frequency              : 19310
- 50GHz ITU Channel            : 61
- Modulation                   : 16QAM
- Muxponder Mode               : 1x400
- Transmit Power               : -190
- 50GHz Wavelength             : 1552524


Transceiver Policy Properties
-----------------------------
- Policy Name                  : default
- TF                           : False
- Admin State                  : disabled
- Type                         : ZRP
- Chromatic Dispersion Minimum : -13000
- Chromatic Dispersion Maximum : 13000
- DAC Rate                     : 1x1.25
- DWDM Carrier Grid Selector   : 100MHzFrequency
- FEC Mode                     : oFEC
- 100MHz Frequency             : 1911500
- 50GHz Frequency              : 19115
- 50GHz ITU Channel            : 1
- Modulation                   : 16QAM
- Muxponder Mode               : 1x400
- Transmit Power               : -190
- 50GHz Wavelength             : 1528773


Transceiver Policy Properties
-----------------------------
- Policy Name                  : default
- TF                           : False
- Admin State                  : disabled
- Type                         : ZRP
- Chromatic Dispersion Minimum : -13000
- Chromatic Dispersion Maximum : 13000
- DAC Rate                     : 1x1.25
- DWDM Carrier Grid Selector   : 100MHzFrequency
- FEC Mode                     : oFEC
- 100MHz Frequency             : 1911500
- 50GHz Frequency              : 19115
- 50GHz ITU Channel            : 1
- Modulation                   : 16QAM
- Muxponder Mode               : 1x400
- Transmit Power               : -190
- 50GHz Wavelength             : 1528773
```

Developer

```
# iserver get aci policy transceiver --apic apic11 --name default --view verbose

{
    "duration": 1930,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 452,
        "disconnect_time": 0,
        "mo_time": 1083,
        "total_time": 1535
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
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	452	-	connect apic11o.emea-sp.cisco.com
True	342	2	apic11o.emea-sp.cisco.com class xcvrOpticsIfPol
True	405	470	apic11o.emea-sp.cisco.com class l1RsSynceEthIfPolCons
True	336	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyTrans.md)