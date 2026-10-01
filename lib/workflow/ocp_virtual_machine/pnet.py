import json
from lib import ip_helper
from lib import filter_helper


def validate(params, my_output, network):
  items = network.split(',')
  if len(items) not in [3,4]:
    my_output.error('Network format pnet,name,ip or pnet,name,ip,ip')
    return None

  metadata = {}
  metadata['network'] = items[1]
  metadata['subnet'] = None
  metadata['ipv4'] = None
  metadata['ipv6'] = None

  info = params['k8s_handler'].get_clusterwide_private_network(metadata['network'])
  if info is None:
    my_output.default('Private network %s %s' % (metadata['network'], my_output.add_color('not found', 'Red')))
    return None
  
  if not ip_helper.is_valid_ip_address(items[2]):
    my_output.error('Invalid IP address: %s' % (items[2]))
    return None
  
  if ip_helper.is_valid_ipv4_address(items[2]):
    metadata['ipv4'] = items[2]
  else:
    metadata['ipv6'] = items[2]

  if len(items) == 4:
    if not ip_helper.is_valid_ip_address(items[3]):
      my_output.error('Invalid IP address: %s' % (items[3]))
      return None

    if ip_helper.is_valid_ipv4_address(items[3]):
      metadata['ipv4'] = items[3]
    else:
      metadata['ipv6'] = items[3]

  matching_subnet_v4 = None
  if metadata['ipv4'] is not None:
    for subnet in info['subnet']:
      cidrv4 = filter_helper.get(subnet, 'cidrv4')
      if cidrv4 is not None:
        if ip_helper.is_ipv4_in_cidr(metadata['ipv4'], cidrv4):
          matching_subnet_v4 = subnet
          metadata['subnet'] = subnet['name']

    if matching_subnet_v4 is None:
      my_output.error(
        'IP address %s not matching any subnet of private network %s' % (
          metadata['ipv4'],
          metadata['network']
        )
      )
      return None
    
  matching_subnet_v6 = None
  if metadata['ipv6'] is not None:
    for subnet in info['subnet']:
      cidrv6 = filter_helper.get(subnet, 'cidrv6')
      if cidrv6 is not None:
        if ip_helper.is_ipv6_in_cidr(metadata['ipv6'], cidrv6):
          matching_subnet_v6 = subnet
          metadata['subnet'] = subnet['name']

    if matching_subnet_v6 is None:
      my_output.error(
        'IP address %s not matching any subnet of private network %s' % (
          metadata['ipv6'],
          metadata['network']
        )
      )
      return None
  
  if matching_subnet_v4 is not None and matching_subnet_v6 is not None:
    if matching_subnet_v4 != matching_subnet_v6:
      my_output.error(
        'IPv4 address %s and IPv6 address %s must belong to the single subnet of private network %s' % (
          metadata['ipv4'],
          metadata['ipv6'],
          metadata['network']
        )
      )
      return None
  
  if metadata['ipv4'] is None:
    del metadata['ipv4']

  if metadata['ipv6'] is None:
    del metadata['ipv6']

  return metadata


def add(params, my_output, content, index, network):
  pnet_metadata = validate(params, my_output, network)
  if pnet_metadata is None:
    return None

  subnet_name = pnet_metadata['subnet']
  del pnet_metadata['subnet']

  if index == 0:
    if filter_helper.get(content, 'spec:template:metadata:annotations') is None:
      content['spec']['template']['metadata']['annotations'] = {}

    if filter_helper.get(content, 'spec:template:metadata:annotations:privnet.isovalent.com/network-attachment') is not None:
      my_output.default(json.dumps(content['spec']['template']['metadata'], indent=4), wrap='~~~')
      my_output.error('Unexpected template metadata')
      return None
    
    content['spec']['template']['metadata']['annotations']['privnet.isovalent.com/network-attachment'] = json.dumps(pnet_metadata)
    
    # Change interface to bridge mode

    interfaces = filter_helper.get(content, 'spec:template:spec:domain:devices:interfaces')
    if interfaces is None or len(interfaces) == 0:
      my_output.default(json.dumps(content['spec']['template']['spec'], indent=4), wrap='~~~')
      my_output.error('Unexpected template spec')
      return None

    if 'masquerade' not in interfaces[0]:
      my_output.default(json.dumps(content['spec']['template']['spec'], indent=4), wrap='~~~')
      my_output.error('Unexpected template spec')
      return None

    del content['spec']['template']['spec']['domain']['devices']['interfaces'][0]['masquerade']
    content['spec']['template']['spec']['domain']['devices']['interfaces'][0]['bridge'] = {}

  if index == 1:
    if filter_helper.get(content, 'spec:template:metadata:annotations') is None:
      content['spec']['template']['metadata']['annotations'] = {}


    content['spec']['template']['metadata']['annotations']['privnet.isovalent.com/secondary-network-attachments'] = json.dumps(
      [pnet_metadata]
    )

  if index > 1:
    if filter_helper.get(content, 'spec:template:metadata:annotations') is None:
      my_output.default(json.dumps(content['spec']['template']['metadata'], indent=4), wrap='~~~')
      my_output.error('Unexpected template spec metadata')
      return None

    pnets = filter_helper.get(content, 'spec:template:metadata:annotations:privnet.isovalent.com/secondary-network-attachments')
    if pnets is None:
      my_output.default(json.dumps(content['spec']['template']['metadata'], indent=4), wrap='~~~')
      my_output.error('Unexpected template spec metadata')
      return None
    
    try:
      jpnets = json.loads(pnets)
      jpnets.append(pnet_metadata)
      content['spec']['template']['metadata']['annotations']['privnet.isovalent.com/secondary-network-attachments'] = json.dumps(
        jpnets
      )
    except BaseException:
      my_output.default(json.dumps(content['spec']['template']['metadata'], indent=4), wrap='~~~')
      my_output.error('template spec metadata manipulation failed')
      return None

  if index >= 1:
    network_mo = {}
    network_mo['name'] = 'eth%s' % (index)
    network_mo['multus'] = {}
    network_mo['multus']['networkName'] = '%s/%s-%s' % (
      params['namespace'],
      pnet_metadata['network'],
      subnet_name
    )
    content['spec']['template']['spec']['networks'].append(
      network_mo
    )

    interface_mo = {}
    interface_mo['name'] = 'eth%s' % (index)
    interface_mo['bridge'] = {}
    content['spec']['template']['spec']['domain']['devices']['interfaces'].append(
      interface_mo
    )

  return content