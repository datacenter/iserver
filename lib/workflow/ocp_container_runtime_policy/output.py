import json


def print_ocp_container_policy_config(info, my_output):
    my_output.default(
        'Container Policy Configuration',
        underline=True,
        before_newline=True
    )

    if len(info) == 0:
        my_output.default('None')
        return

    equal = True
    if len(info) > 1:
        reference = '\n'.join(info[0]['config'])
        for item in info:
            if '\n'.join(item['config']) != reference:
                equal = False

    if equal:
        my_output.default('Configuration the same on all nodes', before_newline=True, after_newline=True)
        my_output.default(
            json.dumps(
                info[0]['config'],
                indent=4
            )
        )

    if not equal:
        for item in info:
            my_output.default('Node %s [%s]' % (item['name'], item['ip']), after_newline=True)

            my_output.default(
                json.dumps(
                    item['config'],
                    indent=4
                ),
                wrap='~~~'
            )

def print_ocp_container_policy_mc(info, my_output):
    my_output.default(
        'Container Policy Machine Configuration',
        underline=True,
        before_newline=True
    )

    if len(info) == 0:
        my_output.default('None')
        return

    for item in info:
        my_output.default('Machine config: %s' % (item['name']), before_newline=True)
        my_output.default('Node: %s' % (', '.join(item['node'])))
        for file_info in item['file']:
            my_output.default('Path: %s' % (file_info['path']))
            my_output.default(file_info['content'], wrap='~~~')

def print_ocp_container_policy_info(info, my_output):
    if 'mc' in info:
        print_ocp_container_policy_mc(info['mc'], my_output)
        
    if 'config' in info:
        print_ocp_container_policy_config(info['config'], my_output)
