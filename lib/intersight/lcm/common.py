import time
import json

from progress.bar import IncrementalBar

from lib.intersight import compute
from lib import isctl_helper
from lib import log_helper
from lib import output_helper
from lib.intersight.organization import main as organization
from lib.intersight.compute_server_setting import main as compute_server_setting
from lib.intersight.workflow import main as workflow
from lib.intersight.workflow_task_info import main as workflow_task_info
from lib.intersight import workflow_info


class LcmServerCommon():
    def __init__(self, iaccount, silent=False, verbose=False, debug=False, log_id=None):
        self.iaccount = iaccount
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.isctl = isctl_helper.Isctl(iaccount, log_id=log_id)
        self.compute_handler = compute.Compute(iaccount, log_id=log_id)
        self.workflow_handler = workflow.Workflow(iaccount, log_id=log_id)
        self.workflow_task_info_handler = workflow_task_info.WorkflowTaskInfo(iaccount, log_id=log_id)
        self.organization = organization.Organization(iaccount, log_id=log_id)
        self.server_setting_handler = compute_server_setting.ComputeServerSetting(iaccount, log_id=log_id)
        self.workflow_info_handler = workflow_info.WorkflowInfo(
            iaccount,
            silent=silent,
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug

        self.my_output.set_flags(self.flags['silent'], self.flags['verbose'], self.flags['debug'])

    def show_flags(self):
        self.my_output.dictionary(self.flags, title='Flags', stream='debug')

    def get_server_setting_id(self, device_moid):
        server_setting_id = self.server_setting_handler.get_id_by_device_moid(
            device_moid
        )
        if server_setting_id is None:
            self.log.error(
                'get_server_setting_id',
                'No server setting id for device moid: %s' % (device_moid)
            )
        return server_setting_id

    def get_server_workflow_info(self, servers_mo):
        settings = {}
        settings['workflow'] = 86400

        cache_ttl = 1
        self.compute_handler.set_cache(
            servers_mo,
            settings,
            cache_ttl
        )

        match_rules = {}
        servers_info = self.compute_handler.get_info(
            servers_mo,
            settings,
            match_rules,
            cache_ttl,
            prepare_cache=False
        )

        return servers_info

    def wait_workflows_start(self, servers, workflow_name, max_start_time=30):
        start_time = int(time.time())
        for server in servers:
            self.log.debug(
                'lcm_server_common.wait_workflows_start',
                'Server %s' % (
                    server['Moid']
                )
            )
            server['LcmWorkflowId'] = None

        if not self.flags['silent']:
            bar_handler = IncrementalBar('Workflows started', max=len(servers))
            bar_handler.goto(0)

        while True:
            workflows = self.workflow_handler.get_last()
            if workflows is None:
                if int(time.time()) - start_time > max_start_time:
                    self.my_output.error('Max start waiting time elapsed')
                    return None

                time.sleep(5)
                continue

            started = 0
            for server in servers:
                if server['LcmWorkflowId'] is not None:
                    started = started + 1
                    continue

                for workflow_item in workflows:
                    if not self.workflow_handler.is_server_workflow(server['Moid'], workflow_item):
                        continue

                    if workflow_item['Name'] != workflow_name:
                        continue

                    in_server_workflows = False
                    for server_workflow in server['Workflow']['Last']:
                        if workflow_item['Moid'] == server_workflow['Moid']:
                            in_server_workflows = True
                            break

                    if in_server_workflows:
                        continue

                    server['LcmWorkflowId'] = workflow_item['Moid']
                    self.log.debug(
                        'lcm_server_common.wait_workflows_start',
                        'Server %s Workflow %s' % (
                            server['Moid'],
                            workflow_item['Moid']
                        )
                    )
                    started = started + 1
                    break

            if not self.flags['silent']:
                bar_handler.goto(started)

            if started == len(servers):
                break

            if int(time.time()) - start_time > max_start_time:
                self.my_output.error('Max start waiting time elapsed')
                return None

            time.sleep(5)

        if not self.flags['silent']:
            bar_handler.finish()
            self.my_output.files_only('Workflows started: [#######################] %s/%s' % (len(servers), len(servers)))

        return servers

    def wait_workflows_end(self, servers, max_complete_time=60):
        start_time = int(time.time())

        if not self.flags['silent']:
            bar_handler = IncrementalBar('Workflows finished', max=len(servers))
            bar_handler.goto(0)

        while True:
            workflows = self.workflow_handler.get_last()
            if workflows is None:
                if int(time.time()) - start_time > max_complete_time:
                    self.my_output.error('Max start waiting time elapsed')
                    return None

                time.sleep(5)
                continue

            finished = 0
            for server in servers:
                server['__Output'] = {}
                server['LcmWorkflowFinished'] = False
                server['LcmWorkflowCompleted'] = False

                for workflow_item in workflows:
                    if workflow_item['Moid'] == server['LcmWorkflowId']:
                        server['LcmWorkflowStatus'] = workflow_item['Status']
                        server['LcmWorkflowInfo'] = self.workflow_handler.get_info(workflow_item)

                        if workflow_item['Status'] == 'COMPLETED':
                            server['LcmWorkflowFinished'] = True
                            server['LcmWorkflowCompleted'] = True
                            server['__Output']['LcmWorkflowStatus'] = 'Green'
                            finished = finished + 1

                        if workflow_item['Status'] == 'FAILED':
                            server['LcmWorkflowFinished'] = True
                            server['LcmWorkflowCompleted'] = False
                            server['__Output']['LcmWorkflowStatus'] = 'Red'
                            finished = finished + 1

                        break

            if not self.flags['silent']:
                bar_handler.goto(finished)

            if finished == len(servers):
                break

            if int(time.time()) - start_time > max_complete_time:
                self.my_output.error('Max complete waiting time elapsed')
                return None

            time.sleep(5)

        if not self.flags['silent']:
            bar_handler.finish()
            self.my_output.files_only('Workflows finished: [#######################] %s/%s' % (len(servers), len(servers)))

        for server in servers:
            self.log.debug(
                'lcm_server_common.wait_workflows_end',
                'Server %s Workflow %s Status %s Finished %s Completed %s' % (
                    server['Moid'],
                    server['LcmWorkflowId'],
                    server['LcmWorkflowStatus'],
                    server['LcmWorkflowFinished'],
                    server['LcmWorkflowCompleted']
                )
            )

        return servers

    def wait_workflows(self, servers, workflow_name, max_start_time=120, max_complete_time=120, summary=False, details=False):
        self.log.debug(
            'lcm_server_common.wait_workflows',
            workflow_name
        )

        servers = self.wait_workflows_start(servers, workflow_name, max_start_time=max_start_time)
        if servers is None:
            return False

        servers = self.wait_workflows_end(servers, max_complete_time=max_complete_time)
        if servers is None:
            return False

        if self.flags['silent']:
            return True

        if summary:
            headers = [
                'Server Moid',
                'Server Name',
                'Workflow ID',
                'Workflow Name',
                'Duration',
                'Status'
            ]

            order = [
                'Moid',
                'Name',
                'LcmWorkflowId',
                'LcmWorkflowInfo.Name',
                'LcmWorkflowInfo.Duration',
                'LcmWorkflowStatus'
            ]

            self.my_output.my_table(
                servers,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                table=True
            )

        success = True
        for server in servers:
            server_workflow_info = {}
            server_workflow_info['server'] = server
            server_workflow_info['workflow'] = server['LcmWorkflowInfo']
            server_workflow_info['tasks'] = self.workflow_task_info_handler.get_workflow_tasks_info(
                server['LcmWorkflowId']
            )
            if details:
                self.workflow_info_handler.print_workflow_info(server_workflow_info)
            else:
                self.workflow_info_handler.print_workflow_info(server_workflow_info, stream='info')
            success = success and server['LcmWorkflowFinished'] and server['LcmWorkflowCompleted']

        self.log.debug(
            'lcm_server_common.wait_workflows',
            json.dumps(
                servers,
                indent=4
            )
        )

        self.log.debug(
            'lcm_server_common.wait_workflows',
            'Success %s' % (
                success
            )
        )

        return success
