FROM python:3.11-slim

RUN mkdir /app
WORKDIR /app

RUN apt-get upgrade -y
RUN apt-get install -y
RUN apt-get update -qqy && apt-get -qqy install -y apt-utils wget sudo curl unzip jq mc libpq-dev build-essential \
    tzdata ca-certificates libssl-dev autoconf libtool make \
    software-properties-common git \
    && rm -rf /var/lib/apt/lists/*

# upgrade PIP, copy and install packages from requirements.txt
COPY /requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY /src /app/src

RUN chmod -R a+rwx /app/

ENV SPREADSHEET_ID=1-TB70kDSqz5f0yv8BcyrqCUewsRqaiqiz8YRfkmYReE
ENV SHEET_CELLS=!F35:G48
ENV SCOPES=https://www.googleapis.com/auth/spreadsheets.readonly
ENV FILENAME=Expensify.xlsx
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
#CMD ["python", "-m", "streamlit ", "run", "/src/expense_analysis/main.py"]
#ENTRYPOINT ["streamlit", "run", "src/main/expense_analysis/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
ENTRYPOINT ["streamlit", "run", "src/main/expense_analysis/main.py", "--server.port=8501"]