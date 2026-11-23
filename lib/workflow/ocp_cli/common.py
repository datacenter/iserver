import json
import copy
from lib import file_helper
from lib import ip_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow - CLI'
    return params