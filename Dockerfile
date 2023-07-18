FROM python:3.9

# Copia il file Python nel container
COPY kernel_classification.py .
COPY requirements.txt .
COPY send_results.py .
COPY catch_topic.py .
COPY model.joblib .
# Installa le dipendenze del file Python se necessario
RUN pip install --no-cache-dir -r requirements.txt

# Comando CMD che esegue il file Python utilizzando l'argomento dalla variabile d'ambiente
CMD ["python3", "catch_topic.py"]
