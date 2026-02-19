def run(linux_handler, my_output, server_name=None):
    if server_name is None:
        my_output.default('LVM Cleanup', before_newline=True, underline=True)
    else:
        my_output.default('LVM Cleanup [%s]' % (server_name), before_newline=True, underline=True)

    my_output.default('- gettings lvs...')
    lvs = linux_handler.get_lvs(cache_enabled=False)
    if lvs is None:
        my_output.error('Logical Volume collection failed')
        return False
    
    my_output.default('- gettings vgs...')
    vgs = linux_handler.get_vgs(cache_enabled=False)
    if vgs is None:
        my_output.error('Volume Group collection failed')
        return False

    my_output.default('- gettings pvs...')
    pvs = linux_handler.get_pvs(cache_enabled=False)
    if pvs is None:
        my_output.error('Physical Volume collection failed')
        return False

    success = True
    for item in lvs:
        if not item['is_pool']:
            my_output.default('- delete lvs: %s' % (item['lv_path']))
            lv_removed, cmd_output = linux_handler.delete_lv_cmd(item['lv_path'])
            my_output.default(cmd_output)
            if not lv_removed:
                my_output.error('Logical volume delete failed')
                success = False

    for item in lvs:
        if item['is_pool']:
            my_output.default('- delete lv pool: %s' % (item['lv_dm_path']))
            lv_removed, cmd_output = linux_handler.delete_lv_cmd(item['lv_dm_path'])
            my_output.default(cmd_output)
            if not lv_removed:
                my_output.error('Logical volume pool delete failed')
                success = False

    for item in vgs:
        my_output.default('- deactivate vg: %s' % (item['vg_name']))
        vg_deactivated, cmd_output = linux_handler.deactivate_vg_cmd(item['vg_name'])
        my_output.default(cmd_output)
        if not vg_deactivated:
            my_output.error('Volume group deactive failed')
            success = False
            continue

        my_output.default('- delete vg: %s' % (item['vg_name']))
        vg_deleted, cmd_output = linux_handler.delete_vg_cmd(item['vg_name'])
        my_output.default(cmd_output)
        if not vg_deleted:
            my_output.error('Volume group delete failed')
            success = False

    for item in pvs:
        my_output.default('- delete pv: %s' % (item['pv_name']))
        pv_deleted, cmd_output = linux_handler.delete_pv_cmd(item['pv_name'])
        my_output.default(cmd_output)
        if not pv_deleted:
            my_output.error('Physical volume delete failed')
            success = False

    return success
