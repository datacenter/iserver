from datetime import datetime, timezone
from kubernetes import client


class K8sCsrApi():
    def __init__(self):
        self.csr_mo = None

    def get_csr_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.csr_mo
        )
        if cache_hit:
            return response

        response, self.csr_mo = self.get_resources(
            'CertificateSigningRequest', 
            'certificates.k8s.io/v1', 
            self.csr_mo,
            name=name
        )

        return response

    def approve_csr_mo(self, name):
        api_handler = self.get_api(api_type='certificate')
        if api_handler is None:
            return False

        body = api_handler.read_certificate_signing_request_status(name)

        approval_condition = client.V1CertificateSigningRequestCondition(
            last_update_time=datetime.now(timezone.utc).astimezone(),
            message='This certificate was approved by iserver',
            reason='AsRequested',
            type='Approved',
            status='True')

        body.status.conditions = [approval_condition]

        try:
            response = api_handler.replace_certificate_signing_request_approval(name, body)
        except BaseException:
            return False
        
        self.increase_change_counter()
        return True