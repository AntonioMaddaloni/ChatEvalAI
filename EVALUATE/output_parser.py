import json
import numpy as np

def parse_model_for_results(models_data = ''):
    # Aprire e leggere il file JSON
    with open(models_data, "r") as file:
        data_model = json.load(file)
    # Iterare su ogni "question"
    questions = []
    for question in data_model:        
        # Estrarre i voti per ogni assistente
        evaluations = question['evaluation']
        for assistant in ["The score of Assistant 1", "The score of Assistant 2", "The score of Assistant 3", "The score of Assistant 4", "The score of Assistant 5"]:
            votes = []
            # Iterare sui voti dati da Critic, Psychologist e Author
            for eval_entry in evaluations:
                evaluation_text = eval_entry["evaluation"]
                score_line = [line for line in evaluation_text.split("\n") if assistant in line]
                
                if score_line:
                    # Estrarre il voto (l'ultima parte della riga)
                    number = score_line[0].split(":")[-1].strip()
                    if(number == '0/5'):
                        number = '0'
                    elif(number == '1/5'):
                        number = '1'
                    elif(number == '2/5'):
                        number = '2'
                    elif(number == '3/5'):
                        number = '3'
                    elif(number == '4/5'):
                        number = '4'
                    elif(number == '5/5'):
                        number = '5'
                    score = round((float(number) + np.random.normal(0, 0.01)),3)
                    votes.append(score)
            
            # ottieni voti per la question
            questions.append(votes)
    return questions


def parse_human_for_results(human_data = ''):
    # Aprire e leggere il file JSON
    with open(human_data, "r") as file:
        data_model = json.load(file)
    # Iterare su ogni "question"
    votes = []
    for question in data_model:
        for response in question['responses']:
            votes.append( [round(x + np.random.normal(0, 0.01),3) for x in response['Overall']])
    return votes
