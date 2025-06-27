# Redfish authentication

iserver uses redfish to configure virtual media mount, boot order and trigger server reboot. It is defined per server in either [server](./input_data_server.md) section or redfish.json file.

## Server section in cluster.json

```
    "server": [
        {
            "hostname": "bm1-1"
            "redfish": {
                "username": "user",
                "password": "pass"
            }
        },
        {
            "hostname": "bm1-2"
            "redfish": {
                "username": "user",
                "password": "pass"
            }
        },
        {
            "hostname": "bm1-3"
            "redfish": {
                "username": "user",
                "password": "pass"
            }
        }
    ]
```

## server.json file

```
[
    {
        "hostname": "bm1-1"
        "redfish": {
            "username": "user",
            "password": "pass"
        }
    },
    {
        "hostname": "bm1-2"
        "redfish": {
            "username": "user",
            "password": "pass"
        }
    },
    {
        "hostname": "bm1-3"
        "redfish": {
            "username": "user",
            "password": "pass"
        }
    }
]
```

## redfish.json

```
{
    "username": "user",
    "password": "pass"
}
```

Note: in case of redfish.json, do not include redfish.username or redfish.password section in cluster.server. It will be overwritten anyway based on file content.

[Back](../BareMetalCluster.md)
