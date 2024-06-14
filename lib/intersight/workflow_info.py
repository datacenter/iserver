import json

from lib import output_helper
from lib.intersight.workflow import main as workflow
from lib.intersight.workflow_task_info import main as workflow_task_info
from lib.intersight import compute


class WorkflowInfo():
    """Class for workflow info
    """
    def __init__(self, iaccount, silent=False, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        self.workflow_handler = workflow.Workflow(iaccount, log_id=log_id)
        self.workflow_task_info_handler = workflow_task_info.WorkflowTaskInfo(iaccount, log_id=log_id)
        self.compute_handler = compute.Compute(iaccount, log_id=log_id)

        self.flags = {}
        self.flags['silent'] = silent
        self.flags['verbose'] = verbose
        self.flags['debug'] = debug

        self.my_output.set_flags(self.flags['silent'], self.flags['verbose'], self.flags['debug'])

    def get_workflow_server_id(self, workflow_object):
        if workflow_object['AssociatedObject']['ObjectType'] in ['compute.RackUnit', 'compute.Blade']:
            return workflow_object['AssociatedObject']['Moid']

        if workflow_object['Name'] == 'Operating System Install':
            return workflow_object['Input']['Server']['Moid']

        if workflow_object['Name'] == 'InstallOS':
            return workflow_object['Input']['Server']['Moid']

        self.my_output.debug('Failed to detect server identify in workflow object')
        self.my_output.debug(json.dumps(workflow_object, indent=4))

        return None

    def get_workflow_info(self, workflow_id):
        """Return dictionary of server, workflow info and workflow tasks info

        Args:
            workflow_id (string): workflow id to be found

        Workflow ID must exist
        May be associated with server object type
        Should have tasks
        If checks fail, None value is returned

        Returns:
            dictionary or None
        """
        server_workflow_info = {}
        workflow_object = self.workflow_handler.get(workflow_id)
        server_workflow_info['workflow'] = self.workflow_handler.get_info(
            workflow_object
        )
        if server_workflow_info['workflow'] is None:
            return None

        server_workflow_info['tasks'] = self.workflow_task_info_handler.get_workflow_tasks_info(workflow_id)
        if server_workflow_info['tasks'] is None:
            return None

        server_workflow_info['server'] = None
        server_id = self.get_workflow_server_id(workflow_object)
        if server_id is not None:
            server_workflow_info['server'] = self.compute_handler.get(
                server_id
            )

        return server_workflow_info

    def print_workflow_info(self, server_workflow_info, stream='default'):
        if server_workflow_info['server'] is not None:
            self.my_output.dictionary(
                server_workflow_info['server'],
                keys=[
                    'Name',
                    'Model',
                    'Serial',
                    'ManagementIp'
                ],
                title_keys=[
                    'Name',
                    'Model',
                    'Serial',
                    'IP'
                ],
                title="Server",
                prefix="- ",
                underline=False,
                stream=stream
            )

        if server_workflow_info['workflow']['Status'] == 'RUNNING':
            self.my_output.dictionary(
                server_workflow_info['workflow'],
                keys=[
                    'Moid',
                    'Name',
                    'Status',
                    'CreateTime',
                    'StartTime',
                    'Progress',
                    'Duration'
                ],
                title_keys=[
                    'Workflow ID',
                    'Name',
                    'Status',
                    'Create Time',
                    'Start Time',
                    'Progress',
                    'Duration'
                ],
                title="Workflow",
                prefix="- ",
                underline=False,
                stream=stream
            )
        else:
            self.my_output.dictionary(
                server_workflow_info['workflow'],
                keys=[
                    'Moid',
                    'Name',
                    'Status',
                    'CreateTime',
                    'StartTime',
                    'EndTime',
                    'Duration'
                ],
                title_keys=[
                    'Workflow ID',
                    'Name',
                    'Status',
                    'Create Time',
                    'Start Time',
                    'End Time',
                    'Duration'
                ],
                title="Workflow",
                prefix="- ",
                underline=False,
                stream=stream
            )

        if len(server_workflow_info['tasks']) > 0:
            order = [
                'Moid',
                'Description',
                'CreateTime',
                'Status',
                'Duration',
                'FailureReason'
            ]

            headers = [
                'Task Moid',
                'Description',
                'Create Time',
                'Status',
                'Duration',
                'Details'
            ]

            self.my_output.my_table(
                server_workflow_info['tasks'],
                order=order,
                headers=headers,
                table=True,
                stream=stream
            )
