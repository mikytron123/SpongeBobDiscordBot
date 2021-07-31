FROM python:3.7

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
RUN chmod +x bot.py
RUN wget -O uni.ttf "https://img.download-free-fonts.com/dl.php?id=88978&hash=40d13c72f9bd682a8df865b946eb4e10"
RUN wget -O color.ttf https://github.com/googlefonts/noto-emoji/blob/main/fonts/NotoEmoji-Regular.ttf?raw=true
CMD ["python","-u", "bot.py"]
