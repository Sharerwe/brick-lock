
import json

def run(**args):
    print('[$] Enter stage 1')
    basic_config =json.dumps([{"module" : "shell_module"}])
    return basic_config
                        
