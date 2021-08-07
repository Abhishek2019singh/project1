# ML integration with DevOps to deploy,trained and monitor Machine Learning model
One of the most tricky and time taking task in a Machine Learning project is to continuously tweak the hyper-parameters until the desired accuracy is acquired and certainly it is one of the reason that many Machine Learning projects fail and are never put into production.But with the integration of ML with DevOps it can be mended up to an extent, as using automation tools we can save lots of time taken by those taken by manual operations.

In this Article i am going to explain my MLOPS project which uses Jenkins as an Automation tool integrated with my Machine Learning model which uses mnist dataset and as per requirement can change the Architecture of model as per requirement and continuously monitors the environment for its fail-safe without user intervention.

Tools and Technologies used in this project:-

1.Git 2.GitHub 3. RHEL 8(VM) 4.Jenkins 5.Docker

Overall extract of my project:-

Creating a container image that has python3 and all the libraries required for ML model.This container will be used to launch an environment to deploy the Machine learning model.
Create a job of chain ml1,ml2,ml3, ml4, ml5,ml6 using build pipeline plugin in Jenkins.
The Job ml1 push the code to the GitHub it is pulled automatically by the Jenkins using the build triggers and is copied to root directory of RHEL 8.
The Job ml2 by looking at the code automatically starts the required container image providing the environment to deploy and train the code (In my case it will launch container containing all the pre-requisite libraries for CNN).
Job ml3 trains the model and predicts the accuracy of the model.
Job ml4 checks if the desired accuracy(In my case it is 95+) is not reached then tweaks the model to get it.
Job ml5 retrains the model an notifies the developer by sending email that the desired accuracy is reached and the best model is created.
Job ml6 is for monitoring in case the container fails due to any reason this job automatically start the container again from where the last trained model left.

![image](https://user-images.githubusercontent.com/64477686/128171523-80d1d5ec-48ed-43f3-b524-0d0ef0bccc1e.png)

This picture shows a Dockerfile and to build this into docker image following commands:
**docker build -t --name container_name:version /root/foldername/**

Pull the code from the GitHub using Poll SCM build trigger and copy it to the root directory using shell execute.


![image](https://user-images.githubusercontent.com/64477686/128600662-ed11569d-7443-4ad0-bb99-f7caade00543.png)


Code for the reference can be found in my GitHub repo:-

https://github.com/Abhishek2019singh/project1/blob/main/CNN.py






