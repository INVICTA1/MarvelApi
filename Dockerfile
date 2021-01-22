#Пишем Dockerfile на инструкциях котороно докер созлает image, а на основе image созда.тся контейнеры
#берем за основу image который уже сущ и в ктр запихнут python
FROM python:3.8
# set the working directory in the container
WORKDIR /API
#
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD ["python","./main.py"]