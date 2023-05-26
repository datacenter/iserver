from lib import log_helper
from lib import output_helper

from lib.iwo.action import IwoAction
from lib.iwo.application import IwoApplication
from lib.iwo.chassis import IwoChassis
from lib.iwo.client import IwoClient
from lib.iwo.cluster import IwoCluster
from lib.iwo.container import IwoContainer
from lib.iwo.dc import IwoDataCenter
from lib.iwo.disk import IwoDisk
from lib.iwo.namespace import IwoNamespace
from lib.iwo.network import IwoNetwork
from lib.iwo.phy import IwoPhysicalMachine
from lib.iwo.pod import IwoPod
from lib.iwo.region import IwoRegion
from lib.iwo.service import IwoService
from lib.iwo.spec import IwoSpec
from lib.iwo.storage import IwoStorage
from lib.iwo.switch import IwoSwitch
from lib.iwo.target import IwoTarget
from lib.iwo.workload import IwoWorkload
from lib.iwo.vdc import IwoVirtualDataCenter
from lib.iwo.vm import IwoVirtualMachine
from lib.iwo.volume import IwoVolume
from lib.iwo.zone import IwoZone


class Iwo(
    IwoAction,
    IwoApplication,
    IwoChassis,
    IwoClient,
    IwoCluster,
    IwoContainer,
    IwoDataCenter,
    IwoDisk,
    IwoNamespace,
    IwoNetwork,
    IwoPhysicalMachine,
    IwoPod,
    IwoRegion,
    IwoService,
    IwoSpec,
    IwoStorage,
    IwoSwitch,
    IwoTarget,
    IwoWorkload,
    IwoVirtualDataCenter,
    IwoVirtualMachine,
    IwoVolume,
    IwoZone
    ):
    def __init__(self, iaccount, verbose=False, debug=False, log_id=None):
        self.verbose = verbose
        self.debug = debug
        self.log_id = log_id

        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        IwoAction.__init__(self)
        IwoApplication.__init__(self)
        IwoChassis.__init__(self)
        IwoClient.__init__(self, iaccount)
        IwoCluster.__init__(self)
        IwoContainer.__init__(self)
        IwoDataCenter.__init__(self)
        IwoDisk.__init__(self)
        IwoNamespace.__init__(self)
        IwoNetwork.__init__(self)
        IwoPhysicalMachine.__init__(self)
        IwoPod.__init__(self)
        IwoRegion.__init__(self)
        IwoService.__init__(self)
        IwoSpec.__init__(self)
        IwoStorage.__init__(self)
        IwoSwitch.__init__(self)
        IwoTarget.__init__(self)
        IwoWorkload.__init__(self)
        IwoVirtualDataCenter.__init__(self)
        IwoVirtualMachine.__init__(self)
        IwoVolume.__init__(self)
        IwoZone.__init__(self)

    def map_state_color(self, state):
        if state.lower() == 'active':
            return 'Green'

        if state.lower() == 'maintenance':
            return 'Yellow'

        return 'Red'

    def map_severity_color(self, severity):
        if severity.lower() == 'critical':
            return 'Red'

        if severity.lower() == 'major':
            return 'Yellow'

        if severity.lower() == 'minor':
            return 'Blue'

        return 'Green'

    def map_staleness_color(self, staleness):
        if staleness.lower() == 'stale':
            return 'Red'

        if staleness.lower() == 'current':
            return 'Green'

        return 'Yellow'

    def get_empty_summary(self):
        summary = {}
        summary['__Output'] = {}
        summary['total'] = 0
        summary['active'] = 0
        summary['critical'] = 0
        summary['major'] = 0
        summary['minor'] = 0
        summary['normal'] = 0
        summary['current'] = 0
        summary['stale'] = 0
        summary['state'] = ''
        summary['severity'] = ''
        summary['connected'] = ''
        return summary

    def get_summary(self, managed_objects):
        summary = self.get_empty_summary()
        summary['total'] = len(managed_objects)

        for managed_object in managed_objects:
            if managed_object['state'] == 'ACTIVE':
                summary['active'] = summary['active'] + 1

            if managed_object['severity'] == 'Critical':
                summary['critical'] = summary['critical'] + 1

            if managed_object['severity'] == 'Major':
                summary['major'] = summary['major'] + 1

            if managed_object['severity'] == 'Minor':
                summary['minor'] = summary['minor'] + 1

            if managed_object['severity'] == 'Normal':
                summary['normal'] = summary['normal'] + 1

            if managed_object['staleness'] == 'CURRENT':
                summary['current'] = summary['current'] + 1

        summary['state'] = '%s/%s' % (
            summary['active'],
            summary['total']
        )

        summary['severity'] = '%s/%s/%s/%s' % (
            summary['critical'],
            summary['major'],
            summary['minor'],
            summary['normal']
        )
        summary['__Output']['severity'] = ':'

        if summary['critical'] == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'R'.rjust(len(str(summary['critical'])), 'R')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if summary['major'] == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'Y'.rjust(len(str(summary['major'])), 'Y')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if summary['minor'] == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'B'.rjust(len(str(summary['minor'])), 'B')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if summary['normal'] == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'G'.rjust(len(str(summary['normal'])), 'G')
            )

        summary['connected'] = '%s/%s' % (
            summary['current'],
            summary['total']
        )

        return summary

    def get_severity_summary(self, managed_objects):
        critical = 0
        major = 0
        minor = 0
        normal = 0
        for managed_object in managed_objects:
            if managed_object['severity'].lower() == 'critical':
                critical = critical + 1

            if managed_object['severity'].lower() == 'major':
                major = major + 1

            if managed_object['severity'].lower() == 'minor':
                minor = minor + 1

            if managed_object['severity'].lower() == 'normal':
                normal = normal + 1

        summary = {}
        summary['__Output'] = {}

        summary['severity'] = '%s/%s/%s/%s' % (
            critical,
            major,
            minor,
            normal
        )

        summary['__Output']['severity'] = ':'
        if critical == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'R'.rjust(len(str(critical)), 'R')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if major == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'Y'.rjust(len(str(major)), 'Y')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if minor == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'B'.rjust(len(str(minor)), 'B')
            )
        summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])

        if normal == 0:
            summary['__Output']['severity'] = '%s.' % (summary['__Output']['severity'])
        else:
            summary['__Output']['severity'] = '%s%s' % (
                summary['__Output']['severity'],
                'G'.rjust(len(str(normal)), 'G')
            )

        return summary

    def print_summary(self, managed_objects):
        summary = self.get_summary(managed_objects)

        order = [
            'state',
            'severity',
            'connected'
        ]

        headers = [
            'Active',
            'Severity',
            'Current'
        ]

        self.my_output.dictionary(
            summary,
            title='Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )
