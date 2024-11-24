# **Guida Completa per il Deployment di Iotronic OpenStack**

Questa guida dettagliata spiega come effettuare il deployment di Iotronic OpenStack utilizzando Docker, con la possibilità di sfruttare pacchetti esistenti di MySQL, Memcached e Keystone provenienti da un'installazione attiva di OpenStack.

---

## **Requisiti Prerequisiti**
1. Sistema operativo: **Ubuntu Bionic (18.04)** o successivi.
2. **Docker** e **Docker Compose** installati.
3. Certificati SSL per i componenti (gestiti dalla CA locale inclusa).
4. Un'installazione attiva di OpenStack con i servizi di:
   - **MySQL** (MariaDB).
   - **Memcached**.
   - **Keystone** configurato e operativo.

---

## **Passaggi per il Deployment**

### **1. Creazione del Certificato con la Root CA**
La Root CA genera i certificati per i client.

```bash
cd ~/iotronic-openstack/0-CA/
sudo ./0-CA_create iotronic
```

- Questo comando crea il certificato client per Iotronic e lo copia nella directory `/etc/ssl/iotronic/client_iotronic/`.

---

### **2. Deploy di Crossbar**
Crossbar è il bus di messaggi utilizzato da Iotronic.

```bash
cd ~/iotronic-openstack/1-iotronic-crossbar/
sudo ./1-crossbar
```

- Verifica che il container **iotronic-crossbar** sia avviato correttamente.

---

### **3. Deploy di WSTUN**
WSTUN gestisce i tunnel WebSocket per Iotronic.

```bash
cd ~/iotronic-openstack/1-iotronic-wstun/
sudo ./1-wstun
```

- Verifica che il container **iotronic-wstun** sia avviato correttamente.

---

### **4. Configurazione del Database**
Se vuoi utilizzare un database MySQL esistente da un'installazione OpenStack attiva, salta questo passaggio. Altrimenti, crea un container MariaDB dedicato:

```bash
cd ~/iotronic-openstack/2-mysql/
sudo ./2-mysql
```

- Per verificare lo stato del database:
  ```bash
  docker logs -f iotronic_db
  ```

---

### **5. Configurazione di Keystone**
Se Keystone è già configurato nell'installazione attiva di OpenStack, salta questo passaggio. Altrimenti:

1. **Deploy del Container Keystone**:
   ```bash
   cd ~/iotronic-openstack/3-keystone/
   sudo ./3-keystone
   ```

2. **Sincronizzazione e Configurazione di Keystone**:
   ```bash
   sudo ./3.5-keystone
   ```

---

### **6. Deploy del Conductor**
Il Conductor è il cuore di Iotronic.

1. **Deploy del Conductor**:
   ```bash
   cd ~/iotronic-openstack/4-conductor/
   sudo ./4-conductor
   ```

2. **Configurazione del Database per il Conductor**:
   ```bash
   sudo ./4.5-conductor
   ```

---

### **7. Deploy di WAgent**
WAgent è il componente agent-side di Iotronic.

```bash
cd ~/iotronic-openstack/5-wagent/
sudo ./5-wagent
```

---

### **8. Deploy della UI**
La UI consente di gestire Iotronic tramite un'interfaccia grafica.

```bash
cd ~/iotronic-openstack/6-ui/
sudo ./6-ui
```

- Accedi alla UI tramite il browser puntando a: `http://<hostname>`

---

## **Configurazioni Aggiuntive**
1. **MySQL**:
   - Configura i dettagli del database nel file di configurazione del Conductor (`conductor-config.env`).
   - Utilizza il servizio MySQL esistente dell'installazione OpenStack se disponibile.

2. **Memcached**:
   - Assicurati che Memcached sia in esecuzione nell'host OpenStack.

3. **Keystone**:
   - Aggiorna il file `keystone.conf` con le configurazioni corrette per i tuoi servizi.

---

## **Note Importanti**
- **Controllo dei Log**:
  Per ogni container, puoi verificare i log utilizzando:
  ```bash
  docker logs -f <container_name>
  ```

- **Persistenza**:
  Se necessario, mappa volumi persistenti per i database e i file di configurazione.

- **Risoluzione dei Problemi**:
  - Controlla che i certificati SSL siano validi.
  - Verifica la connettività tra i container.

- **Pulizia**:
  Rimuovi i container inutilizzati o interrotti per risparmiare risorse:
  ```bash
  docker system prune -f
  ```

