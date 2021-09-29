from flask import Flask
import src.write_html as wh
import src.files as f

app = Flask(__name__)

@app.route('/generer/<name>/<first_name>/<eng>/<month>')
def generer(name, first_name, eng, month):
    # try :
        month = int(month)
        # if not (1 <= month <= 12):
        #     raise Exception
        # if eng not in ['a', 'b', 'A', 'B'] :
        #     raise Exception
        path = wh.write_in_html(name.upper(), first_name.capitalize(), month, eng)
        return f.read_all_file(path)
    # except :
    #     return '''
    #     <h1>Règles:</h1>
    #     <ul>
    #     <li>Le mois doit être un nombre entre 1 et 12.</li>
    #     <li>Le groupe d'anglais doit être a, A, b ou B.</li>
    #     <li>Url : generer/nom/prenom/groupe_anglais/mois.</li>
    #     </ul>
    #     '''

if __name__ == '__main__':
    app.run(threaded=True, host='127.0.0.1', port=5000)
