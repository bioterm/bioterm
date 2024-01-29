FROM python:3.11

WORKDIR /

COPY bioterm/server/backend/requirements.txt /bioterm/server/backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /bioterm/server/backend/requirements.txt

COPY bioterm/common /bioterm/common

COPY bioterm/server/backend /bioterm/server/backend

# CMD ["uvicorn", "bioterm.server.backend.app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8001"]
# CMD ["gunicorn", "bioterm.server.backend.app.main:app",  "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind" "0.0.0.0"]
