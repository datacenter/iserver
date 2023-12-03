# Availability Zone

## Default output

```
# iserver get osp az --cluster pod1 -o json

Cluster: pod1
[
    {
        "__Output": {
            "availableTick": "Green"
        },
        "name": "ALL",
        "available": true,
        "availableTick": "\u2713",
        "host": [
            {
                "name": "AIO-server-1",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-compute",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:14.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-compute",
                "service_namesT": "nova-compute [\u2713]"
            },
            {
                "name": "AIO-server-2",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-compute",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:18.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-compute",
                "service_namesT": "nova-compute [\u2713]"
            },
            {
                "name": "AIO-server-3",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-compute",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:13.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-compute",
                "service_namesT": "nova-compute [\u2713]"
            },
            {
                "name": "compute-server-1",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-compute",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:13.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-compute",
                "service_namesT": "nova-compute [\u2713]"
            },
            {
                "name": "compute-server-2",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-compute",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:19.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-compute",
                "service_namesT": "nova-compute [\u2713]"
            }
        ]
    },
    {
        "__Output": {
            "availableTick": "Green"
        },
        "name": "internal",
        "available": true,
        "availableTick": "\u2713",
        "host": [
            {
                "name": "AIO-server-1",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-conductor",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:15.000000",
                        "updated_age": "1h0m"
                    },
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-scheduler",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:13.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-conductor, nova-scheduler",
                "service_namesT": "nova-conductor [\u2713], nova-scheduler [\u2713]"
            },
            {
                "name": "AIO-server-2",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-conductor",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:19.000000",
                        "updated_age": "1h0m"
                    },
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-scheduler",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:19.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-conductor, nova-scheduler",
                "service_namesT": "nova-conductor [\u2713], nova-scheduler [\u2713]"
            },
            {
                "name": "AIO-server-3",
                "service": [
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-conductor",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:20.000000",
                        "updated_age": "1h0m"
                    },
                    {
                        "__Output": {
                            "availableTick": "Green",
                            "activeTick": "Green"
                        },
                        "name": "nova-scheduler",
                        "available": true,
                        "availableTick": "\u2713",
                        "active": true,
                        "activeTick": "\u2713",
                        "updated_at": "2023-11-18T14:34:14.000000",
                        "updated_age": "1h0m"
                    }
                ],
                "service_names": "nova-conductor, nova-scheduler",
                "service_namesT": "nova-conductor [\u2713], nova-scheduler [\u2713]"
            }
        ]
    }
]
```

Developer

```
# iserver get osp az --cluster pod1 -o json

{
    "duration": 1914,
    "osp": {
        "read": true,
        "success": 1,
        "failed": 0,
        "mo": 1,
        "mo_time": 1414,
        "total_time": 1414
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 2
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-18 15:34:22.833430	True	1414	get	availability_zones
```

[[Back]](./AvailabilityZoneGet.md)