pipeline {
  environment {
    registry = "snir1234"
    registryCredential = 'snir1234:Snir1234!'
    dockerImage = 'python-36-centos:latest'
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git 'https://github.com/snirmusayof/Helper-Cronjobs-Controller.git'
      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build("$registry:$BUILD_NUMBER") 
        }
      }
    }
    stage('push Image') {
      steps{
        script {
          docker.withRegistry( '', $registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
  agent {
    kubernetes {
        defaultContainer 'cronjobs-controller'
        yaml '''  
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cronjobs-contoller
  namespace: cronjobs-contoller
  labels:
    app: cronjobs-contoller
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cronjobs-contoller
  template:
    metadata:
      annotations:
        configHash: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
      labels:
        app: cronjobs-contoller
    spec:
      containers:
      - name: {{ .Values.appName }}
        image: snir1234/cronjobs-contoller:1.0
        ports:
        - containerPort: 5000
