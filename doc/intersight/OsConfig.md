# Operating System Configuration

Each combination of OS vendor and version that supports template-based installation, needs associated configuration file that will be attached upon boot time by SCU.

## Get

```
# iserver get os-config --help

Usage: iserver.py get os-config [OPTIONS]

  Get operating system configuration template

Options:
  --iaccount TEXT  Intersight account
  --vendor TEXT    Vendor Name
  --version TEXT   Version Name
  --id TEXT        Version ID
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example

```
# iserver get os-config --vendor Ubuntu --version "Ubuntu Server 22.04 LTS"

Validate input parameters...
Configuration file: Ubuntu2004AutoInstall [<id>]

#cloud-config
autoinstall:
  ...
```