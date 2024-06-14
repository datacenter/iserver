from lib import output_helper

class ComputesWorkflow():
    """Class for servers' workflows
    """
    def __init__(self, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)

    def failed_workflow_match(self, workflow, failed):
        if not failed:
            return True

        if workflow['Status'] == 'FAILED':
            return True

        return False

    def completed_workflow_match(self, workflow, completed):
        if not completed:
            return True

        if workflow['Status'] == 'COMPLETED':
            return True

        return False

    def power_workflow_match(self, workflow, power):
        if not power:
            return True

        if workflow['Name'] in ['Power On', 'Power Off', 'Power Cycle', 'Reboot IMC', 'Shut Down OS', 'Hard Reset']:
            return True

        return False

    def os_workflow_match(self, workflow, os_filter):
        if not os_filter:
            return True

        if workflow['Name'] in ['InstallOS', 'Operating System Install']:
            return True

        return False

    def fw_workflow_match(self, workflow, fw_filter):
        if not fw_filter:
            return True

        # TBD !!!

        return False

    def match_workflow(self, workflow, settings):
        if not self.failed_workflow_match(workflow, settings['failed']):
            return False

        if not self.completed_workflow_match(workflow, settings['completed']):
            return False

        if not self.power_workflow_match(workflow, settings['power']):
            return False

        if not self.os_workflow_match(workflow, settings['os']):
            return False

        if not self.fw_workflow_match(workflow, settings['fw']):
            return False

        return True

    def get_servers_workflows(self, servers, settings):
        workflows = []

        for server in servers:
            if server['Workflow']['Running'] is not None:
                if self.match_workflow(server['Workflow']['Running'], settings):
                    workflow_info = {}
                    workflow_info['__Output'] = {}

                    workflow_info['server_id'] = server['Moid']
                    workflow_info['server_state'] = server['FlagState']
                    workflow_info['__Output']['server_state'] = server['__Output']['FlagState']
                    workflow_info['server_name'] = server['Name']
                    workflow_info['server_ip'] = server['ManagementIp']
                    workflow_info['server_serial'] = server['Serial']

                    workflow_info['workflow_id'] = server['Workflow']['Running']['Moid']
                    workflow_info['name'] = server['Workflow']['Running']['Name']
                    workflow_info['created'] = server['Workflow']['Running']['CreateTime']
                    workflow_info['created_epoch'] = server['Workflow']['Running']['CreateTimeEpoch']
                    workflow_info['duration'] = 'In progress...'

                    workflow_info['__Output']['status'] = 'Yellow'
                    workflow_info['status'] = 'RUNNING %s%%' % (server['Workflow']['Running']['Progress'])

                    workflows.append(workflow_info)

            count = settings['count']
            if count < 0:
                count = 1000

            for workflow_item in server['Workflow']['Last']:
                if self.match_workflow(workflow_item, settings):
                    workflow_info = {}
                    workflow_info['__Output'] = {}

                    workflow_info['server_id'] = server['Moid']
                    workflow_info['__Output']['server_state'] = server['__Output']['FlagState']
                    workflow_info['server_state'] = server['FlagState']
                    workflow_info['server_name'] = server['Name']
                    workflow_info['server_ip'] = server['ManagementIp']
                    workflow_info['server_serial'] = server['Serial']

                    workflow_info['workflow_id'] = workflow_item['Moid']
                    workflow_info['name'] = workflow_item['Name']
                    workflow_info['created'] = workflow_item['CreateTime']
                    workflow_info['created_epoch'] = workflow_item['CreateTimeEpoch']
                    workflow_info['duration'] = workflow_item['Duration']

                    workflow_info['__Output']['status'] = workflow_item['__Output']['Status']
                    workflow_info['status'] = workflow_item['Status']

                    workflows.append(workflow_info)
                    count = count - 1
                    if count == 0:
                        break

        if settings['sorted'] == 'date':
            workflows = sorted(workflows, key=lambda i: i['created_epoch'], reverse=True)

        if settings['sorted'] == 'server':
            workflows = sorted(workflows, key=lambda i: (i['server_name'], -i['created_epoch']))

        if settings['sorted'] == 'workflow':
            workflows = sorted(workflows, key=lambda i: (i['name'], -i['created_epoch']))

        return workflows

    def print_workflows(self, workflows):
        order = [
            'server_state',
            'server_name',
            'server_ip',
            'server_serial',
            'workflow_id',
            'name',
            'created',
            'duration',
            'status',
        ]

        headers = [
            'SF',
            'Server Name',
            'Server IP',
            'Serial',
            'Workflow ID',
            'Name',
            'Create Time',
            'Duration',
            'Status'
        ]

        self.my_output.my_table(
            workflows,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
