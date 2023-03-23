FROM python:slim-buster
WORKDIR /app
COPY ./.env /app
COPY ./app.py /app
RUN pip install flask requests python-dotenv
CMD [ "python", "app.py" ]
EXPOSE 5024




