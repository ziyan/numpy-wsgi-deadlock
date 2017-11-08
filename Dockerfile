FROM debian:stretch

RUN \
    apt-get update; \
    apt-get install -y -qq apache2 libapache2-mod-wsgi python-pip; \
    rm -rf /var/lib/apt/lists/*

RUN \
    pip install numpy; \
    rm -f /etc/apache2/sites-enabled/000-default.conf; \
    mkdir -p /app

ADD hello.conf /etc/apache2/sites-enabled/
ADD hello.bash hello.wsgi /app/

ENTRYPOINT /app/hello.bash
