import json

# Funzione per trasformare il JSON
def transform_json(data):
    transformed_data = []

    for index, entry in enumerate(data):
        # Creiamo un nuovo dizionario per ogni entry
        question = entry['context']
        responses = entry['responses']
        fact = entry['fact']
        
        # Creiamo una nuova entry con la struttura desiderata
        transformed_entry = {
            "question_id": index + 1,  # Iniziamo da 1
            "question": question,
            "fact": fact,
            "response": {}
        }
        
        # Aggiungiamo le risposte per ogni modello
        for response in responses:
            model_name = response['model']
            transformed_entry["response"][model_name] = response['response']
        
        # Aggiungiamo l'entry trasformata alla lista finale
        transformed_data.append(transformed_entry)
    
    return transformed_data

if __name__ == "__main__":
    # Caricamento del JSON di input
    with open("./DATASET/pc_usr_data.json", "r") as file:
        input_data = json.load(file)

    # Trasformiamo il JSON
    transformed_data = transform_json(input_data)

    # Salviamo il risultato in un nuovo file JSON
    with open("./DATASET/transformed_data.json", "w") as file:
        json.dump(transformed_data, file, indent=4)

    print("Trasformazione completata. Dati salvati in 'transformed_data.json'")