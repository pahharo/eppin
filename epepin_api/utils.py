'''
Created on Jan 18, 2017

@author: Asgard Team
'''
import os
from config import Config


def get_config():
    path = os.path.dirname(os.path.abspath(__file__))
    f = file('%s/config/epepin_server.cfg' % path)
    cfg = Config(f)
    return cfg