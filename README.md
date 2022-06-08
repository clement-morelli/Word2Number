# Work2Number



helm repo add argo https://argoproj.github.io/argo-helm

helm install my-release argo/argo-cd

kubectl port-forward svc/my-release-argocd-server 8080:443

kubectl get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo




kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

On your mac: brew install argocd

kubectl port-forward svc/argocd-server -n argocd 8080:443

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo

--port-forward-namespace argocd to each command

Clements-Macbook:Work2Number clement$ argocd login 127.0.0.1:8080
WARNING: server certificate had error: x509: “Argo CD” certificate is not trusted. Proceed insecurely (y/n)? y
Username: admin
Password: 
'admin:login' logged in successfully
Context '127.0.0.1:8080' updated
Clements-Macbook:Work2Number clement$ argocd account update-password
*** Enter password of currently logged in user (admin): 
*** Enter new password for user admin: 
*** Confirm new password for user admin: 
Password updated
Context '127.0.0.1:8080' updated


argocd app create word2number --repo https://github.com/clement-morelli/Work2Number.git --path word2number --dest-server https://kubernetes.default.svc --dest-namespace default


