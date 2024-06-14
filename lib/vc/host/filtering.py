class VcHostFiltering():
    def __init__(self):
        pass

    def get_hosts_by_name(self, name, strict=True):
        mo_hosts = self.get_host_objects()
        if mo_hosts is None:
            return None

        hosts = []

        for mo_host in mo_hosts:
            mo_host_name = getattr(mo_host, 'name', None)
            if mo_host_name is None:
                continue

            if strict and mo_host_name == name:
                hosts.append(
                    mo_host
                )
                continue

            if name in mo_host_name:
                hosts.append(
                    mo_host
                )

        return hosts
