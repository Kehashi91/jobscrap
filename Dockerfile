FROM python:3.5.6
WORKDIR /jobscrap/jobs
COPY . /jobscrap
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "runscript.py"]