FROM python:3
COPY . /application
WORKDIR /application
RUN pip install -r requirements.txt
CMD streamlit run app.py