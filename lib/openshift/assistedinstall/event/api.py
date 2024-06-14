class AssistedInstallEventApi():
    def __init__(self):
        self.assisted_install_event_api_version = 'v2'
        self.assisted_install_event_url = '%s/events' % (
            self.assisted_install_event_api_version
        )

    def get_assisted_install_event_mo(self):
        response = self.get_assisted_install_mo(
            self.assisted_install_event_url
        )
        return response
