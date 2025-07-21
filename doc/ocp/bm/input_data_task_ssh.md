# Task: ssh

- single ssh public key is defined at the global level of cluster.json file or in ssh.pub file
- add extra keys if needed by definining ssh.keys list or putting ssh public keys in ssh subdirectory

```
    "tasks": [
        {
            "ssh": {
                "keys": [
                    "ssh-ed25519 AAAA..."
                ]
            }
        }
    ]
```

[Back](./input_data_tasks.md)