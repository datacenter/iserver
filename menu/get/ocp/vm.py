import sys
import json
import traceback
import threading
import click

from lib.ocp import output as ocp_output

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("vm")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Filter by cluster node name")
@click.option("--namespace", "vm_namespace", default='', callback=validations.empty_string_to_none, help="Filter by virtual machine namespace")
@click.option("--name", "vm_name", default='', callback=validations.validate_ocp_namespace_name, help="Filter by virtual machine name")
@click.option("--mac", "mac_address_filter", default='', callback=validations.empty_string_to_none, help="MAC filter")
@click.option("--sriov", type=click.Choice(['any', 'enabled', 'disabled'], case_sensitive=False), default='any', show_default=True, help="Filter by sriov capabilities")
@click.option("--fabric", "fabric_hint", callback=validations.validate_fabric, multiple=True, help="Fabric hint")
@click.option("--view", "-v", type=click.Choice(['default', 'intf', 'sriov', 'fabric', 'bgp', 'net', 'disk', 'csi', 'service', 'all'], case_sensitive=False), multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_ocp_vm_command(
        ctx,
        cluster_name,
        node_name,
        vm_namespace,
        vm_name,
        mac_address_filter,
        sriov,
        fabric_hint,
        view,
        output,
        devel
        ):
    """Get ocp vm"""

    # iserver get ocp vm

    ctx.developer = devel
    ctx.output = output
    if len(view) == 0:
        view = ['default']

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        ocp_output_handler = ocp_output.OcpOutput(log_id=ctx.run_id)
        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name
        )
        if ocp_handler is None:
            raise ErrorExit

        # ctx.busy = False
        # response = ocp_handler.k8s_handler.get_virtual_machine_instances()
        # print(response)

        vm_filter = []
        namespace_filtered = False

        if vm_name is not None:
            vm_filter.append(
                'name:%s' % (vm_name['name'])
            )

            if vm_name['namespace'] is not None:
                namespace_filtered = True
                vm_filter.append(
                    'namespace:%s' % (vm_name['namespace'])
                )

        if vm_namespace is not None:
            if namespace_filtered:
                ctx.my_output.error(
                    'Define namespace filter in one place'
                )
                raise ErrorExit

            vm_filter.append(
                'namespace:%s' % (vm_namespace)
            )

        if node_name is not None:
            vm_filter.append(
                'node:%s' % (node_name)
            )

        if sriov != 'any':
            vm_filter.append(
                'sriov:%s' % (sriov)
            )

        if mac_address_filter is not None:
            vm_filter.append(
                'mac:%s' % (mac_address_filter)
            )

        csi_info = False
        if 'csi' in view or 'all' in view:
            csi_info = True

        sriov_info = False
        if 'sriov' in view or 'net' in view or 'all' in view:
            sriov_info = True

        fabric_info = False
        if 'fabric' in view or 'net' in view or 'all' in view:
            if fabric_hint is None:
                if 'all' not in view:
                    ctx.my_output.error('Provide --fabric hint')
                    raise ErrorExit
                if output != 'json':
                    ctx.my_output.default('[INFO] Provide --fabric hint for fabric and bgp information')
            else:
                fabric_info = True

        bgp_info = False
        if 'bgp' in view or 'net' in view or 'all' in view:
            if fabric_hint is None:
                if 'all' not in view:
                    ctx.my_output.error('Provide --fabric hint')
                    raise ErrorExit
            else:
                bgp_info = True

        vms = ocp_handler.get_ocp_vms(
            vm_filter=vm_filter,
            csi_info=csi_info,
            sriov_info=sriov_info,
            fabric_info=fabric_info,
            bgp_info=bgp_info,
            fabric_hint=fabric_hint
        )

        ctx.busy = False

        if vms is None:
            raise ErrorExit

        if output == 'json':
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    vms,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(vms)

        if 'all' in view or 'default' in view:
            ocp_output_handler.print_ocp_vms(vms, title=True)

        if 'all' in view or 'disk' in view:
            ocp_output_handler.print_ocp_vms_disk(vms, title=True)

        if 'all' in view or 'csi' in view:
            ocp_output_handler.print_ocp_vms_csi(vms, title=True)

        if 'all' in view or 'service' in view:
            ocp_output_handler.print_ocp_vms_service(vms, title=True)

        if 'all' in view or 'intf' in view or 'net' in view:
            ocp_output_handler.print_ocp_vms_intf(vms, title=True)

        if 'all' in view or 'sriov' in view or 'net' in view:
            ocp_output_handler.print_ocp_vms_sriov(vms, title=True)

        if fabric_info:
            if 'all' in view or 'fabric' in view or 'net' in view:
                ocp_output_handler.print_ocp_vms_fabric(vms, title=True)

        if bgp_info:
            if 'all' in view or 'bgp' in view or 'net' in view:
                ocp_output_handler.print_ocp_vms_bgp(vms, title=True)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
