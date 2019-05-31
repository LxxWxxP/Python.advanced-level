try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    import json
except ImportError:
    import simplejson

print (json.dumps({'python':2.7}))
