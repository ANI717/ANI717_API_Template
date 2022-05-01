# ANI717 API Template
```
uvicorn main:app --reload
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
pytest -v
pytest -cov
```
```
git init
git status
git add README.md
git commit -m "first commit"
git branch
git branch -M main
git log
git checkout -b dev
git checkout main
git merge dev
git branch -D dev
git remote add origin https://github.com/ANI717/ANI717_API_Template.git
git remote
git push -u origin main
git branch -r
git clone https://github.com/ANI717/ANI717_API_Template.git
git push
git remote rm origin
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
