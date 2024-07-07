FROM python:3.12-bullseye

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip --root-user-action=ignore

RUN pip install -r requirements.txt --root-user-action=ignore

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
