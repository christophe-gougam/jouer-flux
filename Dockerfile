FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV FLASK_APP=run.py

# Exposer le port 5000 (le port par défaut de Flask)
EXPOSE 5000

# Commande pour lancer l'application Flask
CMD ["flask", "run", "--host=0.0.0.0"]
