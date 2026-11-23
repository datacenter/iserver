class K8sCsrWait():
    def __init__(self):
        pass

    def wait_certificate_issued(self, name, match_properties={'issued':True}, break_properties={}, my_output=None, prompt='CertificateSigningRequest', max_time=60):
        return self.wait_managed_object(
            'csr',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )