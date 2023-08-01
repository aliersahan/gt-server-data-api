import requests
import random
from http.server import BaseHTTPRequestHandler, HTTPServer

def make_request():
    url = "https://212.252.126.123/growtopia/server_data.php"
    headers = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "www.growtopia1.com",
        "User-Agent": "UbiServices_SDK_2019.Release.27_PC64_unicode_static",
    }

    data = {
        "version": "4.22",
        "platform": "0",
        "protocol": "182",
    }

    proxies_list = [
        "socks5://USER_NAME:PASSWORD@IP:PORT",
    ]

    selected_proxy = random.choice(proxies_list)
    proxy = {
        "http": selected_proxy,
        "https": selected_proxy,
    }

    response = requests.post(url, headers=headers, data=data, proxies=proxy, verify=False)
    return response.text

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = make_request()
            self.wfile.write(message.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "404 Not Found"
            self.wfile.write(message.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=HelloHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving at port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
