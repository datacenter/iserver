class K8sMutatingWebhookDelete():
    def __init__(self):
        pass
        
    def delete_mutating_webhook(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Mutating Webhook', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))
                              
        mutating_webhook_info = self.get_mutating_webhook(name, cache_enabled=False)
        if mutating_webhook_info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True
        
        if not self.delete_mutating_webhook_mo(name):
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        if my_output is not None:
            my_output.default('Mutating webhook deleted', before_newline=True, after_newline=True)

        if not wait:
            return True
        
        if my_output is not None:
            my_output.default('Wait for no mutating webhook...')

        if not self.wait_no_mutating_webhook(name):
            if my_output is not None:
                my_output.error('timed out')
            return False

        return True    
    