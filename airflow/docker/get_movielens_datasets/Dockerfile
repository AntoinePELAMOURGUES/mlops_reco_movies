
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt ./requirements.txt

COPY ./get_movielens_datasets.py /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/get_movielens_datasets.py"]