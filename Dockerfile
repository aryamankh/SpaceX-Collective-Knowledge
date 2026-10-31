FROM alpine AS base

FROM scratch

ADD kb /kb

COPY --from=base etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/

ENV PORT=80
EXPOSE 80

ENTRYPOINT ["/kb"]
