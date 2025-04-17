# OS Install with DHCP

```
# iserver create os-install dhcp --help

Usage: iserver.py create os-install dhcp [OPTIONS]

  OS installation with dhcp

Options:
  --iaccount TEXT      Intersight account  [default: isctl]
  --ip TEXT            Management IP address
  --name TEXT          Name loose match filter
  --serial TEXT        Serial number
  --scu TEXT           SCU Name
  --image TEXT         OS Image Name
  --interface TEXT     Interface name
  --mac TEXT           Interface mac address
  --hostname TEXT      Hostname
  --password TEXT      Password
  --organization TEXT  Organization name
  --dry-run            Dry run  [default: False]
  --no-wait            Wait disabled  [default: False]
  --verbose            Verbose output  [default: False]
  --devel              Developer output  [default: False]
  --help               Show this message and exit.
```

## Basic execution

```
# iserver create os-install dhcp
    --serial Serial123
    --scu "myScu"
    --image "myImage"
    --interface eno5
    --hostname kvm
    --password ******
    --organization IntersightOrganization

Validate input parameters...
Power Cycle request: [#######################] 1/1
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| Moid-value                | Server123                       | Workflow-id               | COMPLETED        |
+---------------------------+---------------------------------+---------------------------+------------------+
Workflows started: [#######################] 1/1
Workflows finished: [#######################] 1/1

+---------------------------+---------------------------------+---------------------------+------------------+
| Server Moid               | Server Name                     | Workflow ID               | Workflow Status  |
+---------------------------+---------------------------------+---------------------------+------------------+
| Moid-value                | Server123                       | Workflow-id               | COMPLETED        |
+---------------------------+---------------------------------+---------------------------+------------------+
OS installation successful
```
