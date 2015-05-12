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
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
