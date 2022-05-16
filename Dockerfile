FROM python-36-centos:latest
RUN pip3 install -i -r requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 5000
CMD ["python3", "app.py"]
