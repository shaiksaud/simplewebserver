from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
       <head> 
        <title>Device Configuration</title>
    <body> 
        <h1 align = "center">Shaik saud.s - 26013211</h1>
        <h2 align = "center">My laptop configuration</h2>
        <table border="2" cellspacing="10" cellpadding="10"> 
            <tr>
            <th align = "center">S.NO</th>
            <th align = "center">DEVICE TYPE</th>
            <th align = "center">DEVICE INFO</th>
            </tr>
            <tr>
            <td align = "center">1</td>
            <td align = "center">Device Name</td>
            <td align = "center">TL15-53M-G2</td>
            </tr>
            <tr>
            <td align = "center">2</td>
            <td align = "center">Processor</td>
            <td align = "center">Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
            </tr>
            <tr>
            <td align = "center">3</td>
            <td align = "center">Installed RAM</td>
            <td align = "center">16.0 GB (15.7 GB usable)</td>
            </tr>
            <tr>
            <td align = "center">4</td>
            <td align = "center">Graphics Card</td>
            <td align = "center">Intel(R) Graphics (128 MB)</td>
            </tr>
            <tr>
            <td align = "center">5</td>
            <td align = "center">Storage</td>
            <td align = "center">477 GB total (115 GB used)</td>
            </tr>
            <tr>
            <td align = "center">6</td>
            <td align = "center">Device ID</td>
            <td align = "center">0C8C0591-AFF1-4FD1-81FE-2063F09AF79C</td>
            </tr>
            <tr>
            <td align = "center">7</td>
            <td align = "center">Product ID</td>
            <td align = "center">00342-42954-11520-AAOEM</td>
            </tr>
            <tr>
            <td align = "center">8</td>
            <td align = "center">System Type</td>
            <td align = "center">64-bit operating system, x64-based processor</td>
            </tr>
            <tr>
            <td align = "center">9</td>
            <td align = "center">Pen and Touch Support</td>
            <td align = "center">No pen or touch input is available for this display</td>
            </tr>
        </table>
    </body>
    </head> 
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()