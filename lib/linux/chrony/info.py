class LinuxChronyInfo():
    def __init__(self):
        self.chrony_config = None
        self.chrony_tracking = None

    def get_chrony_config_info(self):
        if self.chrony_config is not None:
            return self.chrony_config

        chrony_config_mo = self.get_chrony_config_cmd()

        self.chrony_config = {}
        self.chrony_config['configuration'] = self.get_lines(chrony_config_mo)
        self.chrony_config['server'] = []
        self.chrony_config['pool'] = []

        servers = self.get_lines(chrony_config_mo, begin_pattern='server ', strip=True)
        if servers is not None:
            for server in servers:
                self.chrony_config['server'].append(
                    server.split(' ')[0]
                )

        pools = self.get_lines(chrony_config_mo, begin_pattern='pool ', strip=True)
        if pools is not None:
            for pool in pools:
                self.chrony_config['pool'].append(
                    pool.split(' ')[0]
                )

        return self.chrony_config

    def get_chrony_tracking_info(self):
        if self.chrony_tracking is not None:
            return self.chrony_tracking

        chrony_tracking_mo = self.get_chrony_tracking_cmd()

        self.chrony_tracking = {}
        self.chrony_tracking['__Output'] = {}
        self.chrony_tracking['reference'] = self.get_line(chrony_tracking_mo, 'Reference ID').split(':')[1].strip()
        self.chrony_tracking['stratum'] = self.get_line(chrony_tracking_mo, 'Stratum').split(':')[1].strip()
        self.chrony_tracking['time'] = self.get_line(chrony_tracking_mo, 'Ref time').split(':')[1].strip()
        self.chrony_tracking['system_time'] = self.get_line(chrony_tracking_mo, 'System time').split(':')[1].strip()
        self.chrony_tracking['last_offset'] = self.get_line(chrony_tracking_mo, 'Last offset').split(':')[1].strip()
        self.chrony_tracking['rms_offset'] = self.get_line(chrony_tracking_mo, 'RMS offset').split(':')[1].strip()
        self.chrony_tracking['frequency'] = self.get_line(chrony_tracking_mo, 'Frequency').split(':')[1].strip()
        self.chrony_tracking['residual_frequency'] = self.get_line(chrony_tracking_mo, 'Residual freq').split(':')[1].strip()
        self.chrony_tracking['skew'] = self.get_line(chrony_tracking_mo, 'Skew').split(':')[1].strip()
        self.chrony_tracking['root_delay'] = self.get_line(chrony_tracking_mo, 'Root delay').split(':')[1].strip()
        self.chrony_tracking['root_dispertion'] = self.get_line(chrony_tracking_mo, 'Root dispersion').split(':')[1].strip()
        self.chrony_tracking['update_interval'] = self.get_line(chrony_tracking_mo, 'Update interval').split(':')[1].strip()
        self.chrony_tracking['status'] = self.get_line(chrony_tracking_mo, 'Leap status').split(':')[1].strip()
        if self.chrony_tracking['status'] == 'Normal':
            self.chrony_tracking['__Output']['status'] = 'Green'
            self.chrony_tracking['ok'] = True
        else:
            self.chrony_tracking['__Output']['status'] = 'Red'
            self.chrony_tracking['ok'] = False

        return self.chrony_tracking
