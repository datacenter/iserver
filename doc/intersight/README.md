# Intersight

Uses Intersight API calls to provide the state and control on Intersight managed servers.

## Features

Inventory
- [Chassis](./ChassisInventory.md)
- [Server](./ServerInventory.md)
- Power and Thermal

Server Control
- [Power control](./PowerControl.md)
- [Locator LED control](./LedControl.md)
- [Operating System installation](./OsInstall.md)

Workflow
- [Workflows](./Workflows.md)
- [Workflow details](./Workflow.md)

## Requirements

- install [isctl](https://github.com/cgascoig/isctl) binary and make sure it is your path

```
$ isctl version
isctl version 0.2.6 (Git commit 64aafddd2c34dd854d8627f2032a4afa3b17c7db)
```

- check if isctl can be called by iserver

```
$ iserver --check-isctl
[SUCCESS] isctl found
isctl version 0.2.6 (Git commit 64aafddd2c34dd854d8627f2032a4afa3b17c7db)
```

## Intersight API authentication

iserver interacts with Intersight using REST API (via isctl) and it needs an API key. iserver stores the key id/pem under iaccount name that can be passed on every command run e.g.

```
$ iserver get server --iaccount <name>
```

Multiple iaccounts supported. Last used iaccount name becomes default one.

## Configuration of iaccount

Get Intersight API key:
- Login to the Intersight GUI.
- Generate a new API Key (under Settings -> API Keys). Choose "API key for OpenAPI schema version 2" as the API Key Purpose.
- Save the key locally and make a note of the key ID.

```
$ iserver settings iaccounts add --name lab --pem intersight-key.pem --key 5be4.../5f9.../627...
Added
```

Optionally define EU instance of intersight server using --server option.

```
$ iserver settings iaccounts get

+----------+-----------------------------------------+----------------+--------+
| iaccount | key file                                | server         | key id |
+----------+-----------------------------------------+----------------+--------+
| lab      | /home/cisco/.itool/iaccount/lab/key.pem | intersight.com | *****  |
+----------+-----------------------------------------+----------------+--------+
```

```
$ iserver get server --iaccount lab
iaccount lab (cache: 600 seconds)
Select servers...
Selected servers: 121
Collect server api objects...
Collect server information |################################| 121/121


Server Summary [#121]
---------------------

+-----------+-----+---------+--------------------------------+---------------------------+--------------------+-------------+---------------+--------------+-----------+
| SF        | MF  | WF (7d) | Name                           | Tag                       | Model              | Serial      | IP            | CPU          | Memory    |
+-----------+-----+---------+--------------------------------+---------------------------+--------------------+-------------+---------------+--------------+-----------+
| P+ W(2)   | Cri | --      | Server1                        | psirt:manual              | (R) UCSC-C220-M5SX | MYSERIAL    | 10.1.1.1      | 2S 40C 80T   | 384 [GiB] |
+-----------+-----+---------+--------------------------------+---------------------------+--------------------+-------------+---------------+--------------+-----------+
| P+ H      | Cri | --      | Server2                        | psirt:manual              | (R) UCSC-C220-M5SX | MYSERIAL    | 10.1.1.1      | 2S 40C 80T   | 384 [GiB] |
+-----------+-----+---------+--------------------------------+---------------------------+--------------------+-------------+---------------+--------------+-----------+
```

## Cache

iserver uses by default cache of all collected API objects with default TTL of 600 seconds.

```
# iserver settings iaccounts cache

Intersight Settings
-------------------
- Cache Enabled           : False
- Cache TTL [sec]         : 600
- Compute Cache Directory : C:\Users\akaliwod\.itool\compute
```

You can disable/enable the cache and control TTL value using the command as above with --enable and --ttl options.

```
# iserver settings iaccounts cache --enabled true

Intersight Settings
-------------------
- Cache Enabled           : True
- Cache TTL [sec]         : 600
- Compute Cache Directory : C:\Users\akaliwod\.itool\compute

# iserver settings iaccounts cache --enabled false

Intersight Settings
-------------------
- Cache Enabled           : False
- Cache TTL [sec]         : 600
- Compute Cache Directory : C:\Users\akaliwod\.itool\compute
```

[[Back]](../../README.md)