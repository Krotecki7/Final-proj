FROM python:3.12-slim

WORKDIR /.

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SECRET_KEY='django-insecure-bq#_1b_um#0s)8ipvtjjjs!y_!tbe52#9%x&hgk(c72g4+vwi5'

RUN mkdir -p /media

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]