import os


def anonymize():
    try:
        value = os.getenv('iHide')        
    except BaseException:
        value = None

    if value is None:
        return False
    
    return True
