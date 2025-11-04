# OpenShift Container Platform (OCP)

## Bare Metal Cluster Installation - SNO w/Cilium CNI - REST API

### Requirements

What do you need first
- [pull secret](https://console.redhat.com/openshift/install/pull-secret)
- [access token](https://console.redhat.com/openshift/token)
- SSH public key to access the node later

### Get Access Token

REST POST API
- https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token
- Headers
  ```
  {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  ```
- Data
  ```
  {
    'grant_type': 'refresh_token',
    'client_id': 'cloud-services',
    'refresh_token': '<your-access-token>'
  }
  ```

Expected response in JSON format with access_token parameter. This value will have to be used in Authorization as bearer.

### Create cluster

Notes:
- at this stage you create cluster with OVN network type. It will be changed later to Cilium
- this example is for SNO that's why high_avaialability_mode is set to "None" value
- put the right ssh key and pull secret

REST POST API
- https://api.openshift.com/api/assisted-install/v2/clusters
- Headers
  ```
  {'Content-Type': 'application/json', 'Authorization': 'Bearer xyz'}
  ```
- Payload
  ```
  {
    "name": "<name>",
    "openshift_version": "4.15.11",
    "base_dns_domain": "domain.com",
    "ssh_public_key": "ssh-ed25519 xyz",
    "cpu_architecture": "x86_64",
    "cluster_network_cidr": "10.128.0.0/14",
    "cluster_network_host_prefix": 23,
    "service_network_cidr": "172.30.0.0/16",
    "high_availability_mode": "None",
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com",
    "network_type": "OVNKubernetes",
    "pull_secret": "abc"
  }
  ```

As the result you will get JSON with 'id' field, this will be your cluster-id that will be used in subsequent calls

### Change CNI to Cilium

PATCH REST API
- https://api.openshift.com/api/assisted-install/v2/clusters/your-cluster-id/install-config
- Headers
  ```
  {'Content-Type': 'application/json', 'Authorization': 'Bearer xyz'}
  ```
- Data
  ```
  {
    "networking": {
      "networkType": "Cilium"
    }
  }
  ```

### Create Infra

This step will augment installation data with the server networking details such as network.yaml, interface name + mac address.
Keep cluster_id attribute in JSON body to the value from create cluster step.

REST POST API
- https://api.openshift.com/api/assisted-install/v2/infra-envs
- Headers
  ```
  {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  ```
- Data
  ```
  {
      "openshift_version": "4.15.11",
      "ssh_authorized_key": "ssh-ed25519 xyz",
      "static_network_config": [
          {
              "network_yaml": "interfaces:\r\n- name: eno5\r\n  type: ethernet\r\n  state: up\r\n- name: eno6\r\n  type: ethernet\r\n  state: up\r\n- name: bond1\r\n  type: bond\r\n  state: up\r\n  link-aggregation:\r\n    mode: 802.3ad\r\n    options:\r\n      lacp_rate: slow\r\n    port:\r\n    - eno5\r\n    - eno6\r\n- name: bond1.666\r\n  type: vlan\r\n  state: up\r\n  vlan:\r\n    base-iface: bond1\r\n    id: 666\r\n  ipv4:\r\n    address:\r\n    - ip: 10.4.4.1\r\n      prefix-length: 28\r\n    dhcp: false\r\n    enabled: true\r\nroutes:\r\n  config:\r\n  - destination: 0.0.0.0/0\r\n    next-hop-address: 10.4.4.15\r\n    next-hop-interface: bond1.666\r\ndns-resolver:\r\n  config:\r\n    search:\r\n    - domain.com\r\n    server:\r\n    - 10.3.3.3",
              "mac_interface_map": [
                  {
                      "logical_nic_name": "eno5",
                      "mac_address": "aa:aa:aa:aa:aa:aa"
                  },
                  {
                      "logical_nic_name": "eno6",
                      "mac_address": "bb:bb:bb:bb:bb:bb"
                  }
              ]
          }
      ],
      "additional_trust_bundle": "",
      "proxy": {
          "no_proxy": "domain.com",
          "https_proxy": "http://proxy.domain.com:80",
          "http_proxy": "http://proxy.domain.com:80"
      },
      "image_type": "minimal-iso",
      "cluster_id": "<id>>",
      "pull_secret": "<pull-secret>",
      "cpu_architecture": "x86_64",
      "name": "<name>"
  }
  ```

### Upload manifests

Cilium has multiple manifest files. You need to upload them one-by-one using REST API as below

REST POST API
- https://api.openshift.com/api/assisted-install/v2/clusters/your-cluster-id/manifests
- Headers
  ```
  {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  ```
- Data
  ```
  {
    "file_name": "cluster-network-03-cilium-ciliumconfigs-crd.yaml",
    "folder": "manifests",
    "content": "<encoded_content>"}
  ```

The Python code example to generate the content

```
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
```

### Look at console

![WaitingForHost](images/waiting_for_host.png)

### Boot from ISO

Get cluster configuration state e.g. https://api.openshift.com/api/assisted-install/v2/clusters/your-cluster-id/install-config

It will have iso_url attribute

```
    "iso_url": "https://api.openshift.com/api/assisted-images/bytoken/some-token/4.15/x86_64/minimal.iso",
```

Download this ISO, uploade it to web server, configure server to boot from it (all via your preferred method e.g. Redfish)

### Track installatio progress

Run install-config and check state attributes of JSON response e.g.

```
    "status": "pending-for-input",
    "status_info": "User input required",
    "status_updated_at": "<data>",
```

That's how you will understand the progress of installation and if it was successful/in-progress/failed.

[[Back]](../BareMetalCluster.md)
