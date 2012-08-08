#!/bin/env python

import web
import views

urls = (
    '/', 'views.index',
    '/hello/(.*)', 'views.hello',
)

app = web.application(urls, globals(), autoreload=True)

# customize error pages
app.notfound = views.notfound
app.internalerror = views.internalerror

if __name__ == "__main__":      # for test
    app.run()
else:                           # for mod_wsgi(recommend you to use nginx+uwsgi)
    application = app.wsgifunc()
