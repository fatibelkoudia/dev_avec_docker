FROM python:3.9
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN useradd --create-home --shell /usr/sbin/nologin appuser \
    && chown -R appuser:appuser /server
USER appuser
EXPOSE 8000
