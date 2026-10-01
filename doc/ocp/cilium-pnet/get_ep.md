# Private Network - Get endpoints

[[Back]](./README.md)

## Example

```
# iserver get ocp cilium pnet -v ep

OpenShift Workflow - Isovalent Private Network - Get Information
================================================================

OpenShift Cluster: bm3
Cilium cni found

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cilium Agent DB: privnet-endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----+-----------------+---------+-----------+------+-------------+-------------------+--------------+-------+----------+
| ID | Private Network | Subnet  | Namespace | Name | IP          | MAC               | POD IP       | Node  | External |
+----+-----------------+---------+-----------+------+-------------+-------------------+--------------+-------+----------+
| 1  | blue            | subnet0 | default   | b1   | 10.0.200.11 | 9e:5e:3c:f1:19:c0 | 10.128.3.75  | bm1-1 | False    | 
| 2  | red             | subnet0 | default   | r1   | 10.0.100.11 | 92:84:6c:da:7f:0f | 10.128.3.160 | bm1-1 | False    | 
| 3  | blue            | subnet0 | default   | b2   | 10.0.200.12 | 1a:4b:dc:30:db:4a | 10.128.4.29  | bm1-2 | False    | 
| 4  | red             | subnet0 | default   | r2   | 10.0.100.12 | 4e:c4:bf:41:a5:34 | 10.128.4.124 | bm1-2 | False    | 
| 5  | blue            | subnet0 | default   | b3   | 10.0.200.13 | 3e:11:cf:64:a6:07 | 10.128.1.51  | bm1-3 | False    | 
| 6  | red             | subnet0 | default   | r3   | 10.0.100.13 | 8e:ce:4e:9c:cd:5c | 10.128.1.199 | bm1-3 | False    | 
+----+-----------------+---------+-----------+------+-------------+-------------------+--------------+-------+----------+

View: state (def), res, webhook, db, ep, all
```

[[Back]](./README.md)