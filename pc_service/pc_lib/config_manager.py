import configparser

#Instantiating new configparser
_config = configparser.ConfigParser()
_config.read('pc_lib/config.ini')

def base_url():
    print(list(_config['DEFAULT']))
    return _config['DEFAULT']['base_url']

