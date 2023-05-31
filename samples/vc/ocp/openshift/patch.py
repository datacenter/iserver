import os
import sys
import traceback


def get_file(filename):
    if os.path.isfile(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file_handler:
                return file_handler.read()
        except BaseException:
            print(traceback.format_exc())

    return None


def set_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as file_handler:
            file_handler.write(content)
    except BaseException:
        print(traceback.format_exc())
        return False

    return True


config_content = get_file('/root/config.yaml')
if config_content is None:
    print('Failed to read config file')
    sys.exit(1)
config_content = config_content.rstrip('\n')

secret_content = get_file('/root/pull-secret.txt')
if secret_content is None:
    print('Failed to read secret file')
    sys.exit(1)
secret_content = secret_content.rstrip('\n')

ssh_key_filename = get_file('/root/.ssh/id_ed25519.pub')
if ssh_key_filename is None:
    print('Failed to read ssh key file')
    sys.exit(1)
ssh_key_filename = ssh_key_filename.rstrip('\n')

config_content = config_content.replace('PULL_SECRET_FILE', secret_content)
config_content = config_content.replace('SSH_PUBLIC_KEY', ssh_key_filename)
if not set_file('/root/config.yaml', config_content):
    sys.exit(1)

print('Config variables replaced with files content')

sys.exit(0)
