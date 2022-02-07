from doctest import FAIL_FAST
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
  return {"msg": "Hello World"}