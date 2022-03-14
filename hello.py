from flask import Flask,  redirect,  url_for,  request,  render_template
from werkzeug.utils import secure_filename
import json
#urlhot=usodeurl.ACCESOBD('hotel')
#urlhot.settraining(2)

app = Flask(__name__)
@app.route('/hello/<name>')
def hello_world(name):
    #return "welcome %s" %name
    return render_template('hello.html', nombre=urlhot.text, foto=secure_filename(urlhot.urlphoto))
@app.route('/empaqueta/<name>')
def empaqueta_hotelact(name):
    print ('empaquetando')
    paquetes=empaqueta.empaqueta(name)
    pjson=json.dumps(paquetes)
    print(pjson)
    return "%s" %pjson
@app.route('/clasifyhotel/<name>')
def clasifica_hotel(name):
    empaqueta.empaqueta()
    return "welcome %s" %name
    #return render_template('hello.html', nombre=urlhot.text, foto=secure_filename(urlhot.urlphoto))
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('empaqueta_hotelact', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('empaqueta_hotelact', name=user))
if __name__ == '__main__':
    app.run()
