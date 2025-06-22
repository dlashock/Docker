FROM debian:stable-slim

# COPY source destination
COPY Docker /bin/goserver

ENV PORT=8991

CMD ["/bin/goserver"]