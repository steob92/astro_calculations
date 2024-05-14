FROM python:latest

COPY . /app

WORKDIR /app
RUN pip install ipython
RUN pip install -r requirements.txt

CMD [ "python3", "/app/run_script.py" ]
