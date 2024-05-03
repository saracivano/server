from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response = json.dumps({
            "message": "Success!"
        })

        self.wfile.write(bytes(response, "utf-8"))

if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Server)
    print(f"Server started @ http://{HOST}:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\nServer stopped.")