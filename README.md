# mini-rag

a minimal implementaion of the RAG system for qustion answering


## requirements 

- python 3.8 or later


#### install python using miniconda 

1) Download and install miniconda from [here](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2)
2) Create a new enviroment using the following command:

```bash
$ conda create -n mini-rag-app python=3.8

```
3) Avtivate the enviroment "
```bash
$ conda activate mini-rag-app
```

## installation

### install the required packages

```bash
$ pip install -r requirements.txt

```
### setup you enviroment variables 

```bash
$ cp .env_copy .env
```

set your enviroment variables int the `env` file, like `GOOGLE_API_KEY` value.


### run the fastapi server 

```bash 

$ uvicorn main:app --reload --host 0.0.0.0 --port 5000

```