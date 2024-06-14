from lib import filter_helper
from lib import ip_helper
from lib import info_helper

class VersionInfo():
    def __init__(self):
        self.version = None

    def get_version_info(self, version_mo):
        if version_mo is None:
            return None

        # {
        #     "header_str": "Cisco Nexus Operating System (NX-OS) Software\nTAC support: http://www.cisco.com/tac\nCopyright (C) 2002-2022, Cisco and/or its affiliates.\nAll rights reserved.\nThe copyrights to certain works contained in this software are\nowned by other third parties and used and distributed under their own\nlicenses, such as open source.  This software is provided \"as is,\" and unless\notherwise stated, there is no warranty, express or implied, including but not\nlimited to warranties of merchantability and fitness for a particular purpose.\nCertain components of this software are licensed under\nthe GNU General Public License (GPL) version 2.0 or \nGNU General Public License (GPL) version 3.0  or the GNU\nLesser General Public License (LGPL) Version 2.1 or \nLesser General Public License (LGPL) Version 2.0. \nA copy of each such license is available at\nhttp://www.opensource.org/licenses/gpl-2.0.php and\nhttp://opensource.org/licenses/gpl-3.0.html and\nhttp://www.opensource.org/licenses/lgpl-2.1.php and\nhttp://www.gnu.org/licenses/old-licenses/library.txt.\n",
        #     "bios_ver_str": "05.47",
        #     "kickstart_ver_str": "9.3(9)",
        #     "nxos_ver_str": "9.3(9)",
        #     "bios_cmpl_time": "04/28/2022",
        #     "kick_file_name": "bootflash:///nxos.9.3.9.bin",
        #     "nxos_file_name": "bootflash:///nxos.9.3.9.bin",
        #     "kick_cmpl_time": "2/4/2022 7:00:00",
        #     "nxos_cmpl_time": "2/4/2022 7:00:00",
        #     "kick_tmstmp": "02/04/2022 09:54:27",
        #     "nxos_tmstmp": "02/04/2022 09:54:27",
        #     "chassis_id": "Nexus9000 C9336C-FX2 Chassis",
        #     "cpu_name": "Intel(R) Xeon(R) CPU D-1526 @ 1.80GHz",
        #     "memory": 24569944,
        #     "mem_type": "kB",
        #     "proc_board_id": "FDO23490E2Y",
        #     "host_name": "ipn12-eu-spdc",
        #     "bootflash_size": 115805708,
        #     "kern_uptm_days": 140,
        #     "kern_uptm_hrs": 19,
        #     "kern_uptm_mins": 21,
        #     "kern_uptm_secs": 46,
        #     "rr_usecs": 933674,
        #     "rr_ctime": "Thu Jul 20 14:00:18 2023",
        #     "rr_reason": "Module PowerCycled",
        #     "rr_sys_ver": "",
        #     "rr_service": "HW check by card-client",
        #     "plugins": "Core Plugin, Ethernet Plugin",
        #     "manufacturer": "Cisco Systems, Inc.",
        #     "TABLE_package_list": {
        #         "ROW_package_list": {
        #             "package_id": ""
        #         }
        #     }
        # }

        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name

        excludeded_keys = [
            'TABLE_package_list',
            'header_str'
        ]
        for key in version_mo:
            if key not in excludeded_keys:
                info[key] = version_mo[key]

        info['uptime'] = ''
        if info['kern_uptm_days'] > 0:
            info['uptime'] = '%s days ' % (info['kern_uptm_days'])

        info['uptime'] = '%s%s:%s:%s' % (
            info['uptime'],
            info['kern_uptm_hrs'],
            info['kern_uptm_mins'],
            info['kern_uptm_secs']
        )

        info['memory_size'] = '%s%s' % (
            info['memory'],
            info['mem_type']
        )
        if info['mem_type'] == 'kB':
            info['memory_size'] = self.info_handler.convert_memory(
                info['memory'] * 1024
            )

        return info

    def get_versions_info(self, local_cache_enabled=True, cache_enabled=True):
        if local_cache_enabled:
            if self.version is not None:
                return self.version

        managed_objects = self.get_version_mo(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if managed_objects is None:
            self.log.error(
                'get_versions_info',
                'No version managed objects: %s' % (self.nexus_name)
            )
            return None

        self.version = []
        for managed_object in managed_objects:
            self.version.append(
                self.get_version_info(
                    managed_object
                )
            )

        return self.version

    def match_version(self, version_info, version_filter):
        if version_filter is None or len(version_filter) == 0:
            return True

        for ap_rule in version_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_version',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_versions(self, object_filter=None, local_cache_enabled=True, cache_enabled=True):
        all_versions = self.get_versions_info(
            local_cache_enabled=local_cache_enabled,
            cache_enabled=cache_enabled
        )
        if all_versions is None:
            self.log.error(
                'get_versions',
                'Failed to get version: %s' % (self.nexus_name)
            )
            return None

        versions = []

        for version_info in all_versions:
            if not self.match_version(version_info, object_filter):
                continue

            versions.append(
                version_info
            )

        return versions
