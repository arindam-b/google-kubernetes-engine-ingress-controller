# Dockerize

docker build -t arindambanerjee/weatherapp:v1 app-weather/

docker build -t arindambanerjee/cityguide:v1 app-cityguide/

# Create a namespace for your ingress resources
kubectl create namespace ingress-basic

or 

kubectl apply -f namespace.yml

# Deploy applications

kubectl apply -f deploy-weatherapp.yml

kubectl apply -f deploy-cityguideapp.yml

# Create an ingress route

kubectl apply -f ingress.yml

#Tear down

kubectl delete ns ingress-basic


# Important Lessons Learnt

When you define ingress, it is must you keep following things:

1. For each service, keep one default endpoint: "/" and one with context path.
   For example, here we have 2 services:
   weatherapp	: default endpoint - "/" 
				  contenxt path - "/weather" 
   cityguideapp	: default endpoint - "/"
				  contenxt path - "/cityguide"
   It's because ingress is a L7 load balancer, so it does internal health checking and path is "/"
   So if the path does not exists, it fails.
   
2. In Spring Boot application which often set context-path which hardcodes the path. Hence "/" does not satified, unless you keep it for default path.
   So it fails. So don't put context-path in spring-boot if you want to use it for ingress.