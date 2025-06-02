
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

RUN pip install spacy && \
    python -m spacy download en_core_web_sm

# Copy the requirements file
COPY ./requirements.txt ./requirements.txt

COPY ./ /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/app/get_movielens_datasets.py"]