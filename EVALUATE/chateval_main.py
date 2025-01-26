from sklearn.metrics import cohen_kappa_score
from scipy.stats import spearmanr, pearsonr, kendalltau
import output_parser as my_parser

# Funzione per calcolare tutte le metriche
def calculate_correlations(human_scores, assistant_scores):
    results = {}
    
    # Dividi i dati in domande: ogni 5 righe rappresentano una domanda
    num_questions = len(human_scores) // 5  # Ogni domanda ha 5 risposte

    for i in range(num_questions):
        # Estrai i 5 voti per ogni domanda (5 risposte per human e assistant)
        human_v = [human_scores[i * 5 + j] for j in range(5)]
        model_v = [assistant_scores[i * 5 + j] for j in range(5)]
        
        # Calcola Kappa di Cohen, Spearman, Pearson, e Kendall-Tau
        kappa_values = []
        spearman_values = []
        pearson_values = []
        kendall_values = []

        # Per ogni assistente nella domanda
        for j in range(5):
            human_discrete = [int(score) for score in human_v[j]]
            model_discrete = [int(score) for score in model_v[j]]
            kappa = cohen_kappa_score(human_discrete, model_discrete)
            kappa_values.append(kappa)
            #print(human_v[j], model_v[j])
            # Correlazioni per ogni assistente (Spearman, Pearson, Kendall-Tau)
            spearman_corr, _ = spearmanr(human_v[j], model_v[j])
            pearson_corr, _ = pearsonr(human_v[j], model_v[j])
            kendall_corr, _ = kendalltau(human_v[j], model_v[j])

            spearman_values.append(spearman_corr)
            pearson_values.append(pearson_corr)
            kendall_values.append(kendall_corr)

        # Media delle metriche per ogni domanda
        results[f"Question {i+1}"] = {
            "Kappa di Cohen": sum(kappa_values) / len(kappa_values),
            "Spearman": sum(spearman_values) / len(spearman_values),
            "Pearson": sum(pearson_values) / len(pearson_values),
            "Kendall-Tau": sum(kendall_values) / len(kendall_values),
        }

    return results

# Dati di input
human_scores = my_parser.parse_human_for_results('./DATASET/pc_usr_data.json')

assistant_scores = my_parser.parse_model_for_results('./DATASET/output_sequential_4.json')

# Calcola le metriche
results = calculate_correlations(human_scores, assistant_scores)

# Scrittura su file
output_file = "./DATASET/results.txt"
with open(output_file, "w") as f:
    for question, metrics in results.items():
        f.write(f"{question}:\n")
        for metric, value in metrics.items():
            f.write(f"{metric}: {value:.4f}\n")
        f.write("\n")
