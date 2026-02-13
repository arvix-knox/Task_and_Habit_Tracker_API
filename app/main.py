from fastapi import FastAPI

app = FastAPI(title="Task Manager Team API", version="0.0.1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
