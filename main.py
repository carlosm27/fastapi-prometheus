from fastapi import FastAPI
from prometheus_client import make_asgi_app, Counter

app = FastAPI()
index_counter = Counter('index_counter', 'Description of counter')

all_requests = Counter('all_requests', 'A counter of the all requests made')
all_requests.inc()

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/")

def index():
    index_counter.inc()
    
    
    return "Hello, world!"
  

