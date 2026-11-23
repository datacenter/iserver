# Container Runtime Policy - Get

## Workflow

- get chrony machine config (/etc/containers/policy.json)
- get actual machine container runtime policy config from every cluster node
- checks if configuration is the same on every node

## Example

```
# iserver get ocp cpolicy --cluster bm1


OpenShift Workflow - Get container runtime policy
=================================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok
- cluster node [10.10.10.10] [key:C:\Users\user\.itool\ocp-clusters\bm1\ssh.pub]: ok


Collecting data...


Container Policy Machine Configuration
--------------------------------------

Machine config: 01-master-container-runtime
Node: bm1-1, bm1-2, bm1-3
Path: /etc/containers/policy.json
~~~
{
    "default": [
        {
            "type": "insecureAcceptAnything"
        }
    ],
    "transports":
        {
            "docker-daemon":
                {
                    "": [{"type":"insecureAcceptAnything"}]
                }
        }
}
~~~

Machine config: 01-worker-container-runtime
Node: bm1-1, bm1-2, bm1-3
Path: /etc/containers/policy.json
~~~
{
    "default": [
        {
            "type": "insecureAcceptAnything"
        }
    ],
    "transports":
        {
            "docker-daemon":
                {
                    "": [{"type":"insecureAcceptAnything"}]
                }
        }
}
~~~

Container Policy Configuration
------------------------------

Configuration the same on all nodes

{
    "default": [
        {
            "type": "insecureAcceptAnything"
        }
    ],
    "transports": {
        "docker-daemon": {
            "": [
                {
                    "type": "insecureAcceptAnything"
                }
            ]
        }
    }
}
```

[[Back]](./README.md)