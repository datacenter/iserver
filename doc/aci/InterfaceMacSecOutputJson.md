# Node Interface - MACsec

## JSON output

```
# iserver get aci intf macsec
    --apic apic11
    --node bl205-eu-spdc
    --id eth1/28 -o json

[
    {
        "__Output": {
            "id": "Blue",
            "adminSt": "Red",
            "operSt": "Red"
        },
        "adminSt": "disabled",
        "cipherSuite": "gcm-aes-xpn-256",
        "cipherSuiteOper": "0",
        "confOffset": "offset-0",
        "confOffsetOper": "0",
        "dn": "topology/pod-1/node-205/sys/macsec/inst/if-[eth1/28]",
        "id": "eth1/28",
        "keyChain": "",
        "keySvrPrio": "16",
        "lastSakKeyTime": "1970-01-01T02:00:00.000+02:00",
        "mkaNegSt": "if-neg-succ",
        "name": "default",
        "operSt": "down",
        "operStQual": "admin-down",
        "peerCount": "0",
        "portId": "unspecified",
        "replayWindow": "64",
        "sakExpiryTime": "disabled",
        "sakStatus": "no-rx-tx",
        "secPolicy": "should-secure",
        "sessOperSt": "not-initialized",
        "srvStatusFlags": "",
        "txSCI": "",
        "txSSCI": "0",
        "vlanTagCtrl": "skip-0",
        "iod": 28,
        "podId": "1",
        "nodeId": "205",
        "apic": "apic11",
        "pod_node_name": "pod-1/bl205-eu-spdc",
        "up": false,
        "portT": "leaf"
    }
]
```

[[Back]](./InterfaceMacSec.md)