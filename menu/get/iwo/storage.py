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


@click.command("storage")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--vm", "vm_name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by vm name")
@click.option("--phy", "phy_name", is_flag=False, show_default=True, default='', type=click.STRING, callback=validations.empty_string_to_none, help="Filter by phy name")
@click.option("--stale", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select stale")
@click.option("--inactive", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select inactive")
@click.option("--critical", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select critical")
@click.option("--major", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select major or critical")
@click.option("--minor", is_flag=True, show_default=True, default=False, type=click.STRING, help="Select minor, major or critical")
@click.option("--show-dep", is_flag=True, show_default=True, default=False, help="Show dependencies")
@click.option("--show-vm", is_flag=True, show_default=True, default=False, help="Show virtual machines")
@click.option("--show-phy", is_flag=True, show_default=True, default=False, help="Show physical machines")
@click.option("--show-actions", is_flag=True, show_default=True, default=False, help="Show actions")
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--verbose", is_flag=True, show_default=True, default=False, help="Verbose output")
@click.option("--debug", is_flag=True, show_default=True, default=False, help="Debug output")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_iwo_storage_command(
        ctx,
        iaccount,
        name,
        vm_name,
        phy_name,
        stale,
        inactive,
        critical,
        major,
        minor,
        show_dep,
        show_vm,
        show_phy,
        show_actions,
        output,
        verbose,
        debug,
        devel
        ):
    """Get iwo storage device"""

    # iserver get iwo storage

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

        if phy_name is not None:
            show_phy = True
            show_dep = True
            match_rules.append(
                'phy:%s' % (phy_name)
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

        if show_vm or show_phy or show_actions:
            show_dep = True

        storage = iwo_handler.get_storages(
            resolve_dependencies=show_dep,
            match_rules=match_rules
        )
        if storage is None:
            ctx.busy = False
            ctx.my_output.error('Failed to get storage devices')
            raise ErrorExit

        if output == 'json':
            ctx.busy = False
            ctx.log_prompt = False
            ctx.my_output.default(
                json.dumps(
                    storage,
                    indent=4
                )
            )
            return

        ctx.busy = False
        ctx.my_output.json_output(storage)

        iwo_handler.print_storages(
            storage,
            show_dep=show_dep,
            show_actions=show_actions,
            show_vm=show_vm,
            show_phy=show_phy
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
