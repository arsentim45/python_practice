from urllib.parse import unquote


def parse_data(data):
    data = str(data)
    begining = data.find('=')
    end = data.find(' ', begining)
    return unquote(data[begining+1:end])


custom_response = b"""HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 200
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"
Accept-Ranges: bytes
Connection: close

<html>
  <head>
    <title>An Example Page</title>
  </head>
  <body>
     <form>
        Your url:<br>
        <input type="text" name="url"><br>
        <input type="submit" value="Submit">
    </form> 
  </body>
</html>
"""