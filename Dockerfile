FROM python:3.6
WORKDIR /Project/pj1

ARG APP_NAME=main
ENV APP_NAME=${APP_NAME}

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY ./${APP_NAME}.py ./${APP_NAME}.py
COPY ./start.sh ./start.sh

RUN chmod +x ./*.sh

ENV FLASK_APP=${APP_NAME}.py
ENTRYPOINT ["/Project/pj1/start.sh"]
