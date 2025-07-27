FROM python:3.10-slim

WORKDIR /app

COPY scripts/ scripts/
COPY Collection_1/ Collection_1/
COPY Collection_2/ Collection_2/
COPY Collection_3/ Collection_3/
COPY requirements.txt .
COPY README.md .
COPY run_all.sh .

ENV PYTHONPATH="/app"

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x run_all.sh

CMD ["./run_all.sh"]
