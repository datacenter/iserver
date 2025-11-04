# OpenShift Console API

Certain iserver features such as cluster installation, use OpenShift Console API access. One-time configuration is required to properly authenticate.

## Requirement

You must have valid accout at [RedHat Openshift console](https://console.redhat.com)

## Step 1: Get pull secret from RedHat Console

Downloaded pull secret using this [link](https://console.redhat.com/openshift/install/pull-secret)

![PullSecret](./images/pull_secret.png)

## Step 2: Get token from RedHat Console

Access OpenShift Cluster Manager API Token page using this [link](https://console.redhat.com/openshift/token), click 'Load Token' button and save API token to local file

![Token](./images/token.png)

## Step 3: Configure iserver

Run single iserver command as below with token and pull secret passed via filenames. iserver will cache these credentials in its internal structure and use it later for any OpenShift console rest api transactions.

```
# iserver set ocp console --token C:\tmp\token.txt --secret C:\tmp\pull-secret.txt

OpenShift Workflow - OpenShift Console REST API - Configure access
==================================================================

Openshift settings directory will be created: C:\Users\user\.itool\openshift
Token saved: C:\Users\user\.itool\openshift\token
Pull secret saved: C:\Users\user\.itool\openshift\pull_secret.txt
OpenShift console connection successful
```

[[Back]](./Operations.md)