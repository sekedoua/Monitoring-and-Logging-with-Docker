## **Project overview**
 *  Set up monitoring and logging for Docker containers using Prometheus, Grafana, and the ELK stack (Elasticsearch, Logstash, Kibana)
 ### **Final Outcome**
✅ Real-time monitoring of container metrics with Prometheus & Grafana
✅ Centralized logging using ELK stack (Elasticsearch, Logstash, Kibana)
✅ Hands-on experience with observability tools in Docker environments

![ELK](/img/2025-03-26010513.png)
![ELK](/img/2025-03-26010625.png)

## **Prerequisites**

* Python  3.13.1 (Flask 3.1.0) 
* Docker version 27.5.1

## **Project Structure**

```bash
Monitoring-and-Logging-with-Docker/
├── app.py #   Flask  app
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml #  
├── logstash.conf #  
├── requirements.txt # Dependencies 
```
## **TODO**

### **Clone the repo and just run the services**
```bash
git clone  https://github.com/sekedoua/Monitoring-and-Logging-with-Docker.git
cd Monitoring-and-Logging-with-Docker
docker-compose up --build
```
 
```bash
Access the Monitoring & Logging Dashboards : 
 Flask App: http://localhost:5000
 Prometheus UI: http://localhost:9090
 Grafana UI: http://localhost:3000
 Kibana UI: http://localhost:5601
```
```bash
Visualize Logs & Metrics
	Grafana:
		o Add Prometheus as a data source.
		o Create dashboards for container metrics.
	Kibana:
		o View logs stored in Elasticsearch.
		o Create visualizations for container logs.
```

### ** Flask app (app.py) : a simple Flask or Node.js application that logs messages.**
```bash
from flask import Flask
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home route accessed")
    return "Monitoring Docker App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### ** simple requirements.txt :   **
```bash
Flask==3.1.0
prometheus-client
```

### ** Basic Dockerfile **
```bash
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### **Set Up docker-compose.yml with Prometheus, Grafana, and ELK Stack**
```bash
 version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"

  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.10.1
    environment:
      - discovery.type=single-node
    ports:
      - "9200:9200"

  logstash:
    image: docker.elastic.co/logstash/logstash:7.10.1
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:7.10.1
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

```

### ** prometheus.yml : Prometheus config for Monitoring  **
```bash
	global:
	  scrape_interval: 15s

	scrape_configs:
	  - job_name: 'docker-metrics'
		static_configs:
		  - targets: ['web:5000']
```

### ** Configure Logstash for Logging  **
```bash
input 	{
		  file 	{
					path => "/var/log/app.log"
					start_position => "beginning"
				}
		}

output 	{
  elasticsearch {
					hosts => ["elasticsearch:9200"]
					index => "docker-logs"
				}
		}
```
