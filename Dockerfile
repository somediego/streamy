# app/Dockerfile

FROM python:slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/somediego/streamy.git .

RUN pip3 install -r requirements.txt

COPY .streamlit /root/.streamlit

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamy.py", "--server.port=8501", "--server.address=0.0.0.0"]
