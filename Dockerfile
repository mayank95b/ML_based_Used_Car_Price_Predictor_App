FROM python:3
COPY . /usr/app
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --no-cache-dir -r requirements.txt
CMD python new_flask.py
