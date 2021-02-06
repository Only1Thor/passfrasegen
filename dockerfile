FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY randomWordAPI.py .
COPY ordliste.txt .

CMD [ "python", "./randomWordAPI.py" ]