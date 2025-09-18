from fastapi import FastAPI

# Create a FastAPI web application instance
app = FastAPI()

# Define a simple GET endpoint at /ping
@app.get("/ping")
def ping():
    # When someone visits /ping, return JSON {"ok": True}
    return {"ok": True}