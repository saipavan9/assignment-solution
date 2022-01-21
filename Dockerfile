FROM python:3.9
RUN pip install python-socketio uvicorn[standard] python-logging-loki

RUN mkdir app
WORKDIR app

COPY server.py .
EXPOSE 8000

CMD ["uvicorn", "server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
