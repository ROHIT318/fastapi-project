import uvicorn
from app.app import fast_api

if __name__ == "__main__":
    uvicorn.run("app.app:fast_api", host="0.0.0.0", port=8000, reload=True)