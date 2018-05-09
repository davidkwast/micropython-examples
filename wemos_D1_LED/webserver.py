# http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#simple-http-server

import socket

from machine import Pin

led_pin = Pin(14, Pin.OUT, Pin.PULL_UP)

def led_toggle():
    if led_pin.value():
        led_pin.off()
    else:
        led_pin.on()

def led_status():
    if led_pin.value():
        return 'ON'
    else:
        return 'OFF'

def serve():
    
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            #print(line)
            
            if line == b'POST / HTTP/1.1\r\n':
                print('toggling LED')
                led_toggle()
            
            if not line or line == b'\r\n':
                break
        
        response = html.format(**{
            'led_status': led_status()
        })
        cl.send(response)
        cl.close()

# HTML
html = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        
        <title>ESP8266 Webserver blink</title>
        
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
        
    </head>
    <body>
        
        <div class="container">
            
            <h1>ESP8266 Webserver blink</h1>
            
            <hr>
            
            <div class="alert alert-info" role="alert">
                LED status: {led_status}
            </div>
            
            <hr>
            
            <form action="/" method="POST">
                <input class="btn btn-primary" type="submit" value="Toggle LED">
            </form>
            
            <hr>
            
        </div>
        
    </body>
</html>
"""

if __name__ == '__main__':
    serve()
