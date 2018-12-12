"""One shared terminal per URL endpoint

Plus a /new URL which will create a new terminal and redirect to it.
"""
from __future__ import print_function, absolute_import
import logging
import os.path
import sys
import tornado.web
import tornado.ioloop
import tornado_xstatic
from terminado import TermSocket, NamedTermManager
import os.path
import tornado.ioloop
import terminado

STATIC_DIR = os.path.join(os.path.dirname(terminado.__file__), "_static")
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")


AUTH_TYPES = ("none", "login")

class TerminalPageHandler(tornado.web.RequestHandler):
    """Render the /ttyX pages"""
    def get(self, term_name):
        return self.render("termpage.html", static=self.static_url,
                           xstatic=self.application.settings['xstatic_url'],
                           ws_url_path="/_websocket/"+term_name)

class NewTerminalHandler(tornado.web.RequestHandler):
    """Redirect to an unused terminal name"""
    def get(self):
        name, terminal = self.application.settings['term_manager'].new_named_terminal()
        self.redirect("/" + name, permanent=False)

def main():
    print("Starting")
    term_manager = NamedTermManager(shell_command=['zsh'],
                                     max_terminals=100)

    handlers = [
                (r"/_websocket/(\w+)", TermSocket,
                     {'term_manager': term_manager}),
                (r"/new/?", NewTerminalHandler),
                (r"/(\w+)/?", TerminalPageHandler),
                (r"/xstatic/(.*)", tornado_xstatic.XStaticFileHandler)
               ]
    application = tornado.web.Application(handlers, static_path=STATIC_DIR,
                              template_path=TEMPLATE_DIR,
                              xstatic_url=tornado_xstatic.url_maker('/xstatic/'),
                              term_manager=term_manager)

    application.listen(5001, '0.0.0.0')
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
