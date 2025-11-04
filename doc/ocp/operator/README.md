# OpenShift Operations

## Operator Life Cycle Management

One of the ways to manage operators in OpenShift cluster is via administrator UI:
- Operator -> OperatorHub shows all available operators
- Operator -> InstalledOperators shows all installed operators

Installation generic procedure:
- select operator
- adjust its installation parameters (channel, version, namespace)
- install operator
- wait until its ready to be further configured
- perform any follow-up configuration tasks once operator is installed

You can also delete edit subscription and uninstall operator via UI.

iserver offers similar features from the command line incl. post-operator-installation tasks. 
- use 'iserver get k8s package' to get the operators (see below).
- use 'iserver get|set|delete ocp [operator-name]' to control the life cycle of the operator.

## Get operators

Get all available operators with an indication (tick) if operator is already installed.

```
# iserver get k8s package --cluster my-cluster
Cluster: my-cluster (type: ocp)

Package [#689]
--------------

+-----------------------------------------------------+-----------+-------------------------------------------------+---------------------------+------------------------------------------------------------+
| Name                                                | Installed | Provider                                        | Channel                   | Version                                                    |
+-----------------------------------------------------+-----------+-------------------------------------------------+---------------------------+------------------------------------------------------------+
| 3scale-community-operator                           | ✗         | Red Hat                                         | threescale-2.13           | 3scale-community-operator.v0.10.1                          | 
| 3scale-operator                                     | ✗         | Red Hat                                         | threescale-2.15           | 3scale-operator.v0.12.3                                    | 

```

Filter operators by name.

```
# iserver get k8s package --name *nfd* --my-cluster
Cluster: my-cluster (type: ocp)

Package [#2]
------------

+------------------------+-----------+----------+---------+-------------------------+
| Name                   | Installed | Provider | Channel | Version                 |
+------------------------+-----------+----------+---------+-------------------------+
| nfd                    | ✗         | Red Hat  | stable  | nfd.4.18.0-202508201347 |
| openshift-nfd-operator | ✗         | Red Hat  | stable  | nfd.v4.10.0             |
+------------------------+-----------+----------+---------+-------------------------+

Filter: name, installed
View:   state (def), desc
```

Show only installed operators.

```
# iserver get k8s package --name *nfd* --my-cluster
Cluster: my-cluster (type: ocp)

Package [#15]
-------------

+-----------------------------+-----------+--------------------------+-------------+-------------------------------------------------+
| Name                        | Installed | Provider                 | Channel     | Version                                         |
+-----------------------------+-----------+--------------------------+-------------+-------------------------------------------------+
| cephcsi-operator            | ✓         | CephCSI Community        | stable-4.18 | cephcsi-operator.v4.18.9-rhodf                  |
| clife                       | ✓         | Isovalent, part of Cisco | 1.17        | clife.v1.17.7-cee.1                             |
| kubernetes-nmstate-operator | ✓         | Red Hat, Inc.            | stable      | kubernetes-nmstate-operator.4.18.0-202508271223 |
| kubevirt-hyperconverged     | ✓         | Red Hat                  | stable      | kubevirt-hyperconverged-operator.v4.18.13       |
| local-storage-operator      | ✓         | Red Hat                  | stable      | local-storage-operator.v4.18.0-202508201347     |
| lvms-operator               | ✓         | Red Hat                  | stable-4.18 | lvms-operator.v4.18.3                           |
| mcg-operator                | ✓         | NooBaa                   | stable-4.18 | mcg-operator.v4.18.9-rhodf                      |
| ocs-client-operator         | ✓         | Red Hat                  | stable-4.18 | ocs-client-operator.v4.18.9-rhodf               |
| ocs-operator                | ✓         | Red Hat                  | stable-4.18 | ocs-operator.v4.18.9-rhodf                      |
| odf-csi-addons-operator     | ✓         | CSI Addons Community     | stable-4.18 | odf-csi-addons-operator.v4.18.9-rhodf           |
| odf-dependencies            | ✓         | Red Hat                  | stable-4.18 | odf-dependencies.v4.18.9-rhodf                  |
| odf-operator                | ✓         | Red Hat                  | stable-4.18 | odf-operator.v4.18.9-rhodf                      |
| odf-prometheus-operator     | ✓         | Red Hat                  | stable-4.18 | odf-prometheus-operator.v4.18.9-rhodf           |
| recipe                      | ✓         | Red Hat, Inc.            | stable-4.18 | recipe.v4.18.9-rhodf                            |
| rook-ceph-operator          | ✓         | Red Hat                  | stable-4.18 | rook-ceph-operator.v4.18.9-rhodf                |
+-----------------------------+-----------+--------------------------+-------------+-------------------------------------------------+

Filter: name, installed
View:   state (def), desc
```

Show operator description (as long as provided in operator metadata)

```
# iserver get k8s package --name *odf* -v desc --my-cluster
Cluster: my-cluster (type: ocp)

Package [#7]
------------

+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| Name                          | Installed | Provider             | Channel     | Version                                     | Description                              |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| ibm-storage-odf-operator      | ✗         | IBM                  | stable-v1.8 | ibm-storage-odf-operator.v1.8.0             | IBM Storage ODF operator provides basic  |
|                               |           |                      |             |                                             | storage capabilities and extended        | 
|                               |           |                      |             |                                             | management functions through OpenShift   |
|                               |           |                      |             |                                             | data foundation framework for            |
|                               |           |                      |             |                                             | applications.                            |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-csi-addons-operator       | ✓         | CSI Addons Community | stable-4.18 | odf-csi-addons-operator.v4.18.9-rhodf       |                                          |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-dependencies              | ✓         | Red Hat              | stable-4.18 | odf-dependencies.v4.18.9-rhodf              |                                          |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-multicluster-orchestrator | ✗         | Red Hat              | stable-4.18 | odf-multicluster-orchestrator.v4.18.9-rhodf |                                          |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-node-recovery-operator    | ✗         | Red Hat, Inc.        | alpha       | odf-node-recovery-operator.v1.1.0           | ODF Node Recovery is an operator that    |
|                               |           |                      |             |                                             | assist in the recovery of and ODF        |
|                               |           |                      |             |                                             | cluster that has a device or a node      |
|                               |           |                      |             |                                             | replaced                                 | 
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-operator                  | ✓         | Red Hat              | stable-4.18 | odf-operator.v4.18.9-rhodf                  | OpenShift Data Foundation provides a     |
|                               |           |                      |             |                                             | common control plane for storage         |
|                               |           |                      |             |                                             | solutions on OpenShift Container         |
|                               |           |                      |             |                                             | Platform.                                |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+
| odf-prometheus-operator       | ✓         | Red Hat              | stable-4.18 | odf-prometheus-operator.v4.18.9-rhodf       | Manage the full lifecycle of             |
|                               |           |                      |             |                                             | configuring and managing Prometheus and  |
|                               |           |                      |             |                                             | Alertmanager servers.                    |
+-------------------------------+-----------+----------------------+-------------+---------------------------------------------+------------------------------------------+

Filter: name, installed
View:   state (def), desc
```

[[Back]](../Operations.md)