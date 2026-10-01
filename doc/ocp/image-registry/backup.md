```
spec:
  defaultRoute: true
  httpSecret: 473047b4638a002cd1e917e8d19bf3fa1df2b3a163aa9d3bd4ec39644e50179ccdfe7c23912baeb52073e131668994c1291e75811a54026739b3e8ef4eb2f602
  logLevel: Normal
  managementState: Removed
  observedConfig: null
  operatorLogLevel: Normal
  proxy: {}
  replicas: 1                                                                                                                                                                                                                                                    
  requests:                                                                                                                                                                                                                                                      
    read:                                                                                                                                                                                                                                                        
      maxWaitInQueue: 0s                                                                                                                                                                                                                                         
    write:                                                                                                                                                                                                                                                       
      maxWaitInQueue: 0s                                                                                                                                                                                                                                         
  rolloutStrategy: Recreate                                                                                                                                                                                                                                      
  storage:                                                                                                                                                                                                                                                       
    managementState: Managed                                                                                                                                                                                                                                     
    pvc:                                                                                                                                                                                                                                                         
      claim: image-registry-storage                                                                                                                                                                                                                              
  unsupportedConfigOverrides: null  
```

```
+----+--------------------------+--------+------+----+------------------------------------------+------------+------+---------------+---------------+-------+------+-----+
| ID | PVC                      | Status | Cron | DV | PV                                       | Mode       | Size | Access Mode   | Storage Class | Usage | Snap | Age |
+----+--------------------------+--------+------+----+------------------------------------------+------------+------+---------------+---------------+-------+------+-----+
| 1  | openshift-image-registry | Bound  |      |    | pvc-d3151f47-31e8-4396-bd6b-b684d6868918 | Filesystem | 30Gi | ReadWriteOnce | lvms-vg1      | ---   | --   | 23d |
|    | image-registry-storage   |        |      |    |                                          |            |      |               |               |       |      |     | 
+----+--------------------------+--------+------+----+------------------------------------------+------------+------+---------------+---------------+-------+------+-----+
```