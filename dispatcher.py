#-------------------------------------------------------------------------------
# Name:        dispatcher
# Purpose:     This class dispaches web request to various applications running
#              on the intro2libys.info domain
#
# Author:      Jeremy Nelson
#
# Created:     2014-01-21
# Copyright:   (c) Jeremy Nelson 2014
# Licence:     GPL v.2
#-------------------------------------------------------------------------------
import importlib
import os
import sys
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


DISPATCH_ROOT = os.path.abspath(os.path.dirname(__file__))
from intro2libsys.server import app as publisher_app

sys.path.append(DISPATCH_ROOT)
coasl_server2014 = importlib.import_module("coasl-rda-linked-data.server", None)
# lita_server2014 = importlib.import_module("lita_library_linked_data.server", None)

from lita_library_linked_data.server import app as lita_app


application = DispatcherMiddleware(
    publisher_app,
    {'/coasl-webinar-2014': coasl_server2014.app,
     '/lita-webinar-2014': lita_app
     })

def main():
    run_simple('0.0.0.0', 8080, application, use_reloader=True)


if __name__ == '__main__':
    main()
