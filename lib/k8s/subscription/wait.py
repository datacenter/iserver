import time


class K8sSubscriptionWait():
    def __init__(self):
        pass

    def wait_subscription_install_plan(self, namespace, name, max_time=360):
        start_time = int(time.time())
        while True:
            subscription = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if subscription is not None:
                if subscription['install_plan_name'] is not None:
                    return subscription['install_plan_name']

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_subscription_install_plan',
                    'Max time reached'
                )
                return None

            time.sleep(5)

    def wait_no_subscription(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            subscription_info = self.get_subscription(
                namespace,
                name,
                cache_enabled=False
            )
            if subscription_info is None:
                return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_no_subscription',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)