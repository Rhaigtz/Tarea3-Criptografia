# write-html-2-windows.py

import webbrowser
from rijndael.cipher.crypt import new
from rijndael.cipher.blockcipher import MODE_CBC



rjn = new('thisisatestkeywhichis32byteslong', MODE_CBC, 'thisisatestkeywhichis32byteslong', 32)
encd = rjn.encrypt('A padded string to BLOCKSIZE length.')

f = open('helloworld.html','wb')




message = """<html>
<head></head>
<body><p>Este sitio contiene un mensaje secreto</p>
<div classname={} id={}>
</body>
</html>""".format('rijndael', encd)




f.write(message.encode())
f.close()

webbrowser.open_new_tab('helloworld.html')