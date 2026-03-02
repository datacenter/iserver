# Local Storage Operator - Create Volume

There are tree ways (aka mode) to configure volumes in local storage i.e.

Intent | Mode | Command 
--- | --- | ---
All-nodes with device discovery | [discovery-all](./create_volume_all.md) | iserver set ocp lso --mode volume 
Selected nodes with device discovery | [discovery-node](./create_volume_nodes.md) | iserver set ocp lso --mode volume --device nodeName-a
Explicit nodes and devices | [explicit](./create_volume_explicit.md) | iserver set ocp lso --mode volume --device nodeName-a:wwn-b 

[[Back]](./README.md)