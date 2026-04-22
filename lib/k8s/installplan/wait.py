class K8sInstallplanWait():
    def __init__(self):
        pass

    def wait_installplan_ready(self, namespace, name, my_output=None, prompt='InstallPlan', max_time=600):
        return self.wait_managed_object(
            'installplan',
            name,
            namespace=namespace,
            match_properties={'ready':True},
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )