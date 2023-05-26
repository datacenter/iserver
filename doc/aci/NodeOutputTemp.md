# Node

## Temperature specific output

```
# iserver get aci node --apic apic11 -o temp --name bl205*

Apic: apic11

+---------------------+--------------------+-----+------+-----+
| Node                | Sensor             | Avg | Last | Max |
+---------------------+--------------------+-----+------+-----+
| pod-1/bl205-eu-spdc | supslot-1.sensor-1 | 20  | 21   | 21  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-1 | 20  | 21   | 21  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-2 | 27  | 27   | 27  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-2 | 27  | 27   | 27  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-3 | 31  | 32   | 32  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-3 | 31  | 32   | 32  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-4 | 47  | 47   | 48  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-4 | 47  | 47   | 48  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-5 | 36  | 36   | 36  | 
| pod-1/bl205-eu-spdc | supslot-1.sensor-5 | 36  | 36   | 36  | 
+---------------------+--------------------+-----+------+-----+
```

[[Back]](./Node.md)