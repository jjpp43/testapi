from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/quote")
async def say_quote():
    return {"message": "Success is falling 9 times and getting up 10 times."}
