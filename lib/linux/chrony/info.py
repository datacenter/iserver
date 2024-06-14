class LinuxChronyInfo():
    def __init__(self):
        self.chrony_config = None
        self.chrony_tracking = None

    def get_chrony_config_info(self):
        if self.chrony_config is not None:
            return self.chrony_config

        chrony_config_mo = self.get_chrony_config_cmd()

        # pool 0.rhel.pool.ntp.org iburst
        # driftfile /var/lib/chrony/drift
        # makestep 1.0 3
        # rtcsync
        # logdir /var/log/chrony
        # server <fqdn> iburst prefer

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

        # Reference ID    : AD26C943 (fqdn)
        # Stratum         : 2
        # Ref time (UTC)  : Fri Apr 19 11:48:32 2024
        # System time     : 0.000012511 seconds fast of NTP time
        # Last offset     : -0.000027058 seconds
        # RMS offset      : 0.000115619 seconds
        # Frequency       : 13.625 ppm slow
        # Residual freq   : -0.000 ppm
        # Skew            : 0.031 ppm
        # Root delay      : 0.020759970 seconds
        # Root dispersion : 0.001136309 seconds
        # Update interval : 1028.0 seconds
        # Leap status     : Normal

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
