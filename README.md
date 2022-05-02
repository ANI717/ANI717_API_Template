# ANI717 API Template
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
```
docker image build -t my-first-api .
docker run -p 5000:5000 -d my-first-api
```
```
minikube delete
minikube start --driver=docker

kubectl apply -f k8s.yaml
minikube start service: test-api-service

minikube dashboard
kubectl get deploy
kubectl delete deploy test-api-app
kubectl get svc
kubectl delete svc test-api-service
```
