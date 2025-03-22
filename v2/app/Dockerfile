FROM python:3.13.2

WORKDIR /usr/src/app/backend/app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

EXPOSE 8081

CMD ["fastapi", "run", "main.py", "--port", "8081"]