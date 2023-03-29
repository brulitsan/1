FROM python:3.10-alpine

ENV PYTHONDONTERITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY /stazhirovka/ .

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]