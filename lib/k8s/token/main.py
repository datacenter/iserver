import json
import time
import traceback
from kubernetes import client


class K8sToken():
    def __init__(self):
        pass

    def get_service_account_token(self, sa_namespace, sa_name, expiration_seconds=4294967296):
        api_handler = self.get_api(cluster_type='standard')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            body = client.AuthenticationV1TokenRequest(
                api_version='authentication.k8s.io/v1',
                kind='TokenRequest',
                spec=client.V1TokenRequestSpec(
                    audiences=[],
                    expiration_seconds=expiration_seconds
                )
            )

            response = api_handler.create_namespaced_service_account_token(sa_name, sa_namespace, body)
        except BaseException:
            self.log.error('k8s.get_service_account_token', traceback.format_exc())
            self.log.k8s(
                'get',
                'get_service_account_token',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        try:
            token = getattr(getattr(response, 'status'), 'token')
        except BaseException:
            self.log.error('k8s.get_service_account_token', traceback.format_exc())
            self.log.k8s(
                'get',
                'get_service_account_token',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        return token
