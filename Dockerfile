FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /resume_ranker/

COPY requirements.txt /resume_ranker/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]