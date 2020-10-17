import webbrowser
from oscrypto import symmetric
import codecs

key = input('Ingrese llave: ')
plain_text = input('Ingrese texto plano a encriptar: \n')


while len(key) < 5 or len(key) > 16:
    key = input('La llave debe tener un tamaño entre 5 a 16 caracteres, vuelva a ingresar la llave: ')



encrypted = symmetric.rc4_encrypt(codecs.encode(key,'utf-8'), codecs.encode(plain_text,'utf-8'))


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
</html>""".format('rc4', encrypted.hex(), 'key', key )

f.write(message.encode('utf-8'))
f.close()

webbrowser.open_new_tab('index.html')
