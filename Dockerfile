FROM python:3.10

RUN mkdir -p /opt/TestProj
WORKDIR /opt/TestProj
ADD . /opt/TestProj

RUN pip3 install --no-cache-dir -e .[docs]
# build doc
RUN mkdocs build
CMD [ "mkdocs", "serve" ]