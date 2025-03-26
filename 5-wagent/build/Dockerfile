# Base image
FROM ubuntu:bionic

# Impostazioni delle variabili d'ambiente
ENV DEBIAN_FRONTEND=noninteractive \
    LC_CTYPE=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    TZ=Europe/Rome

# Installazione delle dipendenze di sistema e configurazione iniziale
RUN apt-get update && apt-get install -y --no-install-recommends \
        nano \
        software-properties-common \
        locales \
        tzdata \
        build-essential \
        python3 \
        python3-pip \
        python3-setuptools \
        python3-openstackclient \
        git \
        apache2 \
        libapache2-mod-wsgi-py3 \
        rustc \
    && locale-gen en_US.UTF-8 \
    && echo $TZ > /etc/timezone \
    && ln -fs /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copia del repository iotronic nel container
COPY ./iotronic /opt/build/iotronic

# Imposta la directory di lavoro
WORKDIR /opt/build/iotronic

# Installazione di Python e pacchetti richiesti
RUN pip3 install --upgrade pip setuptools-rust \
    && pip3 install --ignore-installed PyYAML \
    && pip3 install \
        "pbr!=2.1.0,>=2.0.0" \
        "eventlet!=0.18.3,!=0.20.1,>=0.18.2" \
        "oslo.config>=5.2.0" \
        "oslo.log>=3.36.0" \
        "oslo.concurrency>=3.26.0" \
        "oslo.policy>=1.35.0" \
        "oslo.messaging>=6.3.0" \
        "oslo.db>=4.27.0" \
        "paramiko>=2.0.0" \
        "SQLAlchemy!=1.1.5,!=1.1.6,!=1.1.7,!=1.1.8,>=1.0.10" \
        "keystonemiddleware>=4.17.0" \
        "autobahn>=18.10.1" \
        "python-neutronclient>=6.7.0" \
        "python-designateclient>=2.11.0" \
        "pecan!=1.0.2,!=1.0.3,!=1.0.4,!=1.2,>=1.0.0" \
        "PyMySQL>=0.7.6" \
        "osprofiler>=1.5.0" \
        "WSME>=0.8" \
    && python3 setup.py install

# Creazione dell'utente iotronic e configurazione dei log
RUN useradd -m -d /var/lib/iotronic iotronic \
    && mkdir -p /var/log/iotronic \
    && touch /var/log/iotronic/iotronic-wagent.log \
    && chown -R iotronic:iotronic /var/log/iotronic/
    && sed -i "s/\.with_lockmode('update')/.with_for_update()/g" $(find /usr/local/lib -type f -path "*iotronic/db/sqlalchemy/api.py")
    
# Monta volumi per configurazione e log
VOLUME ["/etc/iotronic", "/var/log/iotronic"]

# Comando di default per avvio del WAMP agent
CMD ["/usr/local/bin/iotronic-wamp-agent"]
