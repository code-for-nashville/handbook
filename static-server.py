#!/usr/bin/env python3
from http.server import SimpleHTTPRequestHandler
import http.server

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    http.server.test(CORSRequestHandler, http.server.HTTPServer)