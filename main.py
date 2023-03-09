from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def 함수이름():
  return '보낼 값'