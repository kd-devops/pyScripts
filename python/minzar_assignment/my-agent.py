import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options
from mem_info import *
from check_apache_status import * 

define("port", default=9000, help="run on port", type=int)
define("debug", default=True, help="enable debugging features", type=bool)



class MemoryHandler(tornado.web.RequestHandler):
    def get(self):
	mem_stats = mem_status()
	self.write(mem_stats)

class ApacheStatusHandler(tornado.web.RequestHandler):
    def get(self):
	apache_status = check_apache_status()
	self.write(apache_status)

handlers = [
    	(r"/api/mem_status?", MemoryHandler),
	(r"/api/apache_status?",ApacheStatusHandler),
]
 
if __name__ == "__main__":
    parse_command_line()
    application = tornado.web.Application(handlers, debug=options.debug)
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
