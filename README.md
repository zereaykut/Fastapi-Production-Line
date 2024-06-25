# fastapi_production_line
A Rest API apllication that uses fastapi and pydantic in backend.

## Run Application
Clone the repo
```shell
git clone https://github.com/zereaykut/fastapi_production_line
cd fastapi_production_line
```

Create python environment
```shell
python -m venv env
```

Activate environment in Mac/Linux 
```shell
source env/bin/activate
```

Activate environment in Windows 
```shell
.\env\Scripts\activate
```

Install required packages
```shell
pip install -r requirements.txt
```

Run dashboard
```shell
uvicorn main:app --reload
```
Application can be accessed from http://127.0.0.1:8000

## Application Docs
Application docs can be accessed on http://127.0.0.1:8000/docs
