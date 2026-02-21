from fastapi import FastAPI


from routes import base



# initialize the fastapi
app = FastAPI()

# get the fast api funtion 'router' form 'base' and run it 
app.include_router(base.base_router)

