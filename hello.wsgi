def application(environ, start_response):
    import numpy
    a = numpy.fromstring('-2.3693744349064819e-197', dtype=numpy.float64, sep=' ')[0]
    print(a**2)

    # rest is same as http://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html
    status = '200 OK'
    output = b'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
