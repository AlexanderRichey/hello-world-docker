FROM public.ecr.aws/docker/library/python:3.7-slim

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--log-level=debug", "wsgi"]
