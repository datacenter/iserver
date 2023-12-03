class NfvoVnfiGet():
    def __init__(self):
        self.vnfi_plans = None
        self.vnfi = None

    def is_vnfi(self, vnfi_name):
        vnfi = self.get_vnfi(vnfi_name)
        if vnfi is None:
            return False
        return True

    def get_vnfis_count(self):
        vnfis = self.get_vnfis()
        if vnfis is None:
            return 0
        return len(vnfis)

    def get_vnfi_info(self, vnfi_mo):
        info = {}
        info['__Output'] = {}
        for key in vnfi_mo:
            info[key] = vnfi_mo[key]

        vim_ids = []
        for vim in vnfi_mo['resource-orchestration']['vim']:
            vim_ids.append(
                vim['vim-id']
            )
        info['vim-ids'] = ','.join(vim_ids)

        info['ready'] = self.is_vnfi_ready(vnfi_mo['name'])
        if info['ready']:
            info['readyTick'] = '\u2713'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['readyTick'] = '\u2717'
            info['__Output']['readyTick'] = 'Red'

        return info

    def get_vnfis_info(self):
        vnfis = self.get_vnfis()

        info = []
        if vnfis is not None:
            for vnfi_mo in vnfis:
                info.append(
                    self.get_vnfi_info(
                        vnfi_mo
                    )
                )

        return info

    def get_vnfis(self, output_format='json', cache=True, trace=None):
        if cache and self.vnfi is not None:
            return self.vnfi

        success = False
        response = None

        datastore = 'running'
        header = 'Accept'
        params = None

        if self.nfvo_version == '3.x':
            media_type = 'application/vnd.yang.data'
            if self.restconf_enabled:
                datapath = ('tailf-etsi-rel2-nfvo:nfvo', 'vnf-info')
            else:
                datapath = ('nfvo', 'vnf-info')

        if self.nfvo_version == '4.x':
            media_type = 'application/vnd.yang.collection'
            if self.restconf_enabled:
                datapath = ('etsi-nfv-descriptors:nfv', 'cisco-etsi-nfvo:vnf-info')
            else:
                datapath = ('nfv', 'vnf-info')
                params = 'deep'

        success, response = self.api_handler.get_data(
            output_format,
            datastore,
            datapath,
            header=header,
            media_type=media_type,
            params=params,
            trace=trace
        )

        if not success or response is None:
            self.log.error(
                'nso.get_vnfis',
                'Failure: %s' % (response)
            )
            return None

        if self.nfvo_version == '3.x':
            if 'vnf-deployment' in response['tailf-etsi-rel2-nfvo:vnf-info']['tailf-etsi-rel2-nfvo-esc:esc']:
                response = response['tailf-etsi-rel2-nfvo:vnf-info']['tailf-etsi-rel2-nfvo-esc:esc']['vnf-deployment']
            else:
                response = None

        if self.nfvo_version == '4.x':
            response = response['collection']['cisco-etsi-nfvo:vnf-info']

        return response

    def get_vnfi(self, vnfi_name, output_format='json', trace=None):
        success = False
        response = None

        if self.nfvo_version == '3.x':
            return False, 'Unsupported NFVO 3.x version'

        if self.nfvo_version == '4.x' and not self.restconf_enabled:
            return False, 'REST API not supported for NFVO 4.x'

        success, response = self.api_handler.get_data(
            output_format,
            'running',
            (
                'etsi-nfv-descriptors:nfv',
                'cisco-etsi-nfvo:vnf-info=%s' % (vnfi_name),
            ),
            header='Accept',
            media_type='application/vnd.yang.data',
            params=None,
            trace=trace
        )

        if not success or response is None:
            self.log.error(
                'nso.get_vnfi',
                'Failure: %s' % (response)
            )
            return None

        if self.nfvo_version == '4.x' and output_format == 'json':
            response = response['cisco-etsi-nfvo:vnf-info']

        return response

    def is_vnfi_ready(self, vnfi_name, cache=True):
        plan = self.get_vnfi_plan(vnfi_name, cache=cache)
        if plan is None:
            return False

        ready = True
        for component in plan['plan']['component']:
            for state in component['state']:
                if state['name'] == 'tailf-ncs:ready':
                    if state['status'] != 'reached':
                        ready = False

        return ready

    def add_vnfi_plan_output(self, plan):
        for component in plan['plan']['component']:
            for state in component['state']:
                state['__Output'] = {}
                if state['status'] == 'reached':
                    state['__Output']['status'] = 'Green'
                else:
                    state['__Output']['status'] = 'Red'
        return plan

    def get_vnfis_plan(self, output_format='json', trace=None, cache=True):
        if cache and self.vnfi_plans is not None:
            return self.vnfi_plans

        success = False
        response = None

        if self.nfvo_version == '3.x':
            return False, 'Unsupported NFVO 3.x version'

        if self.nfvo_version == '4.x' and not self.restconf_enabled:
            return False, 'REST API not supported for NFVO 4.x'

        success, response = self.api_handler.get_data(
            output_format,
            'running',
            (
                'etsi-nfv-descriptors:nfv',
                'cisco-etsi-nfvo:vnf-info-plan',
            ),
            header='Accept',
            media_type='application/vnd.yang.data',
            params=None,
            trace=trace
        )

        if not success or response is None:
            self.log.error(
                'nso.get_vnfis_plan',
                'Failure: %s' % (response)
            )
            return None

        if self.nfvo_version == '4.x' and output_format == 'json':
            self.vnfi_plans = []

            vnfi_plans = response['cisco-etsi-nfvo:vnf-info-plan']
            if vnfi_plans is not None:
                for vnfi_plan in vnfi_plans:
                    self.vnfi_plans.append(
                        self.add_vnfi_plan_output(
                            vnfi_plan
                        )
                    )

        return self.vnfi_plans

    def get_vnfi_plan(self, vnfi_name, cache=True):
        plans = self.get_vnfis_plan(cache=cache)
        if plans is None:
            return None

        for plan in plans:
            if plan['name'] == vnfi_name:
                return plan

        return None
