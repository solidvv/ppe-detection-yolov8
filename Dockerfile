FROM ultralytics/ultralytics:latest-python

WORKDIR /ultralytics

COPY . .

CMD ["python", "prediction.py"]