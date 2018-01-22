'''
Created on Jan 16, 2017

@author: Asgard Team
'''
import sys
import utils

from daemon import Daemon
from flask import Flask
from epepin_api.v1.routes import apiv1


app = Flask(__name__)
app.register_blueprint(apiv1, url_prefix='/v1')


class EpepinDaemon(Daemon):
    def run(self):
        app.run(epepin_endpoint, epepin_port)


def main():
    cfg = utils.get_config()
    global epepin_endpoint
    epepin_endpoint = cfg.epepin_api_endpoint
    global epepin_port
    epepin_port = cfg.epepin_api_port
    daemon = EpepinDaemon('/tmp/daemon-eppin.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()

        elif 'status' == sys.argv[1]:
            pid = daemon.status()
            if not pid:
                print("EPEPIN API Server Daemon isn't running ;)")
            else:
                print("EPEPIN API Server Daemon is running [PID=%d]" % pid)
        else:

            sys.exit(2)
        sys.exit(0)
    else:
        print "Usage of EPEPIN API Server: %s start|stop|restart|status" % sys.argv[0]
        sys.exit(2)


if __name__ == "__main__":
 sys.exit(main())
