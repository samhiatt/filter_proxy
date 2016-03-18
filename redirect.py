def start(context, argv):
    if len(argv) != 5:
        raise ValueError('Usage: -s "redirect.py api.example.com /apiPrefix localhost 3000"')
    context.domainName = argv[1]
    context.pathStartsWith = argv[2]
    context.hostToRedirectTo = argv[3]
    context.portToRedirectTo = int(argv[4])

def request(context, flow):
    if flow.request.pretty_host == context.domainName and flow.request.path.startswith(context.pathStartsWith):
        print "REQUEST: %s://%s:%s%s REDIRECTED TO %s://%s:%s%s"%(
                flow.request.scheme, flow.request.pretty_host, flow.request.port, flow.request.path, "http", 
                context.hostToRedirectTo, context.portToRedirectTo, flow.request.path
        )
        print "SNI: "+flow.client_conn.connection.get_servername()
        flow.request.headers['ProxyHost'] = flow.client_conn.connection.get_servername()
        flow.request.scheme = "http"
        flow.request.host = context.hostToRedirectTo
        flow.request.port = context.portToRedirectTo

