# Data Science (AI) Operator - Get

## Workflow

- get ai operator state
- get auth state
- get data science cluster initialization state
- get data science cluster state

## Example

```
# iserver get ocp ai --cluster bm1

OpenShift Workflow - Data Science (AI) - Get Information
========================================================

OpenShift Cluster: bm1
Operator
--------
- subscription: redhat-ods-operator/rhods-operator
- channel: stable
- csv: rhods-operator.2.25.0

+----+------+--------------+----------------------+-------+
| ID | Auth | Admin Groups | Allowed Groups       | Ready |
+----+------+--------------+----------------------+-------+
| 1  | auth | rhods-admins | system:authenticated | ✓     |
+----+------+--------------+----------------------+-------+

+----+-------------------------------------+-----------------------------------+-------+
| ID | Data Science Cluster Initialization | Version                           | Ready |
+----+-------------------------------------+-----------------------------------+-------+
| 1  | default-dsci                        | OpenShift AI Self-Managed v2.25.0 | ✓     |
+----+-------------------------------------+-----------------------------------+-------+

+----+----------------------+-----------------------------------+-------+-------------------------+----------+---------------------------------------+-----------------+
| ID | Data Science Cluster | Version                           | Ready | Components              | Disabled | Release Name                          | Release Version |
+----+----------------------+-----------------------------------+-------+-------------------------+----------+---------------------------------------+-----------------+
| 1  | default-dsc          | OpenShift AI Self-Managed v2.25.0 | ✓     | ✓ Code Flare            | ---      | CodeFlare operator                    | 1.15.0          | 
|    |                      |                                   |       | ✓ Dashboard             |          | Kubeflow Pipelines                    | 2.5.0           | 
|    |                      |                                   |       | ✓ Data Science Pipeline |          | Feast                                 | 0.54.0          | 
|    |                      |                                   |       | ✓ Feast Operator        |          | KServe                                | v0.14.0         | 
|    |                      |                                   |       | ✓ Kserver               |          | kueue                                 | 0.11.6          | 
|    |                      |                                   |       | ✓ Kqueue                |          | Llama Stack                           | v0.2.22         | 
|    |                      |                                   |       | ✓ Llama Stack Operator  |          | Llama Stack Operator                  | v0.3.0          | 
|    |                      |                                   |       | ✓ Model Mesh Serving    |          | ModelMesh Serving                     | v0.12.0         | 
|    |                      |                                   |       | ✓ Model Registry        |          | Google ML Metadata                    | v1.14.0         | 
|    |                      |                                   |       | ✓ Ray                   |          | Kubeflow Model Registry               | latest          | 
|    |                      |                                   |       | ✓ Training Operator     |          | Open Data Hub Model Registry Operator | latest          | 
|    |                      |                                   |       | ✓ TrustyAI              |          | KubeRay                               | 1.4.0           | 
|    |                      |                                   |       | ✓ Workbench             |          | Kubeflow Training Operator            | 1.9.0           | 
|    |                      |                                   |       |                         |          | TrustyAI operator                     | v1.37.0         | 
|    |                      |                                   |       |                         |          | TrustyAI service                      | v0.28.0         | 
|    |                      |                                   |       |                         |          | TrustyAI LMEval driver                | v1.37.0         | 
|    |                      |                                   |       |                         |          | TrustyAI LMEval job                   | v0.4.8          | 
|    |                      |                                   |       |                         |          | TrustyAI Guardrails orchestrator      | 0.9.4           | 
|    |                      |                                   |       |                         |          | TrustyAI builtin detectors            | v0.2.0          | 
|    |                      |                                   |       |                         |          | TrustyAI sidecar gateway              | v0.2.1          | 
|    |                      |                                   |       |                         |          | Kubeflow Notebook Controller          | 1.10.0          | 
+----+----------------------+-----------------------------------+-------+-------------------------+----------+---------------------------------------+-----------------+

Dashboard
- default-dsc: https://rhods-dashboard-redhat-ods-applications.apps.bm1.ocp.domain.com
```

[[Back]](./README.md)