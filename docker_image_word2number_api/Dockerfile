FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements-prod.txt

EXPOSE 8000

CMD ["waitress-serve", "--port=8000", "app:api"]