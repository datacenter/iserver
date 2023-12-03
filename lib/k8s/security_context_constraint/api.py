import time
import traceback


class K8sSecurityContextConstraintApi():
    def __init__(self):
        self.security_context_constraint_mo = None

    def get_security_context_constraint_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.security_context_constraint_mo is not None:
                return self.security_context_constraint_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='security.openshift.io/v1',
                kind='SecurityContextConstraints'
            )
            self.security_context_constraint_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'security_context_constraint',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_security_context_constraint_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'security_context_constraint',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'security_context_constraint',
            self.security_context_constraint_mo
        )

        return self.security_context_constraint_mo
