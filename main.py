#from gevent import monkey
#monkey.patch_all()

import tornado.ioloop
import tornado.web
from controller import *


from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['/docs'], module_directory='/tmp/mako_modules')

def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    print(mytemplate.render(**kwargs))

application = tornado.web.Application([
    (r"/question/add", AddQuestionHandler),
    (r"/question/(.*?)/", QuestionHandler),
    (r"/question/(.*?)/option/add", AddOptionHandler),
    (r"/review/add", AddReviewHandler),
    (r"/static", StaticHandler),
    (r"/", MainHandler),
])

if __name__ == "__main__":
    port = 8888
    try:
        from config import port as p
        port = p
    except:
        pass
        
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
