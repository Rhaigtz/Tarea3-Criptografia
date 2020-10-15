import webbrowser
from oscrypto import symmetric
import codecs

encrypted = symmetric.rc4_encrypt(b'key123', b'text')


f = open('index.html', 'wb')

message = """<html>
<head></head>
<body>
<p>Esta pagina contiene un mensaje encriptado</p>

<div class={} id={}>
</div>
<div class={} id={}>
</div>

</body>
</html>""".format('rc4', encrypted.hex(), 'key', 'key123' )

f.write(message.encode('utf-8'))
f.close()

webbrowser.open_new_tab('index.html')
