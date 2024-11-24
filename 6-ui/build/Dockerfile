FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive \
    LC_CTYPE=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    TZ=Europe/Rome

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        software-properties-common \
        memcached \
        python-memcache \
        openstack-dashboard \
        git \
        python3-pip \
        python3-setuptools \
        nano \
        nocache \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Clona i repository necessari
RUN git clone https://opendev.org/x/python-iotronicclient.git /opt/build/python-iotronicclient
RUN git clone https://opendev.org/x/iotronic-ui.git /opt/build/iotronic-ui

# Installa python-iotronicclient
WORKDIR /opt/build/python-iotronicclient
RUN pip3 install --upgrade pip \
 && pip3 install \
       "pbr>=2.0.0" \
       "appdirs>=1.3.0" \
       "dogpile.cache>=0.6.2" \
       "jsonschema>=3.2.0" \
       "keystoneauth1>=2.18.0" \
       "osc-lib>=1.2.0" \
       "oslo.i18n>=3.15.3" \
       "oslo.serialization>=1.10.0" \
       "oslo.utils>=3.33.0" \
       "PrettyTable>=2.0.0" \
       "python-openstackclient>=3.3.0" \
       "PyYAML>=3.12" \
       "requests>=2.18.0" \
       "six>=1.11.0" \
       "pbr>=1.8" \
 && pip3 install .

# Installa iotronic-ui
WORKDIR /opt/build/iotronic-ui
RUN pip3 install \
       "Django>=2.2.24" \
       "django-compressor" \
       "oslo.config>=6.8.1" \
 && python3 setup.py install \
 && cp iotronic_ui/api/iotronic.py /usr/share/openstack-dashboard/openstack_dashboard/api/ \
 && cp iotronic_ui/enabled/_6000_iot.py /usr/share/openstack-dashboard/openstack_dashboard/enabled/ \
 && cp iotronic_ui/enabled/_6* /usr/share/openstack-dashboard/openstack_dashboard/enabled/

# Aggiungi lo script startUI
COPY bin/startUI /usr/local/bin/startUI
RUN chmod +x /usr/local/bin/startUI

VOLUME ["/etc/openstack-dashboard/"]

EXPOSE 80

CMD ["/usr/local/bin/startUI"]
