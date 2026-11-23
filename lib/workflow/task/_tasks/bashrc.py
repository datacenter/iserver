import json
from lib import file_helper


def run(task, user_settings, my_output, ssh_handler, log_id):
    if not task['enabled']:
        return True

    my_output.default('Task cli bashrc', before_newline=True, underline=True)
    my_output.default(json.dumps(task, indent=4))

    if task['http_proxy'] is None or len(task['http_proxy']) == 0:
        my_output.default('No changes needed')
        return True

    my_output.default('Download /var/home/core/.bashrc')
    filename = file_helper.get_tmp_filename()
    success = ssh_handler.scp_file(
        '/var/home/core/.bashrc',
        filename,
        put=False
    )
    if not success:
        my_output.error('Download failed')
        return False

    content = file_helper.get_file_text(filename)
    if content is None:
        my_output.error('Failed to read downloaded file: %s' % (filename))
        return False

    if 'http_proxy' in content.lower():
        my_output.default('http proxy already defined in .bashrc')
        return True

    content = '%s\n' % (content)
    content = '%sexport HTTP_PROXY=%s\n' % (content, task['http_proxy'])
    content = '%sexport HTTPS_PROXY=%s\n' % (content, task['https_proxy'])
    content = '%sexport NO_PROXY=%s\n' % (content, task['no_proxy'])
    my_output.default(content, before_newline=True, after_newline=True)

    success = file_helper.set_file(filename, content)
    if not success:
        my_output.error('Failed to set local file: %s' % (filename))
        return False

    my_output.default('Upload /var/home/core/.bashrc')
    success = ssh_handler.scp_file(
        filename,
        '/var/home/core/.bashrc'
    )
    if not success:
        my_output.error('Upload failed')
        return False

    my_output.default('.bashrc uploaded with proxy settings')
    return True
