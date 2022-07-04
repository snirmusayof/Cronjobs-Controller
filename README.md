# Outer Service Architecture



![image](https://user-images.githubusercontent.com/63164964/177109901-6767dd31-6f94-403b-98db-dd94f3fd4bb1.png)



### Helper Cronjobs Manager

* Script that run all 3 min, deployed on the helper VM, fetches files from a fixed remote server and saves them to in path /var/Cloudlet-Otuer-Service to scripts and a cronjobs /var/cron.d
* Deployed as a container.
* THe container will be deployed as part a pre-hook workflow (Ansible)
* Deployed with deploy-helper-services playbook.


### Helper Cronjobs Controller

* An HTTP server exporting files (tests and cronjobs), which is deployed on the OpenShift cluster.
* A big benefit of this architecture, is that it is GitOps  oriented, and when files are added ot changed in git (To helper-Cronjobs-Controller tests and cronjobs directories), the pod restart and the new files are in the pod.

### Upating process

* Adding tests to repo Helper-Cronjobs-controller.
* To do commit to branch main.
* Run ci that build image with a tests
* Change version in hekm repo to Helper-Cronjobs-controller in Values file.
* To do snyc in Argo app.



