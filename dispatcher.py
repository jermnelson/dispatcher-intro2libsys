"""
 Name:        dispatcher


 Purpose:     This class dispaches web request to various applications running
              on the intro2libys.info domain

 Author:      Jeremy Nelson

 Created:     2014-01-21
 Copyright:   (c) Jeremy Nelson 2014, 2015
 Licence:     GPL v.2
"""
import importlib
import os
import sys
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware


DISPATCH_ROOT = os.path.abspath(os.path.dirname(__file__))
from intro2libsys.server import app as publisher_app

sys.path.append(DISPATCH_ROOT)
coasl_server2014 = importlib.import_module("coasl-rda-linked-data.server", None)
code4lib_talk2015 = importlib.import_module("code4lib-2015-talk.talk", None)
dlf_forum_poster2014 = importlib.import_module("dlf-forum-2014-poster", None)
lita_server2014 = importlib.import_module("lita-library-linked-data.server", None)
nextlibsys_server2014 = importlib.import_module("next-library-systems", None)
niso_webinar2015 = importlib.import_module("niso-2015-webinar", None)
pycon_poster2014 = importlib.import_module('pycon-2014-poster', None)
##islandora_camp2014 = importlib.import_module('islandora-camp-2014', None)
intro_redis = importlib.import_module('introduction-to-redis', None)


application = DispatcherMiddleware(
    publisher_app,
    {'/coasl-webinar-2014': coasl_server2014.app,
     '/code4lib-2015': code4lib_talk2015.app,
     '/dlf-forum-2014-poster': dlf_forum_poster2014.poster,
     '/lita-webinar-2014': lita_server2014.app,
     '/introduction-to-redis': intro_redis.app,
  ##   '/islandora-camp-2014': islandora_camp2014.presentation,
     '/next-library-systems-2014': nextlibsys_server2014.app,
     '/niso-2015-webinar': niso_webinar2015.app,
     '/pycon-2014-poster': pycon_poster2014.poster})

def main():
    run_simple('0.0.0.0', 8081, application, use_reloader=True)


if __name__ == '__main__':
    main()
