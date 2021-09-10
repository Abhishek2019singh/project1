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



![Screenshot (193)](https://user-images.githubusercontent.com/64477686/132846717-f0a3edaa-2e48-477e-b92b-f1953db37d94.png)

![Screenshot (194)](https://user-images.githubusercontent.com/64477686/132846926-5daf6302-ffb9-489d-83b4-17066dc72d44.png)

![Screenshot (195)](https://user-images.githubusercontent.com/64477686/132846955-8b9d3e7d-7415-4359-aca4-d7572d84a3a9.png)



The Job project1_step2 by looking at the code automatically starts the required container image providing the environment to deploy and train the code (In my case it will launch container containing all the pre-requisite libraries for CNN).



![Screenshot (196)](https://user-images.githubusercontent.com/64477686/132847453-d2c43d87-7385-4fac-860e-03e47ea11fbc.png)

![Screenshot (197)](https://user-images.githubusercontent.com/64477686/132847473-f13294d5-a06e-4fa1-9a69-c400a03b1e5d.png)

![Screenshot (198)](https://user-images.githubusercontent.com/64477686/132848250-38db0b16-7a81-4a85-9bbf-0704c1b5de7c.png)



Job project1_step3 trains the model and predicts the accuracy of the model.

Code for the reference can be found in my GitHub repo:-

https://github.com/Abhishek2019singh/project1/blob/main/CNN.py




![Screenshot (201)](https://user-images.githubusercontent.com/64477686/132848863-2f67d0d1-e1ce-42e8-b2fa-ea3cd5b29f6c.png)

![Screenshot (202)](https://user-images.githubusercontent.com/64477686/132848882-f781094b-2979-4072-b537-d5d2e7168a43.png)



Here data.txt file stores accuracy of the model which will be used to compare with the desired accuracy and further actions will be taken.



![Screenshot (214)](https://user-images.githubusercontent.com/64477686/132850209-04e021a7-cc13-4244-8836-42e216433f47.png)



Job project1_step4 checks if the desired accuracy(In my case it is 95+) is reached or not then tweaks the model to get it.



![Screenshot (204)](https://user-images.githubusercontent.com/64477686/132852324-6cbbe187-d129-435c-9e8b-1cac1c382e39.png)

![Screenshot (205)](https://user-images.githubusercontent.com/64477686/132852344-cefab1f4-4d5b-4cb1-941c-70aee63076c8.png)



Here i have used various Linux commands to compare the accuracy and tweak the model as per requirement it can be done by python code but to make it simple i had used Linux commands instead.



Job project1_step5 retrains the model an notifies the developer by sending email that the desired accuracy is reached and the best model is created.




![Screenshot (207)](https://user-images.githubusercontent.com/64477686/132852660-256d1817-b41d-4bcf-97ca-ce690e7977fc.png)

![Screenshot (209)](https://user-images.githubusercontent.com/64477686/132852669-e926a223-d807-45d1-a699-0b15998b43c6.png)

![Screenshot (213)](https://user-images.githubusercontent.com/64477686/132852722-993cc82d-0230-459e-9b53-56c7e2fd6408.png)




For sending mail i have used python code and the received mail after best trained model for reference is attached below:-




![image](https://user-images.githubusercontent.com/64477686/132852843-f7be1d6a-bff8-4f15-a7ea-42964dd77c88.png)

![Screenshot (215)](https://user-images.githubusercontent.com/64477686/132853430-0fae088c-968a-4645-922f-0a83819cafc2.png)




Job project_step6 is for monitoring in case the container fails due to any reason this job automatically start the container again from where the last trained model left.




![Screenshot (211)](https://user-images.githubusercontent.com/64477686/132853541-12f75bb0-8cbd-460b-8287-a2b254ff485e.png)




I have used build periodically trigger to monitor the environment for any fail-safe which checks it every minute and in case of failure starts the container automatically.




![Screenshot (212)](https://user-images.githubusercontent.com/64477686/132853561-666e67f7-bad8-4dd2-9c95-5aabb092154e.png)




At last the complete build pipeline view of my project :


![Screenshot (190)](https://user-images.githubusercontent.com/64477686/132853655-af512052-3cb3-4ee6-9b37-dc09622a0a27.png)



