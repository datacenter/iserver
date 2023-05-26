# Node Interface - MACsec

## Verbose output

```
# iserver get aci intf macsec
    --apic apic11
    --node bl205-eu-spdc
    --id eth1/28 -o verbose

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

Interface Macsec
----------------
- Interface       : eth1/28
- Admin State     : disabled
- Oper State      : down
- Reason          : admin-down
- Session State   : not-initialized
- Peers           : 0
- Cepher Suite    : 0
- Confid Offset   : 0
- Key Chain       : 
- Ker Server Prio : 16
- Replay Window   : 64


MKA Stats
---------

SecY Stats
----------
- OK Packets           : 0
- Rx Decrypted Octets  : 0
- Rx Decrypted Packets : 0
- Delayed Packets      : 0
- Invalidated Octets   : 0
- Invalidated Packets  : 0
- Invalid Packets      : 0
- Late Packets         : 0
- Not Using SA Packets : 0
- Not Valid Packets    : 0
- Unchecked Packets    : 0
- Unused SA Packets    : 0
- Tx Encrypted Octets  : 0
- Tx Encrypted Packets : 0
- Tx Protected Octets  : 0
- Tx Protected Packets : 0
```

[[Back]](./InterfaceMacSec.md)