FROM python:3

ENV CONTAINER true

RUN mkdir /app

COPY *.* /app/

WORKDIR /app

RUN pip install -r requirements.txt

RUN python dataPresenter.py

EXPOSE 8000/tcp

CMD [ "python", "-m", "http.server" ]