from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

db_config = {
    'host': 'localhost',      
    'user': 'root',     
    'password': '', 
    'database': 'Animali'  
}

@app.route('/dati', methods=['GET'])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        # Query per ottenere tutti i dati
        query = "SELECT * FROM Pesci"
        cursor.execute(query)
        result = cursor.fetchall()
        
        return jsonify(result)
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile connettersi al database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/dati/crea', methods=['POST'])
def create_animal():
    data = request.get_json()

    nome_comune = data.get('Nome_Comune')
    famiglia = data.get('Famiglia')
    ambiente = data.get('Ambiente')
    dimensioni = data.get('Dimensioni')
    alimentazione = data.get('Alimentazione')

    if not nome_comune or not famiglia or not ambiente or not dimensioni or not alimentazione:
        return jsonify({"errore": "Tutti i campi (Nome_Comune, Famiglia, Ambiente, Dimensioni, Alimentazione) sono obbligatori"}), 400

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "INSERT INTO Pesci (Nome_Comune, Famiglia, Ambiente, Dimensioni, Alimentazione) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(query, (nome_comune, famiglia, ambiente, dimensioni, alimentazione))
        conn.commit()

        return jsonify({"successo": "Nuovo animale creato", "id": cursor.lastrowid}), 201
    
    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile inserire l'animale nel database"}), 500
    
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


@app.route('/dati/elimina/<int:id>', methods=['DELETE'])
def delete_animal(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "DELETE FROM Pesci WHERE Id = %s"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"errore": "Animale non trovato"}), 404

        return jsonify({"successo": "Animale eliminato"}), 200

    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile eliminare l'animale nel database"}), 500

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()



            @app.route('/dati/aggiorna/<int:id>', methods=['PUT'])
def update_animal(id):
    data = request.get_json()

    # Estrazione dei dati dal corpo della richiesta
    nome_comune = data.get('Nome_Comune')
    famiglia = data.get('Famiglia')
    ambiente = data.get('Ambiente')
    dimensioni = data.get('Dimensioni')
    alimentazione = data.get('Alimentazione')

    # Validazione dei dati: tutti i campi devono essere presenti
    if not nome_comune or not famiglia or not ambiente or not dimensioni or not alimentazione:
        return jsonify({"errore": "Tutti i campi (Nome_Comune, Famiglia, Ambiente, Dimensioni, Alimentazione) sono obbligatori"}), 400

    try:
        # Connessione al database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query per aggiornare i dati nella tabella 'Pesci'
        query = """
        UPDATE Pesci
        SET Nome_Comune = %s, Famiglia = %s, Ambiente = %s, Dimensioni = %s, Alimentazione = %s
        WHERE Id = %s
        """
        # Esegui la query di aggiornamento con i nuovi valori
        cursor.execute(query, (nome_comune, famiglia, ambiente, dimensioni, alimentazione, id))
        conn.commit()

        # Verifica se l'animale è stato trovato e aggiornato
        if cursor.rowcount == 0:
            return jsonify({"errore": "Animale non trovato"}), 404

        return jsonify({"successo": "Animale aggiornato"}), 200

    except Error as e:
        print("Errore nella connessione al database:", e)
        return jsonify({"errore": "Impossibile aggiornare l'animale nel database"}), 500

    finally:
        # Chiudi la connessione al database
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
