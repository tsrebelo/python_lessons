from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

if __name__ == "__main__":
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Servidor ativo em http://localhost:{PORT}")
    print("Pressiona Ctrl+C para parar.")
    httpd.serve_forever()


# "https://www.traceandmoment.com" - Trace & Moment
# "https://www.inkandlens.com" - Ink & Lens Studio

# Trace & Moment Studio | Ink & Lens Studio — Início