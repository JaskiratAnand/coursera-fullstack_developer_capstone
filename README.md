# Full Stack Application Development Capstone Project

This project was built as the final submission for the IBM Full Stack Web Development Professional Certificate program on Coursera. It demonstrates the skills and knowledge acquired throughout the 12-course series, focusing on front-end, back-end, databases, and deployment.

### Certificate Link
https://www.coursera.org/account/accomplishments/verify/Q0W7A5MTEENF

## Project Overview
The Capstone Project is a full-stack application that combines various technologies and best practices learned throughout the course. This project is a Car Dealership website build end-to-end. The user can view multiple dealerships, filter them as per their state, view reviews on the dealerships and post their own reviews.

This application showcases my skills in front-end and back-end development, database design, and deployment strategies, which were central themes in the course series.

### Features
* User Authentication: Secure login and registration functionality.
* CRUD Operations: Create, Read, Update, and Delete from the database.
* Data Persistence: Uses a robust database to store and retrieve information.

### Tech Stack
* Frontend: React.js, Django, Javascript, Python
* Backend: Python (Django), Node.js, Express
* Database: MongoDB, SQLite
* Version Control: Git, GitHub
* Containerization: Docker, Kubernetes
* CI/CD: Git Worrflows
* Deployment: IBMCloud

## Installation

### In Development 
* Clone the Repository
  ```bash
  git clone https://github.com/JaskiratAnand/coursera-fullstack_developer_capstone.git
  ```
* build frontend
  ```bash
  cd coursera-fullstack_developer_capstone/server/frontend
  npm install
  npm run build
  ```
* Build & Run the backend in Docker
  ```bash
  cd coursera-fullstack_developer_capstone/server/database

  docker build . -t nodeapp
  docker-compose up
  ```
* Update .env file in djangoapp
* activate djangoenv & install dependencies
  ```bash
  cd coursera-fullstack_developer_capstone/server
  pip install virtualenv
  virtualenv djangoenv
  source djangoenv/bin/activate

  python3 -m pip install -U -r requirements.txt
  ```
* Migrate models & database
  ```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py collectstatic
  ```
* Run django server
  ```bash
  python3 manage.py run server
  ```

### In Docker/Kubernetes Cluster

* Create Docker Image
  ```bash
  cd coursera-fullstack_developer_capstone/server

  docker build -t dealershipApp
  ```
* Change `image:` to your docker image tag
* Create Kubernetes deployment
  ```bash
  kubectl apply -f deployment.yaml
  ``` 
* Set port-forwarding
  ```bash
  kubectl port-forward deployment.apps/dealership 8000:8000
  ```
  
## Screenshots

* Home Page
  ![deployed_loggedin](https://github.com/user-attachments/assets/42a70803-6fb0-4b7d-b3b9-5b7e90091503)

* Dealers List
  ![deployed_dealer_detail](https://github.com/user-attachments/assets/906a1016-2317-43a7-abc7-c6f1609c4f14)

* Dealer Reviews
  ![deployed_add_review](https://github.com/user-attachments/assets/6017a253-4883-4547-b404-fb9e93543e65)

* Write Reviews
  ![dealership_review_submission](https://github.com/user-attachments/assets/5f3e40a1-5340-4fc6-ab39-864a40a5cfb1)
