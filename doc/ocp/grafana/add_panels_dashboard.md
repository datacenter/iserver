# Grafana Operator - Dashboard with panels (as-a-code)

Assume that you want to have panel(s) visualizing the Prometheus metrics e.g, 

## Single Panel

```
apiVersion: grafana.integreatly.org/v1beta1
kind: GrafanaDashboard
metadata:
  name: dashboard2
  namespace: grafana-operator
spec:
  instanceSelector:
    matchLabels:
      dashboards: test
  folder: 'my-tests'
  json: |
    {
      "title": "my-dashboard-with-panels",
      "uid" : "my-dashboard-with-panels-id",
      "panels": [
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          }
        }
      ]
    }
```

Notes:
- replace datasource.uid with prometheus datasource of your Grafana instance

![Content](../images/grafana/panel_dashboard_content.png)

## Multiple Panels

```
    {
      "title": "my-dashboard-with-panels",
      "uid" : "my-dashboard-with-panels-id",
      "panels": [
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          }
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          }
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          }
        }
      ]
    }
```

![Content](../images/grafana/panel2_dashboard_content.png)

## GridPos

[GridPos](https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/view-dashboard-json-model/): 
- w 1-24 (the width of the dashboard is divided into 24 columns)
- h in grid height units, each represents 30 pixels
- x The x position, in same unit as w
- y The y position, in same unit as h
- The grid has a negative gravity that moves panels up if there is empty space above a panel.
- No horizontal gravity

The rules above explain
- A12 has y:1 but is still aligned with A10-A11 due to negative gravity
- the same applies for A21
- think "tetris" game essentially

```
    {
      "title": "my-dashboard-with-panels",
      "uid" : "my-dashboard-with-panels-id",
      "panels": [
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 6,
            "x": 0,
            "y": 0
          },
          "title": "A10"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 3,
            "w": 4,
            "x": 7,
            "y": 0
          },
          "title": "A11"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 11,
            "y": 1
          },
          "title": "A12"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 6,
            "x": 0,
            "y": 5
          },
          "title": "A20"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 3,
            "w": 4,
            "x": 7,
            "y": 5
          },
          "title": "A21"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 11,
            "y": 5
          },
          "title": "A22"
        }
      ]
    }
```

![Content](../images/grafana/panel3_dashboard_content.png)

## Row

Note:
- row limits horizontal gravity

```
    {
      "title": "my-dashboard-with-panels",
      "uid" : "my-dashboard-with-panels-id",
      "panels": [
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 0
          },
          "panels": [],
          "title": "Row1",
          "type": "row"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 6,
            "x": 0,
            "y": 0
          },
          "title": "A10"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 3,
            "w": 4,
            "x": 7,
            "y": 0
          },
          "title": "A11"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 11,
            "y": 1
          },
          "title": "A12"
        },
        {
          "collapsed": false,
          "gridPos": {
            "h": 1,
            "w": 24,
            "x": 0,
            "y": 5
          },
          "panels": [],
          "title": "Row2",
          "type": "row"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 6,
            "x": 0,
            "y": 6
          },
          "title": "A20"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 3,
            "w": 4,
            "x": 7,
            "y": 6
          },
          "title": "A21"
        },
        {
          "datasource": {
            "uid": "da183399-bccb-40c4-902e-d672321d193a",
            "type": "prometheus"
          },
          "gridPos": {
            "h": 4,
            "w": 2,
            "x": 11,
            "y": 6
          },
          "title": "A22"
        }
      ]
    }
```

![Content](../images/grafana/panel4_dashboard_content.png)

[[Back]](./README.md)