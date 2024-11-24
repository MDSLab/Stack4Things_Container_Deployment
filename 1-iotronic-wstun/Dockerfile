# Dockerfile per wstun
FROM node:carbon-alpine

# Versione del pacchetto wstun
ENV VERSION=1.0.11

# Installazione dipendenze necessarie
RUN npm install -g --unsafe websocket@1.0.26 \
    optimist@0.6.1 \
    node-uuid@1.4.7 \
    under_score \
    log4js@1.1.1 \
    && npm cache --force clean

# Imposta la directory di lavoro per l'installazione di wstun
WORKDIR /usr/local/lib/node_modules/@mdslab/

# Copia il pacchetto wstun dalla cartella `confs` e lo estrae
COPY ./confs/wstun-$VERSION.tar.gz ./wstun-$VERSION.tar.gz
RUN tar zxfv wstun-$VERSION.tar.gz \
    && mv wstun-$VERSION wstun \
    && rm wstun-$VERSION.tar.gz

# Configura il percorso NODE_PATH per npm
ENV NODE_PATH=/usr/local/lib/node_modules

# Imposta la directory di lavoro finale
WORKDIR /usr/bin/

# Esponi porte utilizzate da wstun
EXPOSE 40001-40050
EXPOSE 8080

# Crea directory per i log di wstun
RUN mkdir -p /var/log/wstun/

# Copia il file binario wstun.js nel percorso corretto
COPY ./confs/bin/wstun.js /usr/local/lib/node_modules/@mdslab/wstun/bin/

# Imposta i certificati SSL nella directory corretta
RUN mkdir -p /var/lib/iotronic/ssl/

# Entry point del container, configurato per usare SSL
ENTRYPOINT ["node", "/usr/local/lib/node_modules/@mdslab/wstun/bin/wstun.js", "-r", "-s", "8080", "--ssl=true", "--key=/var/lib/iotronic/ssl/iotronic.key", "--cert=/var/lib/iotronic/ssl/iotronic.pem"]
