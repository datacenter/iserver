import json
import openshift as oc


class OcpApiSubscription():
    def __init__(self):
        pass

    def is_ocp_subscription(self, subscription_name, subscription_namespace):
        if self.get_ocp_subscription(subscription_name, subscription_namespace) is None:
            return False
        return True

    def get_ocp_subscription(self, subscription_name, subscription_namespace):
        subscriptions = self.get_ocp_subscriptions()
        for subscription in subscriptions:
            if subscription['name'] == subscription_name and subscription['namespace'] == subscription_namespace:
                return subscription
        return None

    def get_ocp_subscriptions(self):
        subscriptions = []
        with oc.client_host(
            hostname=self.ocp_cluster_settings['parameters']['installer']['vm']['ip'],
            username=self.ocp_cluster_settings['parameters']['installer']['vm']['username'],
            password=self.ocp_cluster_settings['parameters']['installer']['vm']['password'],
            auto_add_host=True
            ):
            for obj in oc.selector('subscription', all_namespaces=True).objects():
                subscription = {}
                subscription['name'] = obj.name()
                subscription['namespace'] = obj.namespace()

                obj_json = json.loads(obj.as_json())
                subscription['spec'] = obj_json['spec']
                subscription['state'] = obj_json['status']['state']

                subscriptions.append(
                    subscription
                )

        return subscriptions
