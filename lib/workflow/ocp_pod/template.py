import importlib
from lib.workflow.ocp_pod import common as local_common
from lib.workflow.ocp_pod import pnet


def get_variables_from_params(params):
  variables = {}
  variables['NAMESPACE'] = params['namespace']
  variables['NAME'] = params['name']

  vmap = dict(
  )
  for key in vmap:
    if key in params:
      variables[vmap[key]] = params[key]
  
  return variables


def add_networking(params, my_output, content):
  if 'network' not in params:
    return content
  
  index = 0
  for network in params['network']:
    if network.split(',')[0] == 'pnet':
      content = pnet.add(params, my_output, content, index, network)
      if content is None:
        return content

    index += 1

  return content


def get(params, my_output):
  params['variables'] = get_variables_from_params(params)
  
  cmodule = importlib.import_module('lib.workflow.ocp_pod.%s' % (params['template']))
  content = getattr(cmodule, 'get')(
    params,
    my_output
  )

  content = add_networking(params, my_output, content)
  content = local_common.add_params(params, content)
  return content