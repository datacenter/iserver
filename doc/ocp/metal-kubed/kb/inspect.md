# Metal Kubed - host inspection

[[Back]](../README.md)

## Automatic inspection

When new `BareMetalHost` is created, ironic agent collects information about the available hardware components and sends it back to Metal3. The host will stay in the inspecting state until this process is completed.

## Controlling inspection

Inspection can be initiated by [annotation](https://book.metal3.io/bmo/inspect_annotation.html). Once inspection is requested, you should see the `BareMetalHost` in inspecting state until inspection is completed, and by the end of inspection the inspect.metal3.io annotation will be removed automatically.

```
$ oc annotate bmh -n openshift-machine-api bm1-1 inspect.metal3.io=''
baremetalhost.metal3.io/bm1-1 annotated
```

## Inspection logs

Inspection is performed by metal3 ironic container e.g.,

```
$ oc logs -n openshift-machine-api metal3-xyz -c metal3-ironic
2026-04-17 16:19:01.959 56 DEBUG sushy.connector [None req-d76c4957-f60d-4bb8-bc4a-ffc0cd78dea8 - - - - - -] 
  HTTP request: 
    GET https://10.10.10.10/redfish/v1/Systems/AAAA; 
    headers: {'OData-Version': '4.0', 'Accept-Encoding': 'identity'}; 
    body: None; 
    blocking: False; 
    timeout: 60; 
    session arguments: {}; 
    _op /usr/lib/python3.12/site-packages/sushy/connector.py:167
```

[[Back]](../README.md)