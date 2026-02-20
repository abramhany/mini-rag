from fastapi import FastAPI

app = FastAPI()



# uvicorn main:app --reload --host 0.0.0.0 --port 5000
# use this command to start an web and to update every time you change the code --host all you to host it 0.0.0.0 allows all to enter --port 5000 is the number of the port you are using 
@app.get('/welcome')
def hello():
    return {
        'message':'Hello there!'
    }
