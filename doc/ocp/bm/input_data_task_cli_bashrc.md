# Task: cli bashrc

## Input Data Model

Minimum intent definition (showing tasks.cli content only for brevity)

```
{
    "bashrc": true
}
```

```
{
    "bashrc": {}
}
```

```
{
    "bashrc": {
        "enabled": true
    }
}
```

Complete input showing defaults based on proxy defaults of the cluster

```
{
    "enabled": true,
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com"
}
```

Configuration tips:
- set proxy settings to custom or empty values to avoid proxy.json inheritance

## Workflow

- download .bashrc from cluster management node selected with kube:true
- if proxy already defined, then exit
- modify .bashrc with proxy settings
- upload .bashrc

## Output

Example

```
Task cli bashrc
---------------
{
    "enabled": true,
    "http_proxy": "http://proxy.domain.com:80",
    "https_proxy": "http://proxy.domain.com:80",
    "no_proxy": "domain.com"
}
Download /var/home/core/.bashrc

export HTTP_PROXY=http://proxy.domain.com:80
export HTTPS_PROXY=http://proxy.domain.com:80
export NO_PROXY=domain.com


Upload /var/home/core/.bashrc
.bashrc uploaded with proxy settings
```

[Back](./input_data_tasks_cli.md)