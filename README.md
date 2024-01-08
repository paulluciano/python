Docker code for an image and container.

Project consists of two (2) parts
|- *.py file
|- Dockerfile

*** Dockerfile Contents BEGIN ***
FROM python:latest

RUN pip install --upgrade pip && \
    pip install pytz

COPY test.py /

CMD [ "python", "./test.py" ]
*** Dockerfile Contents END ***

*** Compile code ***
docker build -t python-time .

NOTE: Assume two (2) files are located in a single folder .../code and command prompt is at same level [name]@[server]:.../code$
