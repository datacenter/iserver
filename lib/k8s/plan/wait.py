import time


class K8sPlanWait():
    def __init__(self):
        pass

    def wait_plan(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='Plan', max_time=60):
        return self.wait_managed_object(
            'plan',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_plan(self, namespace, name, max_time=60, my_output=None, prompt='Plan'):
        return self.wait_no_managed_object(
            'plan',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='Wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_plan_ready(self, namespace, name, max_time=360, break_on_invalid=True):
        start_time = int(time.time())
        while True:
            info = self.get_plan(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if break_on_invalid and not info['vms_found']:
                    return False
                
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_plan_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)

    def wait_plan_archived(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_plan(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if 'Archived' in info['conditions']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_plan',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)