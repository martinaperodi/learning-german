import pandas as pd
import spacy
from collections import Counter

# 1. Carichiamo il modello linguistico tedesco
nlp = spacy.load("de_core_news_sm")

def analizza_tedesco(file_path):
    # 2. Leggiamo il file di testo
    with open(file_path, 'r', encoding='utf-8') as f:
        testo = f.read()

    # 3. Analizziamo il testo con spaCy
    # (Dividiamo il testo in pezzi più piccoli se è un libro intero per non sovraccaricare la RAM)
    doc = nlp(testo)

    # 4. Estraiamo i lemmi
    # Escludiamo punteggiatura, numeri e le "Stop words" (parole comuni come 'der', 'die', 'das')
    lemmi = [
        token.lemma_.lower() 
        for token in doc 
        if token.is_alpha and not token.is_stop
    ]

    # 5. Contiamo le frequenze
    frequenze = Counter(lemmi)

    # 6. Creiamo un DataFrame con Pandas
    df = pd.DataFrame(frequenze.items(), columns=['Parola', 'Frequenza'])

    # 7. Ordiniamo in modo discendente
    df = df.sort_values(by='Frequenza', ascending=False)

    return df

# Esecuzione
if __name__ == "__main__":
    file_da_leggere = "pg30165.txt"
    risultato = analizza_tedesco(file_da_leggere)

    # Salviamo il risultato in un file CSV per aprirlo con Excel o Numbers
    risultato.to_csv("analisi_vocaboli_tedesco.csv", index=False)
    
    print("Analisi completata! Trovi i risultati in 'analisi_vocaboli_tedesco.csv'")
    print(risultato.head(20)) # Mostra le prime 20 parole nel terminale