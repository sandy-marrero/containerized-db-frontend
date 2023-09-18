FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENV NAME World

CMD ["python", "app/app.py"]
