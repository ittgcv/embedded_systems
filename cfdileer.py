from cfdiclient import Autenticacion
from cfdiclient import Fiel

FIEL_KEY = 'Claveprivada_FIEL_PEPM710624PY5_20171108_112525.key'
FIEL_CER = 'pepm710624py5.cer'
FIEL_PAS = 'sdjazmin'
cer_der = open(FIEL_CER, 'rb').read()
key_der = open(FIEL_KEY, 'rb').read() 
fiel = Fiel(cer_der, key_der, FIEL_PAS)

auth = Autenticacion(fiel)

token = auth.obtener_token()

print(token)
