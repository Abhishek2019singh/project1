# ML integration with DevOps to deploy,trained and monitor Machine Learning model
One of the most tricky and time taking task in a Machine Learning project is to continuously tweak the hyper-parameters until the desired accuracy is acquired and certainly it is one of the reason that many Machine Learning projects fail and are never put into production.But with the integration of ML with DevOps it can be mended up to an extent, as using automation tools we can save lots of time taken by those taken by manual operations.

In this Article i am going to explain my MLOPS project which uses Jenkins as an Automation tool integrated with my Machine Learning model which uses mnist dataset and as per requirement can change the Architecture of model as per requirement and continuously monitors the environment for its fail-safe without user intervention.

Tools and Technologies used in this project:-

1.Git 2.GitHub 3. RHEL 8(VM) 4.Jenkins 5.Docker

Overall extract of my project:-

1. Creating a container image that has python3 and all the libraries required for ML model.This container will be used to launch an environment to deploy the Machine learning model.
2. Create a job of chain project1_step1, project1_step2, project1_step3, project1_step4, project1_step5 and project1_step6 using build pipeline plugin in Jenkins.
3. The Job project1_step1 push the code to the GitHub it is pulled automatically by the Jenkins using the build triggers and is copied to root directory of RHEL 8.
4. The Job project1_step2 by looking at the code automatically starts the required container image providing the environment to deploy and train the code (In my case it will launch container containing all the pre-requisite libraries for CNN).
5. Job project1_step3 trains the model and predicts the accuracy of the model.
6. Job project1_step4 checks if the desired accuracy(In my case it is 95+) is not reached then tweaks the model to get it.
7. Job project1_step5 retrains the model an notifies the developer by sending email that the desired accuracy is reached and the best model is created.
8. Job project1_step6 is for monitoring in case the container fails due to any reason this job automatically start the container again from where the last trained model left.

![image](https://user-images.githubusercontent.com/64477686/128171523-80d1d5ec-48ed-43f3-b524-0d0ef0bccc1e.png)

This picture shows a Dockerfile and to build this into docker image following commands:
**docker build -t --name container_name:version /root/foldername/**

Pull the code from the GitHub using Poll SCM build trigger and copy it to the root directory using shell execute.

![Screenshot (190)](https://user-images.githubusercontent.com/64477686/132841040-ed50e8d4-683b-4083-ac5c-a212edd03209.png)

![Screenshot (193)](https://user-images.githubusercontent.com/64477686/132846717-f0a3edaa-2e48-477e-b92b-f1953db37d94.png)

![Screenshot (194)](https://user-images.githubusercontent.com/64477686/132846926-5daf6302-ffb9-489d-83b4-17066dc72d44.png)

![Screenshot (195)](https://user-images.githubusercontent.com/64477686/132846955-8b9d3e7d-7415-4359-aca4-d7572d84a3a9.png)

The Job project1_step2 by looking at the code automatically starts the required container image providing the environment to deploy and train the code (In my case it will launch container containing all the pre-requisite libraries for CNN).

![Screenshot (196)](https://user-images.githubusercontent.com/64477686/132847453-d2c43d87-7385-4fac-860e-03e47ea11fbc.png)

![Screenshot (197)](https://user-images.githubusercontent.com/64477686/132847473-f13294d5-a06e-4fa1-9a69-c400a03b1e5d.png)

![Screenshot (198)](https://user-images.githubusercontent.com/64477686/132848250-38db0b16-7a81-4a85-9bbf-0704c1b5de7c.png)










Code for the reference can be found in my GitHub repo:-

https://github.com/Abhishek2019singh/project1/blob/main/CNN.py






