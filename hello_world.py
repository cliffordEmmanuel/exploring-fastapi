from fastapi import FastAPI, Depends

app = FastAPI()

@app.get('/')  # this a route that tells fast api the method to run when a user requests a path.
async def root():  # method declaration here!!
    return {'message':'Hello World'} # send some data to the screen