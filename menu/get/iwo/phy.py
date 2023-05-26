import sys
import json
import threading
import traceback
import click

from lib.iwo import main as iwo

from menu import validations
from menu import defaults
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("phy")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--vm", "vm_name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by vm name")
@click.option("--vdc", "vdc_name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by vdc name")
@click.option("--storage", "storage_name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by storage name")
@click.option("--stale", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select stale")
@click.option("--inactive", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select inactive")
@click.option("--critical", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select critical")
@click.option("--major", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select major or critical")
@click.option("--minor", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select minor, major or critical")
@click.option("--show-dep", is_flag=True, show_default=True, default=False, help="Show dependencies")
@click.option("--show-vm", is_flag=True, show_default=True, default=False, help="Show virtual machines")
@click.option("--show-vdc", is_flag=True, show_default=True, default=False, help="Show virtual data center")
@click.option("--show-storage", is_flag=True, show_default=True, default=False, help="Show storage")
@click.option("--show-actions", is_flag=True, show_default=True, default=False, help="Show actions")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_iwo_phy_command(
        ctx,
        iaccount,
        name,
        vm_name,
        vdc_name,
        storage_name,
        stale,
        inactive,
        critical,
        major,
        minor,
        show_dep,
        show_vm,
        show_vdc,
        show_storage,
        show_actions,
        output,
        verbose,
        debug,
        devel
        ):
    """Get iwo physical machine"""

    # iserver get iwo phy

    ctx.developer = devel
    ctx.output = output

    try:
        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        iwo_handler = iwo.Iwo(
            iaccount,
            verbose=verbose,
            debug=debug,
            log_id=ctx.run_id
        )

        match_rules = []
        if name is not None:
            match_rules.append(
                'name:%s' % (name)
            )

        if vm_name is not None:
            show_vm = True
            show_dep = True
            match_rules.append(
                'vm:%s' % (vm_name)
            )

        if vdc_name is not None:
            show_vdc = True
            show_dep = True
            match_rules.append(
                'vdc:%s' % (vdc_name)
            )

        if storage_name is not None:
            show_storage = True
            show_dep = True
            match_rules.append(
                'storage:%s' % (storage_name)
            )

        if stale is not None:
            match_rules.append(
                'stale'
            )

        if inactive is not None:
            match_rules.append(
                'inactive'
            )

        if critical is not None:
            match_rules.append(
                'critical'
            )

        if major is not None:
            match_rules.append(
                'major'
            )

        if minor is not None:
            match_rules.append(
                'minor'
            )

        if show_vm or show_vdc or show_actions or show_storage:
            show_dep = True

        phys = iwo_handler.get_physical_machines(
            resolve_dependencies=show_dep,
            match_rules=match_rules
        )
        if phys is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get physical machines')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    phys,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(phys)

        iwo_handler.print_physical_machines(
            phys,
            show_dep=show_dep,
            show_vm=show_vm,
            show_vdc=show_vdc,
            show_storage=show_storage,
            show_actions=show_actions
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
