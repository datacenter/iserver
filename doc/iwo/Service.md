# Intersight Workload Optimizer

## Kubernetes Service

```
# iserver get iwo service --help

Usage: iserver.py get iwo service [OPTIONS]

  Get iwo kubernetes service

Options:
  --iaccount TEXT              Intersight account  [default: isctl]
  --name TEXT                  Filter by name
  --cluster TEXT               Filter by cluster
  --app TEXT                   Filter by application
  --stale                      Select stale
  --inactive                   Select inactive
  --critical                   Select critical
  --major                      Select major or critical
  --minor                      Select minor, major or critical
  --show-app                   Show service applications
  --show-actions               Show service actions
  -o, --output [default|json]  [default: default]
  --verbose                    Verbose output
  --debug                      Debug output
  --devel                      Developer output
  --help                       Show this message and exit.

Info: finished in 30 ms and logs saved in /tmp/iserver\d0bf52de09d5
```

Usage examples:
- [List of services](../iwo/ServiceList.md)
- [Filter by service name](../iwo/ServiceNameFilter.md)
- [Filter by kubernetes cluster](../iwo/ServiceClusterFilter.md)
- [Filter by severity](../iwo/ServiceSeverityFilter.md)
- [Multiple filtering rules](../iwo/ServiceMultiFilter.md)
- [Show applications related with service](../iwo/ServiceApp.md)
- [Filter by service application name](../iwo/ServiceAppFilter.md)
