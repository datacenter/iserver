# Tetragon Enterprise Operator - Disable Prometheus 

## Overview

Tetragon exposes a number of Prometheus metrics that can be used for two main purposes:
- monitoring the health of Tetragon itself
- monitoring the activity of processes observed by Tetragon

The metrics are exposed in two steps:
- Service CRD exposes monitoring endpoint
- ServiceMonitor CRD informs user-workload enabled Prometheus on how to scrape the metrics

## Workflow

- disable service monitor in tetragon agents

## Requirements

Tetragon Enterprise operator must be installed.

## Configurable options

```
# iserver delete ocp tetragon --mode prometheus
  --cluster TEXT            Cluster Name
```

## Example

```

```

[[Back]](./README.md)