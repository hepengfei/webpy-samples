import web
import os

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')

render_env = {
    # 'function name used in templates' : function,
}
render = web.template.render(templates_root, base='base', globals=render_env)
render_plain = web.template.render(templates_root)


def notfound():
    return web.notfound(render_plain.notfound())

def internalerror():
    return web.internalerror(render_plain.internalerror())


class index:
    def GET(self):
        return render.index()

class hello:
    def GET(self, name):
        if not name:
            name = "World"
        return render.hello(name)

