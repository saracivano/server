from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import cgi

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
    
    def do_POST(self):
        if self.path == "/python3":
            content_length = int(self.headers['Content-Length'])
            post_data_bytes = self.rfile.read(content_length)

            post_data_str = post_data_bytes.decode("utf-8")
            list_of_post_data = post_data_str.split('&')
            print(post_data_str)

            self.send_response(204)


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Server)
    print(f"Server started @ http://{HOST}:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\nServer stopped.")