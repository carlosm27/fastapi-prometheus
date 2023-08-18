from fastapi import FastAPI

app = FastAPI()

from prometheus_client import make_asgi_app, CollectorRegistry, multiprocess

app = FastAPI(debug=False)

# Using multiprocess collector for registry


metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/")
def index():
  
   
    return "Hello, world!"
  

