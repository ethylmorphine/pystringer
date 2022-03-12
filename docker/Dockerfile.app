FROM alpine:3.14
RUN apk update && apk add --no-cache python3 make gcc

RUN mkdir /py
COPY ./py/* /py/

RUN make -C /py init
