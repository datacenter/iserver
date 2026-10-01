class K8sAuthWait():
    def __init__(self):
        pass

    def wait_auth(self, name, match_properties={}, break_properties={}, my_output=None, prompt='Auth', max_time=60):
        return self.wait_managed_object(
            'auth',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_auth(self, name, my_output=None, prompt='Auth', max_time=60):
        return self.wait_no_managed_object(
            'auth',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
    
    def wait_any_auth(self, my_output=None, prompt='Auth', max_time=360):
        return self.wait_any_managed_object(
            'auth',
            my_output=my_output,
            prompt='Wait for any %s [timeout:%ss]' % (prompt, max_time),
            max_time=max_time
        )

    def wait_auth_ready(self, name, max_time=600, my_output=None):
        return self.wait_auth(
            name, 
            match_properties={'ready':True}, 
            my_output=my_output, 
            max_time=max_time
        )