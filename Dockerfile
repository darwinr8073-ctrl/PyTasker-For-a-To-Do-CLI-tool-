
FROM python:3.11-slim

WORKDIR /app

COPY Python_project_2-11-26.py .

CMD ["python", "Python_project_2-11-26.py"]
