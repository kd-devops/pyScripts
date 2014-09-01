import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options
from mem_info_api import PyAgent

define("port", default=9000, help="run on port", type=int)
define("debug", default=True, help="enable debugging features", type=bool)

VFENSE_TEMPLATE_PATH = "/home/devops/python"
#class IndexHandler(tornado.web.RequestHandler):
#    def get(self):
#        return self.render_string(
#            os.path.join(VFENSE_TEMPLATE_PATH, "header.html")
#        )

class HeaderModule(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            os.path.join(VFENSE_TEMPLATE_PATH, "header.html")
        )

class Application(tornado.web.Application):
   def __init__(self, debug):
	handlers = [
	    (r"/api/py_agent?", PyAgent),
	]

	tornado.web.Application.__init__(self, handlers,
                                         template_path=VFENSE_TEMPLATE_PATH,
                                         debug=debug,)
if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(
        Application(options.debug),
    )
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

