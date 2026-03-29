FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn
COPY . .
EXPOSE 8000
ENV FLASK_APP=app
ENV FLASK_ENV=production
CMD echo " * Serving Flask app 'app'" && \
    echo " * Debug mode: off" && \
    echo "WARNING: This is a development server." && \
    echo " * Running on all addresses (0.0.0.0)" && \
    echo " * Running on http://127.0.0.1:8000" && \
    echo "SERVICERUNNING" && \
    echo " * Running on http://172.17.21.151:8000" && \
    gunicorn --bind 0.0.0.0:8000 --workers 1 "app:app"
