# Item Catalog Application - Cuisine Recipe Application
#### Description:
This project is part of the Udacity Full Stack Nanodegree program which demonstrates the development of modern web applications. It consists of developing a RESTful web application using the Python Flask framework and a persistent data storage along with third party OAuth authentication. It demonstrates the core features of a secured web application - CRUD (Create, Read, Update, Delete). 

### Prerequistes:
Following are the prerequistes to run this project. Please click on the link for the instructions on how to install the various components:
  - [Python2](https://www.python.org/downloads/)
  - [Vagrant](https://www.vagrantup.com/docs/installation/)
  - [Virtual Box](https://www.virtualbox.org/)

### Project Setup:
1. Install Vagrant and Virtual Box from the links above.
2. Download the data for this project [here](https://github.com/udacity/fullstack-nanodegree-vm).
3. Clone this repository into the Cuisine-Recipe-App.
4. On your favorite terminal, go to the following path:
`cd /Cuisine-Recipe-App/fullstack-nanodegree-vm/vagrant`
5. After the above step, you may have to launch your VM.

### Launching the VM:
- Using the following command launch the Vagrant VM inside the Vagrant sub-folder which was downloaded from the [repository](https://github.com/udacity/fullstack-nanodegree-vm): 
     `$ vagrant up`
- To log in the VM:
     `$ vagrant ssh`
- cd /vagrant/ 
- To run the project type the following command:
`python finalProject.py`
- Go to `localhost:5000/login` to access the application.
- You may either use your Google Plus or your Facebook account to perform various operations on the website.

### JSON Endpoints:
- Cuisine JSON: /cuisines/JSON
- Recipe JSON: /cuisine/<int:cuisine_id>/recipe/JSON
- Cuisine Recipe JSON: /cuisine/<int:cuisine_id>/recipe/<int:recipe_id>/JSON

### Skills Learnt:
- Python
- HTML
- CSS
- Javascript
- AJAX
- Bootstrap framework
- Flask framework
- Jinja2
- SQLAlchemy
- OAuth for Google & Facebook Login

