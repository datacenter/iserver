import json


class LinuxLvInfo():
    def __init__(self):
        self.lv = None

    def get_lv_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in managed_object:
            info[key] = managed_object[key]

        info['names'] = [info['lv_name']]

        info['block_device'] = '%s:%s' % (
            info['lv_kernel_major'],
            info['lv_kernel_minor']
        )

        if info['pool_lv'] is None or len(info['pool_lv']) == 0:
            info['is_pool'] = True
        else:
            info['is_pool'] = False

        info['role'] = info['lv_role'].split(',')
        info['layout'] = info['lv_layout'].split(',')
        info['data_percentT'] = '%s%%' % (info['data_percent'])

        info['snapshotCount'] = 0
        info['snapshotCountT'] = '--'
        if len(info['lv_descendants']) > 0:
            info['snapshotCount'] = len(info['lv_descendants'].split(','))
            info['snapshotCountT'] = info['snapshotCount']

        return info

    def get_lvs_info(self, cache_enabled=True):
        if cache_enabled and self.lv is not None:
            return self.lv

        try:
            lvs_mo = json.loads(
                self.get_lv_cmd(cache_enabled=cache_enabled)
            )['report'][0]['lv']
        except BaseException:
            self.log.error(
                'get_lvs_info',
                'Commands output parsing failed'
            )
            return None
        
        self.lv = []
        for lv_mo in lvs_mo:
            self.lv.append(
                self.get_lv_info(
                    lv_mo
                )
            )

        for item in self.lv:
            if len(item['lv_descendants']) > 0:
                for snapshot in item['lv_descendants'].split(','):
                    for sitem in self.lv:
                        if sitem['lv_name'] == snapshot:
                            sitem['names'].append(
                                '[S] %s' % (item['lv_name'])
                            )

        return self.lv
        
    def get_lvs(self, include_pvc=False, name_filter=None, cache_enabled=True, include_snap=False):
        all_lvs = self.get_lvs_info(cache_enabled=cache_enabled)
        if all_lvs is None:
            return None
        
        lvs = []
        descendants = []
        for item in all_lvs:
            if name_filter is None:
                lvs.append(item)
                continue

            if item['lv_name'] not in name_filter:
                continue

            lvs.append(item)
            if include_snap:
                if len(item['lv_descendants']) > 0:
                    for descendant in item['lv_descendants'].split(','):
                        if descendant not in descendants:
                            descendants.append(descendant)

        if len(descendants) > 0:
            for item in all_lvs:
                if item['lv_name'] in descendants:
                    lvs.append(item)

        if include_pvc:
            pvcs = None
            ocp_handler = self.get_ocp_handler()
            if ocp_handler is not None:
                pvcs = ocp_handler.k8s_handler.get_pvcs(
                    usage_info=True,
                    cache_enabled=cache_enabled
                )

            descendants = {}
            for item in lvs:
                item['orphan'] = True
                item['usage'] = '--'
                item['pvc'] = None
                item['snapshot'] = None

                if pvcs is not None:
                    for pvc in pvcs:
                        if item['lv_name'] == pvc['csi_handle']:
                            item['pvc'] = pvc['namespace_name']

                for descendant in item['lv_descendants'].split(','):
                    descendants[descendant] = item['pvc']

            for item in lvs:
                if item['is_pool']:
                    item['orphan'] = False
                    item['usage'] = 'N/A'
                    continue

                if item['pvc'] is not None:
                    item['orphan'] = False
                    item['usage'] = '(pvc) %s' % (item['pvc'])
                    continue

                if item['lv_name'] in descendants:
                    item['orphan'] = False
                    item['usage'] = '(snap) %s' % (descendants[item['lv_name']])
                    continue

        self.log.linux_mo(
            '%s.lv' % (self.server_display_name),
            lvs
        )

        return lvs
