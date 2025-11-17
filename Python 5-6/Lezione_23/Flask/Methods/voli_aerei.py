dati = {
    'Nazione': {
        1: {
            'id': 1,
            'nome': 'Italia'
        }
    },

    'Citta': {
        1: {
            'id': 1,
            'n_abitanti': 60000,
            'nome': 'Pomezia',
            'nazione': 1
        },
        2: {
            'id': 2,
            'n_abitanti': 2500000,
            'nome': 'Roma',
            'nazione': 1
        }
    },

    'Aeroporto': {
        1: {
            'id': 1,
            'codice': 'FCO',
            'nome': 'Aeroporto di Fiumicino',
            'citta': 2
        },
        2: {
            'id': 2,
            'codice': 'CIA',
            'nome': 'Aeroporto di Ciampino',
            'citta': 2
        },
        3: {
            'id': 3,
            'codice': 'MXP',
            'nome': 'Aeroporto di Malpensa',
            'citta': 2
        },
        4: {
            'id': 4,
            'codice': 'BLQ',
            'nome': 'Aeroporto di Bologna',
            'citta': 1
        }
    },

    'CompagniaAerea': {
        1: {
            'id': 1,
            'nome': 'Alitalia',
            'fondazione': 1946,
            'citta': 2
        },
        2: {
            'id': 2,
            'nome': 'Ryanair',
            'fondazione': 1984,
            'citta': 2
        },
        3: {
            'id': 3,
            'nome': 'EasyJet',
            'fondazione': 1995,
            'citta': 2
        },
        4: {
            'id': 4,
            'nome': 'Wizz Air',
            'fondazione': 2003,
            'citta': 1
        }
    },

    'Volo': {
        1: {
            'id': 1,
            'codice': 'AZ123',
            'durata_in_minuti': 90,
            'partenza': 1,
            'arrivo': 2,
            'compagnia': 1
        },
        2: {
            'id': 2,
            'codice': 'RY456',
            'durata_in_minuti': 120,
            'partenza': 2,
            'arrivo': 4,
            'compagnia': 2
        },
        3: {
            'id': 3,
            'codice': 'EZ789',
            'durata_in_minuti': 75,
            'partenza': 2,
            'arrivo': 3,
            'compagnia': 3
        },
        4: {
            'id': 4,
            'codice': 'WZ321',
            'durata_in_minuti': 60,
            'partenza': 4,
            'arrivo': 1,
            'compagnia': 4
        }
    }
}

from flask import Flask, jsonify, request
app = Flask(__name__)

# flask --app voli_aerei run --debug
#http://127.0.0.1:5000/nazioni/

@app.route('/')
def home() -> str:
    return "Ciao sono Nicol"

#NAZIONI:
@app.route('/nazioni', methods=['GET'])
def get_nazioni() -> dict:
    return jsonify(dati['Nazione']), 200

@app.route('/nazioni/<int:id>', methods=['GET'])
def get_nazione(id : int) -> tuple[dict, int]:
    if id in dati['Nazione']:
        return jsonify(dati['Nazione'][id]), 200
    else:
        return jsonify({'errore': f'Nazione con id {id} non trovato'}), 404

@app.route('/nazioni', methods=['POST'])
def post_nazione() -> tuple[dict, int]:
    nazione = request.get_json()
    new_id = len(dati['Nazione']) + 1

    if 'id' not in nazione:
        return jsonify({'errore': 'Inserire id'}), 400

    if not nazione or 'nome' not in nazione:
        return jsonify({'errore': 'Inserire nome'}), 400
    
    if nazione['id'] in dati['Nazione']:
        return jsonify({'errore': 'Id già presente'}), 400

    dati['Nazione'][new_id] = {
        'id' : nazione['id'],
        'nome' : nazione['nome']
    }
    return jsonify(dati['Nazione'][new_id]), 201

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#CITTÀ
@app.route('/citta', methods=['GET'])
def get_cittas() -> tuple[dict, int]:
    return jsonify(dati['Citta']), 200

@app.route('/citta/<int:id>', methods=['GET'])
def get_citta(id : int) -> tuple[dict, int]:
    if id in dati['Citta']:
        return jsonify(dati['Citta'][id]), 200
    else:
        return jsonify({'errore': f'Città con id {id} non trovata'}), 404
    
