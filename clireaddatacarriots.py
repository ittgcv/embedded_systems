from clicarriots import api
from datetime import datetime

client_stream = api.Stream("YOUR APIKEY")

code, response = client_stream.get("madainperez")
print(code, response)
