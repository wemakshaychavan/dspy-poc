from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"hello":"World how are you"}
