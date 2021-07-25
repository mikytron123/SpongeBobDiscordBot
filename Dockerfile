FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod +x bot.py

CMD ["python","-u", "bot.py"]
