class K8sIsovalentBGPAdvertisementWait():
    def __init__(self):
        pass

    def wait_isovalent_bgp_advertisement(self, name, match_properties={}, break_properties={}, my_output=None, prompt='IsovalentBGPAdvertisement', max_time=360):
        return self.wait_managed_object(
            'isovalent_bgp_advertisement',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='Wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_isovalent_bgp_advertisement(self, name, my_output=None, prompt='IsovalentBGPAdvertisement', max_time=360):
        return self.wait_no_managed_object(
            'isovalent_bgp_advertisement',
            name,
            my_output=my_output,
            prompt='Wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )