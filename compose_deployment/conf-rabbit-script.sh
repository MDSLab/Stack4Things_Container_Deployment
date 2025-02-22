#!/bin/bash

# Avvia RabbitMQ in background
rabbitmq-server &  

# Attendi che RabbitMQ sia pronto
sleep 30  

# Aggiungi l'utente OpenStack
rabbitmqctl add_user openstack unime || echo "Utente già esistente"
echo "USER openstack added"

# Attendi di nuovo per sicurezza
sleep 10  

# Imposta i permessi
rabbitmqctl set_permissions openstack ".*" ".*" ".*"
rabbitmqctl set_permissions -p / openstack ".*" ".*" ".*"

# Mantieni il container attivo
wait
