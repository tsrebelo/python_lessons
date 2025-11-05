from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

if __name__ == "__main__":
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Servidor ativo em http://localhost:{PORT}")
    print("Pressiona Ctrl+C para parar.")
    httpd.serve_forever()
