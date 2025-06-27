# Web Server

Web server section is required. ISO is uploaded there and bare metal server mounts ISO remotely using virtual media over http. No http proxy is expected between server IMC and web server.

Web server can be defined in cluster.json or in web.json file in the same directory.

## Public key authentication

```
    "web_server": {
        "ip": "10.3.3.3",
        "username": "user",
        "password": null,
        "ssh_public_key": "ssh-ed25519 AAAA...",
        "image_base_url": "http://10.3.3.3:8080",
        "image_upload_directory": "./image"
    },
```

Notes:
- password attribute can be skipped
- image_upload_directory may be relative to home-dir of username or absolute path
- server virtual media will be configured with image_base_url/generated.iso

## Password-based authentication

```
    "web_server": {
        "ip": "10.3.3.3",
        "username": "user",
        "password": null,
        "ssh_public_key": "ssh-ed25519 AAAA...",
        "image_base_url": "http://10.3.3.3:8080",
        "image_upload_directory": "./image"
    },
```

Notes:
- ssh_public_key attribute can be skipped
- image_upload_directory may be relative to home-dir of username or absolute path
- server virtual media will be configured with image_base_url/generated.iso

## Localhost

If iserver runs on the same machine where web server runs on

```
    "web_server": {
        "ip": "localhost",
        "image_base_url": "http://10.3.3.3:8080",
        "image_upload_directory": "/var/image"
    },
```

Notes:
- image_upload_directory must be absolute path
- server virtual media will be configured with image_base_url/generated.iso

[Back](../BareMetalCluster.md)
