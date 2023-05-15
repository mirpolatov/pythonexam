FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV TOKEN = " "

WORKDIR /apps

COPY .. /apps



RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r requirement.txt

ENTRYPOINT ["python","exam.py"]

