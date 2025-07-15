# OpenShift - Bare Metal Cluster Life Cycle Management

## Input Data Model

Type | Name | Fixed filename | Section Required | Note
--- | --- | --- | --- | ---
File | [cluster.json](./bm/input_data_cluster.md) | True | True | Cluster definition file
File | [server.json](./bm/input_data_server.md) | True | True | cluster.server section
File | [proxy.json](./bm/input_data_proxy.md) | True | False | augments cluster with http proxy settings
File | [ssh.pub](./bm/input_data_ssh_pub.md) | True | True | cluster.ssh_public_key property
File | [web.json](./bm/input_data_web.md) | True | True | cluster.web_server section
File | [redfish.json](./bm/input_data_redfish.md) | True | True | augments cluster.server.redfish section with username and password
File | [tasks.json](./bm/input_data_tasks.md) | True | False | cluster.tasks section
File | [htpasswd](./bm/input_data_htpasswd.md) | False | False | htpasswd-formatted file referred in cluster.tasks.identity provider configuration
File | [fabric.json](./bm/input_data_fabric.md) | True | False | cluster.fabric section
File | [nmstate.yaml](./bm/input_data_nmstate.md) | False | True | nmstate-formatted file for interface configuration of the servers referred by cluster.server.nmstate value with variables
Directory | ssh | True | False | with any-name.pub files for extra SSH pubkey configuration enabled with cluster.tasks.ssh section
Directory | manifests | True | False | [Custom CNI manifests](./bm/input_data_cni.md) with optional variables defined in cluster.json

[Back](../BareMetalCluster.md)