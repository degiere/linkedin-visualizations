from ConfigParser import SafeConfigParser
import os

def config_parser():
    parser = SafeConfigParser()
    parser.read('default.cfg')
    # copy the above here and set app credentials
    parser.read(os.path.expanduser('~/.linkedin.cfg'))
    return parser
