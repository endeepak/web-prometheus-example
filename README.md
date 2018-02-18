# web-prometheus-example

Simple web service exposing prometheus metrics for web requests. Exposes endpoints to simulate CPU and memory load

### Run

#### Using code (local)

```sh
# Ensure python 2.x and pip installed
pip install -r app/requirements.txt
python app/server.py
```

#### Using docker

```sh
docker run -p 5000:5000 -p 8000:8000 endeepak/web-prometheus-example
```

### Requests

```sh
$ curl localhost:5000
$ curl localhost:5000/load/cpu
$ curl localhost:5000/load/memory
```

### Metrics

Metrics will available in http://localhost:8000

```sh
$ curl localhost:8000
# HELP flask_request_count Flask Request Count
# TYPE flask_request_count counter
flask_request_count{endpoint="/",http_status="200",method="GET"} 678.0
```