@app.route('/citta', methods=['POST'])
def post_citta() -> tuple[dict, int]:
    citta = request.get_json()

    if not citta:
        return jsonify({'errore': 'json vuoto'}), 400
    
    if 'id' not in citta:
        return jsonify({'errore': 'Inserire id'}), 400
    
    if 'n_abitanti' not in citta:
        return jsonify({'errore': 'Inserire n_abitanti'}), 400

    if 'nome' not in citta:
        return jsonify({'errore': 'Inserire nome'}), 400
    
    if 'nazione' not in citta:
        return jsonify({'errore': 'Inserire nazione'}), 400

    if citta['id'] in dati['Citta']:
        return jsonify({'errore': 'Id già presente'}), 400
    
    if citta['nazione'] not in dati['Nazione']:
        return jsonify({'errore': 'Nazione inesistente'}), 400

    dati['Citta'][citta['id']] = {
        'id' : citta['id'],
        'nome' : citta['nome'],
        'n_abitanti': citta['n_abitanti'],
        'nazione': citta['nazione']
    }
    return jsonify(dati['Citta'][citta['id']]), 201

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#AEROPORTO
@app.route('/aeroporto', methods=['GET'])
def get_aeroporti() -> tuple[dict, int]:
    return jsonify(dati['Aeroporto']), 200

@app.route('/aeroporto/<int:id>', methods=['GET'])
def get_aeroporto(id : int) -> tuple[dict, int]:
    if id in dati['Aeroporto']:
        return jsonify(dati['Aeroporto'][id]), 200
    else:
        return jsonify({'errore': f'Aeroporto con id {id} non trovato'}), 404
    
@app.route('/aeroporto', methods=['POST'])
def post_aeroporto() -> tuple[dict, int]:
    aeroporto = request.get_json()

    if not aeroporto:
        return jsonify({'errore': 'json vuoto'}), 400
    
    if 'id' not in aeroporto:
        return jsonify({'errore': 'Inserire id'}), 400
    
    if 'codice' not in aeroporto:
        return jsonify({'errore': 'Inserire codice'}), 400

    if 'nome' not in aeroporto:
        return jsonify({'errore': 'Inserire nome'}), 400
    
    if 'citta' not in aeroporto:
        return jsonify({'errore': 'Inserire citta'}), 400

    if aeroporto['id'] in dati['Aeroporto']:
        return jsonify({'errore': 'Id già presente'}), 400
    
    if aeroporto['citta'] not in dati['Citta']:
        return jsonify({'errore': 'citta inesistente'}), 400

    dati['Aeroporto'][aeroporto['id']] = {
        'id' : aeroporto['id'],
        'nome' : aeroporto['nome'],
        'codice': aeroporto['codice'],
        'citta': aeroporto['citta']
    }
    return jsonify(dati['Aeroporto'][aeroporto['id']]), 201


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#


#COMPAGNIA
@app.route('/compagnia', methods=['GET'])
def get_compagnie() -> tuple[dict, int]:
    return jsonify(dati['CompagniaAerea']), 200

@app.route('/compagnia/<int:id>', methods=['GET'])
def get_compagnia(id : int) -> tuple[dict, int]:
    if id in dati['CompagniaAerea']:
        return jsonify(dati['CompagniaAerea'][id]), 200
    else:
        return jsonify({'errore': f'compagnia con id {id} non trovato'}), 404
    
@app.route('/compagnia', methods=['POST'])
def post_compagnia() -> tuple[dict, int]:
    compagnia = request.get_json()

    if not compagnia:
        return jsonify({'errore': 'json vuoto'}), 400
    
    if 'id' not in compagnia:
        return jsonify({'errore': 'Inserire id'}), 400
    
    if 'fondazione' not in compagnia:
        return jsonify({'errore': 'Inserire fondazione'}), 400

    if 'nome' not in compagnia:
        return jsonify({'errore': 'Inserire nome'}), 400
    
    if 'citta' not in compagnia:
        return jsonify({'errore': 'Inserire citta'}), 400

    if compagnia['id'] in dati['CompagniaAerea']:
        return jsonify({'errore': 'Id già presente'}), 400
    
    if compagnia['citta'] not in dati['Citta']:
        return jsonify({'errore': 'citta inesistente'}), 400

    dati['CompagniaAerea'][compagnia['id']] = {
        'id' : compagnia['id'],
        'nome' : compagnia['nome'],
        'fondazione': compagnia['fondazione'],
        'citta': compagnia['citta']
    }
    return jsonify(dati['CompagniaAerea'][compagnia['id']]), 201
