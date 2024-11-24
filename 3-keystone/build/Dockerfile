# Base image
FROM ubuntu:bionic

# Evita richieste interattive durante l'installazione di pacchetti
ENV DEBIAN_FRONTEND=noninteractive
ENV LC_CTYPE=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US \
    TZ=Europe/Rome

# Setta la versione di OpenStack (opzionale)
ARG OPENSTACK_VERSION="stein"

# Aggiorna i pacchetti e installa dipendenze essenziali
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        dialog apt-utils software-properties-common locales curl tzdata python3-openstackclient keystone mysql-client && \
    locale-gen en_US.UTF-8 && \
    echo $TZ > /etc/timezone && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    add-apt-repository -y cloud-archive:$OPENSTACK_VERSION && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Configura i log di Keystone
RUN mkdir -p /var/log/keystone && \
    touch /var/log/keystone/keystone-manage.log \
          /var/log/keystone/keystone-wsgi-public.log \
          /var/log/keystone/keystone.log && \
    chown -R keystone:keystone /var/log/keystone

# Espone directory configurabili e porta di Keystone
VOLUME ["/etc/keystone", "/var/log/keystone"]
EXPOSE 5000

# Comando di default
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
