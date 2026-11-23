# Intersight OpenTelemtry Metrics into OpenShift Prometheus

If you prefer manual way, here goes the example based on [reference](https://github.com/cgascoig/intersight-otel/blob/main/examples/kubernetes/all-in-one.yaml) and adapted for OpenShift.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: intersight-otel
spec:
  selector:
    matchLabels:
      app: intersight-otel
  template:
    metadata:
      labels:
        app: intersight-otel
        component: otel-collector
    spec:
      containers:
        - name: intersight-otel
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - all
            privileged: false
            readOnlyRootFilesystem: true
          image: ghcr.io/cgascoig/intersight-otel:v0.1.2
          command:
            - "/target/release/intersight_otel"
            - "-c"
            - "/etc/intersight-otel/intersight-otel.toml"
          env:
            - name: HTTPS_PROXY
              value: "http://proxy.domain.com:80"
            - name: RUST_LOG
              value: "info"
            - name: intersight_otel_key_file
              value: /etc/intersight-otel-key/intersight.pem
            - name: intersight_otel_key_id
              valueFrom:
                secretKeyRef:
                  name: intersight-api-credentials
                  key: intersight-key-id
          resources:
            requests:
              cpu: 100m
              memory: 64Mi
            limits:
              cpu: 200m
              memory: 128Mi
          volumeMounts:
            - name: intersight-otel-config
              mountPath: /etc/intersight-otel
              readOnly: true
            - name: intersight-otel-key
              mountPath: /etc/intersight-otel-key
              readOnly: true
        - command:
            - "/otelcol"
            - "--config=/conf/otel-collector-config.yaml"
          image: otel/opentelemetry-collector:0.59.0
          name: otel-collector
          resources:
            limits:
              cpu: 1
              memory: 2Gi
            requests:
              cpu: 200m
              memory: 400Mi
          ports:
            - containerPort: 4317 # Default endpoint for OpenTelemetry receiver.
            - containerPort: 2112 # Prometheus exporter
          volumeMounts:
            - name: otel-collector-config-vol
              mountPath: /conf
      volumes:
        - name: intersight-otel-config
          configMap:
            name: intersight-otel-config
        - name: intersight-otel-key
          secret:
            secretName: intersight-api-credentials
            items:
              - key: intersight-key
                path: intersight.pem
        - configMap:
            name: otel-collector-config
            items:
              - key: otel-collector-config
                path: otel-collector-config.yaml
          name: otel-collector-config-vol
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: intersight-otel-config
data:
  intersight-otel.toml: |
    otel_collector_endpoint = "http://127.0.0.1:4317"

    [[pollers]]
    name = "intersight.tam.advisory.count"
    otel_attributes = { scope = "total" }
    api_query = "api/v1/tam/AdvisoryInstances?$count=true"
    aggregator = "result_count"
    interval = 60
---
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
  labels:
    app: opentelemetry
    component: otel-collector
spec:
  ports:
    - name: prometheus-exporter
      port: 2112
  selector:
    component: otel-collector
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  labels:
    app: opentelemetry
    component: otel-collector-config
data:
  otel-collector-config: |
    receivers:
      otlp:
        protocols:
          grpc:
          http:
    processors:
      batch:
      memory_limiter:
        # 80% of maximum memory up to 2G
        limit_mib: 1500
        # 25% of limit up to 2G
        spike_limit_mib: 512
        check_interval: 5s
    extensions:
      zpages: {}
    exporters:
      prometheus:
        endpoint: ":2112"
        send_timestamps: true
        metric_expiration: 180m
        enable_open_metrics: true
        resource_to_telemetry_conversion:
          enabled: true
    service:
      extensions: [zpages]
      pipelines:
        metrics:
          receivers: [otlp]
          processors: [memory_limiter, batch]
          exporters: [prometheus]
---
piVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: intersight-otel
spec:
  endpoints:
  - interval: 30s
    port: prometheus-exporter
    scheme: http
    path: /metrics
  selector:
    matchLabels:
      app: opentelemetry
```