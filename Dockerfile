FROM openshift/base-centos7

LABEL io.k8s.description="Test HTTP Server" \
      io.k8s.display-name="Test HTTP Server" \
      io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" \
      io.openshift.expose-services="9090:http" \
      io.openshift.tags="builder,http"

COPY app.py /opt/app-root/
COPY response.json /opt/app-root/

EXPOSE 9090

USER 1001

WORKDIR /opt/app-root

CMD [ "python", "/opt/app-root/app.py" ]
