def print_ocp_chrony_config(info, my_output):
    my_output.default(
        'Chrony Configuration',
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
        my_output.default('~~~')
        for line in info[0]['config']:
            my_output.default(line)
        my_output.default('~~~')

    if not equal:
        for item in info:
            my_output.default('Node %s [%s]' % (item['name'], item['ip']), after_newline=True)
            my_output.default('~~~')
            for line in item['config']:
                my_output.default(line)
            my_output.default('~~~')


def print_ocp_chrony_state(info, my_output):
    order = [
        'name',
        'status',
        'reference',
        'stratum',
        'time',
        'root_delay'
    ]

    headers = [
        'Node',
        'Status',
        'Reference',
        'Stratum',
        'Time',
        'Delay'
    ]

    my_output.my_table(
        info,
        order=order,
        headers=headers,
        allow_order_subkeys=True,
        underline=True,
        row_separator=True,
        table=True
    )


def print_ocp_chrony_mc(info, my_output):
    my_output.default(
        'Chrony Machine Configuration',
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


def print_ocp_chrony_info(info, my_output):
    if 'mc' in info:
        print_ocp_chrony_mc(info['mc'], my_output)

    if 'config' in info:
        print_ocp_chrony_config(info['config'], my_output)

    if 'state' in info:
        print_ocp_chrony_state(info['state'], my_output)
