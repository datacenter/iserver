import sys
import click

from lib import self_doc


@click.command("doc")
@click.pass_obj
@click.option("--results", "directory", is_flag=False, show_default=False, default='results', help="Results directory")
@click.option("--template", "template_names", multiple=True, help="Select template")
@click.option("--generate", is_flag=True, show_default=True, default=False, help="Generate template from template")
@click.option("--replace", multiple=True, help="Replace pattern:value")
@click.option("--allow-failed", "allow_failed", is_flag=True, show_default=True, default=False, help="Allow failed tests")
@click.option("--anonymize", is_flag=True, show_default=True, default=False, help="Anonymize docs")
def utils_doc_command(ctx, directory, template_names, generate, replace, allow_failed, anonymize):
    """Generate documentation"""

    # iserver utils doc

    if anonymize:
        success = self_doc.anonymize_docs(
            verify=True
        )
        if not success:
            sys.exit(1)
        sys.exit(0)

    if '__ALL__' in template_names:
        template_names = self_doc.get_all_template_names()

    if generate:
        success = self_doc.generate_template_docs(
            template_names
        )

    replace_dir = {}
    for item in replace:
        replace_dir[item.split(':')[0]] = item.split(':')[1]

    success = self_doc.generate_docs(
        directory,
        template_names,
        replace=replace_dir,
        allow_failed=allow_failed
    )

    if not success:
        sys.exit(1)
