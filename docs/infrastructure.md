# Infrastructure

Package file: `packages/infrastructure.yaml`

---

## `docker`

Docker CE.

### Description
`docker` is the platform for developing, shipping, and running applications in containers. It packages apps with dependencies into portable images.

### Usage
```bash
# Run a container
docker run -it ubuntu bash

# Build an image from a Dockerfile
docker build -t myapp .

# List containers
docker ps -a

# List images
docker images

# Stop a container
docker stop container_id

# Remove a container
docker rm container_id

# Docker Compose (v2)
docker compose up -d
```

---

## `docker-compose`

Docker Compose v2.

### Description
`docker-compose` (built into Docker as `docker compose`) defines and runs multi-container applications with a YAML configuration file.

### Usage
```bash
# Start services in background
docker compose up -d

# View logs
docker compose logs -f

# Scale a service
docker compose up -d --scale web=3

# Stop and remove containers
docker compose down

# Build images before starting
docker compose up --build
```

---

## `terraform`

Infrastructure as code.

### Description
`terraform` is a tool for building, changing, and versioning infrastructure safely and efficiently. It supports AWS, Azure, GCP, Kubernetes, and hundreds of other providers.

### Usage
```bash
# Initialize a project
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy

# Format code
terraform fmt

# Validate configuration
terraform validate
```

---

## `minikube`

Local K8s.

### Description
`minikube` runs a single-node Kubernetes cluster locally inside a VM or container. It is ideal for development and testing Kubernetes workloads.

### Usage
```bash
# Start a cluster
minikube start

# Check status
minikube status

# Open the Kubernetes dashboard
minikube dashboard

# Point kubectl to minikube
kubectl config use-context minikube

# Stop the cluster
minikube stop

# Delete the cluster
minikube delete
```

---

## `kubectl`

Kubernetes CLI.

### Description
`kubectl` is the command-line tool for interacting with Kubernetes clusters. It manages pods, deployments, services, config maps, and more.

### Usage
```bash
# View cluster info
kubectl cluster-info

# List pods
kubectl get pods

# View pod logs
kubectl logs my-pod

# Execute a command in a pod
kubectl exec -it my-pod -- /bin/sh

# Apply a manifest
kubectl apply -f deployment.yaml

# Scale a deployment
kubectl scale deployment myapp --replicas=3

# Port forward
kubectl port-forward svc/myapp 8080:80
```

---

## `helm`

Helm package manager.

### Description
`helm` is the package manager for Kubernetes. It uses charts (predefined templates) to define, install, and upgrade complex applications on a cluster.

### Usage
```bash
# Add a chart repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Search for charts
helm search repo nginx

# Install a chart
helm install my-nginx bitnami/nginx

# List releases
helm list

# Upgrade a release
helm upgrade my-nginx bitnami/nginx

# Remove a release
helm uninstall my-nginx
```

---

## `gcloud`

Google Cloud SDK.

### Description
`gcloud` is the CLI for Google Cloud Platform. It manages GCP resources including Compute Engine, Cloud Storage, Cloud Run, and IAM.

### Usage
```bash
# Authenticate
gcloud auth login

# Set project
gcloud config set project my-project-id

# List Compute instances
gcloud compute instances list

# Deploy to Cloud Run
gcloud run deploy my-service --source .

# List buckets
gsutil ls
```

---

## `aws-cli`

AWS CLI v2.

### Description
`aws` is the unified command-line tool for managing Amazon Web Services. It covers EC2, S3, Lambda, IAM, CloudFormation, and 200+ other services.

### Usage
```bash
# Configure credentials
aws configure

# List S3 buckets
aws s3 ls

# EC2 instances
aws ec2 describe-instances

# Invoke a Lambda
aws lambda invoke --function-name myFunction output.json

# CloudFormation deploy
aws cloudformation deploy --template-file template.yaml --stack-name mystack
```

---

## `azure-cli`

Azure CLI.

### Description
`az` is the official CLI for Microsoft Azure. It provides commands for managing VMs, AKS, storage, databases, and Azure Active Directory.

### Usage
```bash
# Login
az login

# Set subscription
az account set --subscription "My Subscription"

# List resource groups
az group list

# Create a VM
az vm create --resource-group myRG --name myVM --image Ubuntu2204

# List AKS clusters
az aks list
```

---

## `oci-cli`

Oracle Cloud CLI.

### Description
`oci` is the command-line interface for Oracle Cloud Infrastructure. It manages compute instances, databases, networking, and identity resources in OCI.

### Usage
```bash
# Configure
oci setup config

# List compute instances
oci compute instance list --compartment-id ocid1.compartment.oc1..xxx

# List buckets
os ns get
oci os bucket list --namespace-name mynamespace
```

---

## `zoho-cli`

Zoho CRM CLI.

### Description
`zohocli` provides command-line access to Zoho CRM APIs for managing leads, contacts, deals, and custom modules.

### Usage
```bash
# Authenticate
zoho auth login

# List leads
zoho crm leads list

# Get a record
zoho crm leads get --id 123456789

# Create a lead
zoho crm leads create --data '{"Last_Name":"Doe","First_Name":"John"}'
```
