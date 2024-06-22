FROM python 

WORKDIR /site_jujutsu

COPY . .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]