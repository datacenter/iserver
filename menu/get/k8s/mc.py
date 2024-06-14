import sys
import json
import threading
import traceback
import click

from lib.k8s import output as k8s_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("mc")
@click.pass_obj
@click.option("--cluster", default='', help="Kubernetes cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by mc name")
@click.option("--path", "filepath", default='', callback=validations.empty_string_to_none, help="Filter by file path")
@click.option("--systemd", default='', callback=validations.empty_string_to_none, help="Filter by systemd name")
@click.option("--content", default='', callback=validations.empty_string_to_none, help="Filter by content")
@click.option("--view", "-v", default=['state'], help="[state|file|systemd|fcontent|scontent|user|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_k8s_mc_command(
        ctx,
        cluster,
        name,
        filepath,
        systemd,
        content,
        view,
        output,
        devel
        ):
    """Get k8s machine config (ocp)"""

    # iserver get k8s mc

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'state|file|systemd|fcontent|scontent|user|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        k8s_handlers = validations.validate_kubernetes_name(ctx, cluster, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        object_filter = []
        if name is not None:
            object_filter.append(
                'name:%s' % (name)
            )

        if filepath is not None:
            object_filter.append(
                'path:%s' % (filepath)
            )

        if systemd is not None:
            object_filter.append(
                'systemd:%s' % (systemd)
            )

        if content is not None:
            object_filter.append(
                'content:%s' % (content)
            )

        if output not in ['json', 'mo']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        if k8s_handlers.get_api() is None:
            ctx.busy = False
            ctx.my_output.error(
                'Connection to kubernetes cluster failed'
            )
            raise ErrorExit

        if output == 'mo':
            machine_configs = k8s_handlers.get_machine_configs(
                object_filter=object_filter,
                return_mo=True
            )
            ctx.my_output.default(
                json.dumps(
                    machine_configs,
                    indent=4
                )
            )
            return

        machine_configs = k8s_handlers.get_machine_configs(
            object_filter=object_filter
        )

        ctx.busy = False

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    machine_configs,
                    indent=4
                )
            )
            return

        if len(machine_configs) == 0:
            ctx.my_output.error(
                'No machine config found matching the search criteria'
            )
            raise ErrorExit

        if 'state' in view:
            k8s_output_handler.print_machine_configs(
                machine_configs,
                title=True
            )

        if 'file' in view:
            k8s_output_handler.print_machine_configs_file(
                machine_configs,
                title=True
            )

        if 'fcontent' in view:
            k8s_output_handler.print_machine_configs_content_file(
                machine_configs,
                title=True
            )

        if 'systemd' in view:
            k8s_output_handler.print_machine_configs_systemd(
                machine_configs,
                title=True
            )

        if 'scontent' in view:
            k8s_output_handler.print_machine_configs_content_systemd(
                machine_configs,
                title=True
            )

        if 'user' in view:
            k8s_output_handler.print_machine_configs_user(
                machine_configs,
                title=True
            )

        ctx.my_output.default('Filter: name, path, systemd, content', before_newline=True)
        ctx.my_output.default('View:   state (def), file, systemd, fcontent, scontent, user, all')

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
