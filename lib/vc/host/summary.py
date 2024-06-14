import time


class VcHostSummary():
    def __init__(self):
        pass

    def add_host_summary_state_flag(self, host_info):
        color = ':'
        if host_info['runtime']['powerState'] == 'poweredOn':
            state = 'P+'
            color = '%sGG' % (color)
        else:
            state = 'P-'
            color = '%sRR' % (color)

        if host_info['runtime']['connectionState'] == 'connected':
            state = '%s C' % (state)
            color = '%s.G' % (color)
        else:
            state = '%s C' % (state)
            color = '%s.R' % (color)

        host_info['flagState'] = state
        host_info['__Output']['flagState'] = color

        return host_info

    def get_host_summary_info(self, mo_host, host_filter=None):
        info = {}
        info['__Output'] = {}

        info['name'] = mo_host['summary'].config.name
        if host_filter is not None:
            if not self.match_host(info, host_filter):
                return None

        hardware = mo_host['summary'].hardware
        info['serial'] = None
        for hardware_id in hardware.otherIdentifyingInfo:
            if hardware_id.identifierType.key == 'SerialNumberTag':
                info['serial'] = hardware_id.identifierValue

        info['hypervisor'] = mo_host['summary'].config.product.fullName

        keys = [
            'vendor',
            'model',
            'memorySize',
            'cpuModel',
            'cpuMhz',
            'numCpuPkgs',
            'numCpuCores',
            'numCpuThreads',
            'numNics',
            'numHBAs'
        ]
        for key in keys:
            info[key] = getattr(hardware, key)

        info['cpuSummary'] = '%s/%s/%s' % (
            info['numCpuPkgs'],
            info['numCpuCores'],
            info['numCpuThreads']
        )

        info['cpuCapacity'] = info['cpuMhz'] * info['numCpuCores']

        info['memoryUnit'] = self.convert_memory(
            info['memorySize']
        )

        runtime = mo_host['summary'].runtime
        keys = [
            'connectionState',
            'powerState',
            'standbyMode'
        ]
        info['runtime'] = {}
        for key in keys:
            info['runtime'][key] = getattr(runtime, key)

        stats = mo_host['summary'].quickStats
        keys = [
            'overallCpuUsage',
            'overallMemoryUsage',
            'distributedCpuFairness',
            'distributedMemoryFairness',
            'availablePMemCapacity',
            'uptime'
        ]
        info['stats'] = {}
        for key in keys:
            info['stats'][key] = getattr(stats, key)

        if info['stats']['overallCpuUsage'] is None:
            info['stats']['overallCpuUsagePct'] = '0%'
        else:
            info['stats']['overallCpuUsagePct'] = self.convert_pct(
                info['stats']['overallCpuUsage'] * 100 / info['cpuCapacity'],
                rounded=0
            )

        if info['stats']['overallMemoryUsage'] is None:
            info['stats']['overallMemoryUsagePct'] = '0%'
        else:
            info['stats']['overallMemoryUsagePct'] = self.convert_pct(
                info['stats']['overallMemoryUsage'] * 1024 * 1024 * 100 / info['memorySize'],
                rounded=0
            )

        info['overallStatus'] = mo_host['summary'].overallStatus

        info = self.add_host_summary_state_flag(info)

        return info

    def get_hosts_summary(self, host_filter=None):
        mo_hosts = self.get_hosts_properties(['summary'])
        if mo_hosts is None:
            return None

        start_time = int(time.time() * 1000)

        hosts = []
        for mo_host in mo_hosts:
            host_info = self.get_host_summary_info(mo_host, host_filter=host_filter)
            if host_info is not None:
                hosts.append(host_info)

        hosts = sorted(
            hosts,
            key=lambda i: i['name'].lower()
        )

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'get_hosts_summary',
            True,
            duration
        )

        return hosts

    def print_hosts_summary(self, info, title=False):
        if title:
            self.my_output.default(
                'Host [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'flagState',
            'name',
            'hypervisor',
            'serial',
            'model',
            'cpuSummary',
            'stats.overallCpuUsagePct',
            'memoryUnit',
            'stats.overallMemoryUsagePct',
            'numNics',
            'numHBAs'
        ]

        headers = [
            'SF',
            'Name',
            'Hypervisor',
            'Serial',
            'Model',
            'CPU',
            'Usage',
            'Memory',
            'Usage',
            'NICs',
            'HBAs'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
