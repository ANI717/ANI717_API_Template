<p align="center">
  <h1 align="center">ANI717 API Template</h1>
</p>

<p align="justify">
A Python Fast API Template for Machine Learning Applications to Receive HTTP POST Request and Respond Accordingly.
</p>

## Run the API
```
git clone https://github.com/ANI717/ANI717_API_Template.git
cd ANI717_API_Template
conda create -n api python==3.9.7 -y
conda activate api
pip install --upgrade pip
pip install .
uvicorn ani717_api_template.main:app
```
## Test the API and Generate Coverage Report (While the API is Running)
```
cd ANI717_API_Template
conda create -n test_api python==3.9.7 -y
conda activate test_api
pip install --upgrade pip
pip install fastapi requests pytest coverage pytest-cov
pytest -v
pytest --cov
```
### [Swagger UI](http://127.0.0.1:8000/docs)
### [Redoc](http://127.0.0.1:8000/redoc)
## Development
```
uvicorn main:app --reload
```
```
pytest -v
pytest --markers
pytest -v -m utils
pytest -v -m app
```
```
pip install --upgrade pip
pip install --upgrade build
python -m build
```
```
pip install pyclean
pyclean --verbose .
```
```
taskkill /f /im python.exe
```
```
conda create -n ENV_NAME python=<python_version>
conda activate ENV_NAME
conda env list
conda env remove -n ENV_NAME
```
```
pip freeze > requirements.txt
```
