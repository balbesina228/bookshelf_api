FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r reqs.txt

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]