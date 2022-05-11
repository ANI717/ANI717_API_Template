<p align="center">
  <h1 align="center">ANI717 API Template</h1>
</p>

<p align="justify">
A Python Fast API Template for Machine Learning Applications to Receive HTTP POST Request and Respond Accordingly.
</p>

## Clone the Repo and Install Dependencies
Python Required >= 3.9.7
```
git clone https://github.com/ANI717/ANI717_API_Template.git
cd ANI717_API_Template
pip install --upgrade pip
pip install .
```
## Run the API
```
uvicorn ani717_api_template.main:app
```
#### [Swagger UI](http://127.0.0.1:8000/docs)</br>
#### [Redoc](http://127.0.0.1:8000/redoc)</br>
## Test the API
```
pytest -v
```
## Generate Coverage Report
```
pytest --cov
```