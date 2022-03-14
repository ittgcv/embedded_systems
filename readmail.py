# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals
import smtplib
import time
import imaplib
import email
import spacy
from limpiacadena import  limpiacadena
#import es_core_news_md
from spacy.matcher import Matcher
import pandas as pd
nlp = spacy.load('es_core_news_sm')
matcher = Matcher(nlp.vocab)
pattern = [{'ORTH':'Citibanamex'}, {'LOWER': 'bancomer'}, {'LOWER': 'banamex'}, {'LOWER': 'citibanamex'}, {'LOWER': 'tarjeta'}, {'LOWER': 'Cuenta'}]
matcher.add('HelloWorld', None, pattern)
#terminology_list = ['San Cristobal', 'centro historico', 'catedral']
#patterns = [nlp(text) for text in terminology_list]
# matcher.add('TerminologyList', None, *patterns)
#pattern = ['Citibanamex']
#matcher.add("Bancos", None, patterns)

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL   = "@ittg.edu.mx"
FROM_EMAIL  = "mperez" + ORG_EMAIL
FROM_PWD    = "idjazmin"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
myEmail={}
def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    subject = msg['subject'].lower()
                    email_subject = unicode(subject, "utf-8")
                    email_subject=limpiacadena(email_subject)
                    email_from = msg['from']
                    myEmail[i]={'asunto':email_subject, 'from':email_from}
                    print("asunto"+email_subject)
                    doc = nlp(email_subject)
                    # for token in doc:
                    #     print(token.text)
                    matches = matcher(doc)
                    for match_id, start, end in matches:
                        string_id = nlp.vocab.strings[match_id]  # get string representation
                        span = doc[start:end]  # the matched span
                        print(match_id, string_id, start, end, span.text)


#    except Exception, e:
    except:
        pass
        #print str(e)
read_email_from_gmail()
dfmyCorreo=pd.DataFrame(myEmail)
print(dfmyCorreo.head())
dfmyCorreo.to_csv("correos.csv", encoding='utf-8')
print('terminado')
