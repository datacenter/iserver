class K8sPodOpenshiftPrometheus():
    def __init__(self):
        self.openshift_prometheus_platform_pod_namespace = 'openshift-monitoring'
        self.openshift_prometheus_platform_pod_name = 'prometheus-k8s-0'
        self.openshift_prometheus_platform_pod_container = 'prometheus'
        self.openshift_prometheus_user_pod_namespace = 'openshift-user-workload-monitoring'
        self.openshift_prometheus_user_pod_name = 'prometheus-user-workload-0'
        self.openshift_prometheus_user_pod_container = 'prometheus'

    def get_openshift_prometheus_platform_exec(self, command):
        output = self.get_pod_exec(
            self.openshift_prometheus_platform_pod_namespace,
            self.openshift_prometheus_platform_pod_name, 
            command, 
            container=self.openshift_prometheus_platform_pod_container
        )
        return output
    
    def get_openshift_prometheus_user_exec(self, command):
        output = self.get_pod_exec(
            self.openshift_prometheus_user_pod_namespace,
            self.openshift_prometheus_user_pod_name, 
            command, 
            container=self.openshift_prometheus_user_pod_container
        )
        return output
