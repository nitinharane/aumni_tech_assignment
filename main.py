import uvicorn as uvicorn
from endpoints.sports_inventory import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)

