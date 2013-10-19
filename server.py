# -*- coding: UTF-8 -*
'''
Created on 2013-10-13

@author: RobinTang
'''

from wsgiref.simple_server import make_server
from wsgiref.util import setup_testing_defaults


def simple_app(environ, start_response):
	print 'start'
	setup_testing_defaults(environ)
	status = '200 OK'
	headers = [('Content-type', 'text/plain')]
	start_response(status, headers)
	print 'end'
	return ['empty']


if __name__ == '__main__':
	port = 8080
	httpd = make_server('0.0.0.0', port, simple_app)
	print "WebDAV serving on port %s..."%port
	httpd.serve_forever()



