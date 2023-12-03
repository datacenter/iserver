import sys
import traceback
import click
import yaml

from lib.k8s import output as k8s_output

from menu import validations
from menu import common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("srnnp")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', callback=validations.empty_string_to_none, help="Cluster name")
@click.option("--namespace", default='openshift-sriov-network-operator', callback=validations.empty_string_to_none, help="Policy namespace")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Policy name")
@click.option("--type", "device_type", type=click.Choice(['vfio', 'net'], case_sensitive=False), help="Device type")
@click.option("--resource", "resource_name", default='', callback=validations.empty_string_to_none, help="Resource name")
@click.option("--node", "node_name", default='', callback=validations.empty_string_to_none, help="Node name")
@click.option("--intf", "interface_name", default='', callback=validations.empty_string_to_none, help="Interface name")
@click.option("--vf", "vf_count", type=click.INT, help="VF count")
@click.option("--range", "vf_range", default='', callback=validations.empty_string_to_none, help="VF range")
@click.option("--no-create", "no_create", is_flag=True, show_default=True, default=False, help="No creation")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_k8s_srnnp_command(
        ctx,
        cluster_name,
        namespace,
        name,
        device_type,
        resource_name,
        node_name,
        interface_name,
        vf_count,
        vf_range,
        no_create,
        devel
        ):
    """Create k8s srnnp"""

    # iserver create k8s srnnp

    ctx.developer = devel
    ctx.output = 'default'

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        if namespace is None:
            ctx.my_output.error('Define policy namespace')
            raise ErrorExit

        if namespace not in ['openshift-sriov-network-operator']:
            ctx.my_output.error('Unsupported policy namespace')
            raise ErrorExit

        if name is None:
            ctx.my_output.error('Define policy name')
            raise ErrorExit

        if resource_name is None:
            ctx.my_output.error('Define resource name')
            raise ErrorExit

        if node_name is None:
            ctx.my_output.error('Define node name')
            raise ErrorExit

        if interface_name is None:
            ctx.my_output.error('Define interface name')
            raise ErrorExit

        if vf_count is None or vf_count <= 0:
            ctx.my_output.error('Define non-zero VF count')
            raise ErrorExit

        if vf_range is not None:
            if len(vf_range.split('-')) != 2:
                ctx.my_output.error('Define valid vf range')
                raise ErrorExit

        if k8s_handlers.is_sriov_network_node_policy(name):
            ctx.my_output.error('Policy already defined: %s' % (name))
            raise ErrorExit

        ctx.my_output.default(
            'SR-IOV Network Node Policy will be created: %s/%s' % (
                namespace,
                name
            )
        )

        srnnp_with_resource = k8s_handlers.get_sriov_network_node_policy_with_resource_name(resource_name)
        if srnnp_with_resource is not None:
            ctx.my_output.error('Resource name already used: %s' % (resource_name))
            raise ErrorExit

        ctx.my_output.default(
            'Resource name: %s' % (
                resource_name
            )
        )

        node_info = k8s_handlers.get_node(node_name)
        if node_info is None:
            ctx.my_output.error('Node not found: %s' % (node_name))
            raise ErrorExit

        ctx.my_output.default(
            'Node name: %s' % (
                node_name
            )
        )

        srnns_with_interface = k8s_handlers.get_sriov_network_node_state_with_node_interface(node_name, interface_name)
        if len(srnns_with_interface) == 0:
            ctx.my_output.error('Interface %s state on node %s not found' % (interface_name, node_name))
            raise ErrorExit

        if len(srnns_with_interface) > 1:
            ctx.my_output.error('Multiple interface %s state on node %s found' % (interface_name, node_name))
            raise ErrorExit

        k8s_output_handler.print_sriov_network_nodes_state(
            srnns_with_interface,
            title=True
        )

        body = 'apiVersion: sriovnetwork.openshift.io/v1'
        body = '%s\nkind: SriovNetworkNodePolicy' % (body)
        body = '%s\nmetadata:' % (body)
        body = '%s\n  namespace: %s' % (body, namespace)
        body = '%s\n  name: %s' % (body, name)
        body = '%s\nspec:' % (body)
        body = '%s\n  resourceName: %s' % (body, resource_name)
        body = '%s\n  nodeSelector:' % (body)
        body = '%s\n    topology.topolvm.io/node: "%s"' % (body, node_name)
        body = '%s\n  numVfs: %s' % (body, vf_count)
        body = '%s\n  nicSelector:' % (body)
        if vf_range is None:
            body = '%s\n    pfNames: [%s]' % (body, interface_name)
        else:
            body = '%s\n    pfNames: ["%s#%s"]' % (body, interface_name, vf_range)
        if device_type == 'vfio':
            body = '%s\n  deviceType: vfio-pci' % (body)
        if device_type == 'net':
            body = '%s\n  deviceType: netdevice' % (body)

        if no_create:
            return

        ctx.my_output.default('\n%s\n' % (body))
        if not common.get_confirmation():
            raise ErrorExit

        body_yaml = yaml.safe_load(body)
        if not k8s_handlers.create_sriov_network_node_policy(body_yaml):
            ctx.my_output.error(
                'SR-IOV network node policy create failed'
            )
            raise ErrorExit

        ctx.my_output.default(
            'SR-IOV network node policy created (note: node may be reloaded)'
        )

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
