import time
import traceback


class K8sMutatingWebhookApi():
    def __init__(self):
        self.mutating_webhook_mo = None

    def get_mutating_webhook_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.mutating_webhook_mo is not None:
                return self.mutating_webhook_mo

        api_handler = self.get_api(cluster_type='standard', api_type='admission')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_mutating_webhook_configuration()

            self.mutating_webhook_mo = []
            for item in response.items:
                webhook_mo = self.convert_object(item.to_dict())
                self.mutating_webhook_mo.append(
                    webhook_mo
                )

            self.log.k8s(
                'get',
                'mutating_webhook',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_mutating_webhook_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'mutating_webhook',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'mutating_webhook',
            self.mutating_webhook_mo
        )

        return self.mutating_webhook_mo

    def delete_mutating_webhook_mo(self, name):
        api_handler = self.get_api(cluster_type='standard', api_type='admission')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            api_response = api_handler.delete_mutating_webhook_configuration(name)
            self.log.k8s(
                'delete',
                'mutating_webhook',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.delete_mutating_webhook_mo', traceback.format_exc())
            self.log.k8s(
                'delete',
                'mutating_webhook',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False
        
        return True
