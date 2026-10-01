import yaml
from lib import filter_helper


def base():
    return """
apiVersion: v1
kind: Pod
metadata:
  name: ${NAME}
  namespace: ${NAMESPACE}
spec:
  containers:
  - image: nginx
    name: nginx
    """

def get(params, my_output):
    content = filter_helper.replace_attributes(base(), params['variables'])
    leftover = filter_helper.get_content_attributes(content)
    if len(leftover) > 0:
       my_output.error('Not all variables replaced: %s' % (', '.join(leftover)))
       return None, None
    
    try:
        content = yaml.safe_load(content)
    except BaseException:
        my_output.error('Template load failed')
        return None, None
    
    return content