FROM python:3.10

COPY requirements/development.txt /usr/scr/app/
COPY requirements/base.txt /usr/scr/app/
WORKDIR /usr/scr/app

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r ./development.txt

COPY . /usr/scr/app/
EXPOSE 8000

CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "core.main:app", "--host", "localhost", "--port", "8000"]
#CMD ["uvicorn", "core.main:app", "--port", "8000"]
