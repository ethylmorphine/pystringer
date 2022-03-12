FROM alpine:3.14
RUN apk update && apk add --no-cache python3 make gcc musl-dev linux-headers python3-dev

RUN mkdir /py
COPY ./py/ /py/

RUN ls -l /py

RUN make -C /py init

ENTRYPOINT make -C /py deploy
