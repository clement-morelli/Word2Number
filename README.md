# Word2Number service

It's an application in Python3  which transform a word into a number following these instructions:

- The number will be the concatenation of the position of each letter of the word in the Latin alphabet.
    
- The transformation is non-case sensitive
    
- A number is transformed into himself
    
- Any space or special character will be skipped.
    
 The history of the calls is stored in a PostgreSQL Database

This small application, is deploy on a local Kubernetes cluster.


## Prerequisites

- install Docker to create images : https://docs.docker.com/desktop/mac/install/
- install Minikube : https://kubernetes.io/fr/docs/tasks/tools/install-minikube/
- install virtualBox : https://www.virtualbox.org/wiki/Downloads
- install dbeaver : https://dbeaver.io/download/
- install argoCD : brew install argocd

## Create docker image
- docker build -t word2number-restapi .
- docker tag word2number-restapi clementmorellidocker/word2number:word2number_restapi
- docker push clementmorellidocker/word2number:word2number_restapi

For this application the Docker images is on the docker hub (docker.io/clementmorellidocker/word2number:word2number_restapi) and the source code is on this Github repository.


## Start the kube

- minikube start --driver=virtualbox

## Install argocd 

- kubectl create namespace argocd

- kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

- To access argued without port-forwarding :
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'

- This command give us the url to access argocd web interface:
minikube service argocd-server -n argocd --url

- This secret will be use in the next step :  
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

- Login with the username admin and the password to set up the context (the ip and the port are find to step before) : 
argocd login "ip:port"

- argocd account update-password

Now we can create the 2 applications: 
- argocd app create word2number --repo https://github.com/clement-morelli/Word2Number.git --path word2number --dest-server https://kubernetes.default.svc --dest-namespace default

- argocd app create postgresql --repo https://github.com/clement-morelli/Word2Number.git --path postgresql --dest-server https://kubernetes.default.svc --dest-namespace default

- To deploy and automated the sync of your apps you can run : 
argocd app set postgresql --sync-policy automated
argocd app set word2number --sync-policy automated

On the web interface you can see 2 apps deployed.

## Expose the service on port 80 with an nginx

First you need to enabled nains on your Kubernetes with :
- minikube addons enable ingress

Second you need to apply the expose-service.yaml with :
- argocd app create nginx-ingress --repo https://github.com/clement-morelli/Word2Number.git --path nginx --dest-server https://kubernetes.default.svc --dest-namespace default
- argocd app set nginx-ingress --sync-policy automated



## Use the Word2Number service
```
## Manual test of the API 
You can use your terminal with a curl or a web browser.
To have the ip address you can use : kubectl cluster-info
After that just try "/status" or /whatyouwant like this:
	http://ipadd/status or curl ipadd/status
	http://ipadd/chsb or curl ipadd/chsb

## Test the API with the script
I have write a little script to test the api:
- pip install requests
- kubectl cluster-info (to have the ip address)
- python3 code_testing.py ip address

## Access to the db and see the contains
For this part you can run the soft dbeaver and add a new db with :

postgreshost and postgresport: use minikube service postgres --url
postgresdb: call_db
postgresuser: clement
postgrespassword: 12345

Now you can see the table with all calls informations of the api.
```
