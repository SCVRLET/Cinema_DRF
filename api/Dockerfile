FROM python:3.8-alpine
ENV PYTHONPATH=${PYTHONPATH}:/app
WORKDIR /app
RUN apk update \
        && apk add --no-cache gcc make libc-dev \
        postgresql-dev python3-dev build-base \
        linux-headers pcre-dev jpeg-dev zlib-dev \
        freetype-dev lcms2-dev openjpeg-dev tiff-dev \
        tk-dev tcl-dev curl
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
COPY ./poetry.lock ./pyproject.toml  /app/
ENV PATH=/root/.poetry/bin:${PATH}
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . /app