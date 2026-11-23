# OS Install with static IP

```
# iserver create os-install static --help

Usage: iserver.py create os-install static [OPTIONS]

  OS installation with static

Options:
  --iaccount TEXT      Intersight account  [default: isctl]
  --ip TEXT            Management IP address
  --name TEXT          Name loose match filter
  --serial TEXT        Serial number
  --scu TEXT           SCU Name
  --image TEXT         OS Image Name
  --interface TEXT     Interface name
  --mac TEXT           Interface mac address
  --address TEXT       IP address
  --prefix INTEGER     Prefix length
  --gateway TEXT       IP gateway
  --nameserver TEXT    Nameserver
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
# iserver create os-install static
    --serial Serial123
    --scu "mySCU"
    --image "myImage"
    --interface eno5
    --hostname kvm
    --password ******
    --address 10.1.1.1
    --prefix 24
    --gateway 10.1.1.2
    --nameserver 10.3.3.4
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