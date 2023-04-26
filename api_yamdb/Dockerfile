FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
LABEL author='https://github.com/dnltv' version=2.1