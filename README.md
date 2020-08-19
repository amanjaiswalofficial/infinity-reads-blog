# infinity-reads-blog

### To Run Application

Steps To Follow:

#### Docker-Compose Instructions
To setup and run in detached mode before launching application:

```docker-compose up -d```

To connect with Mongo_DB from terminal(Optional)

Username: 'user'
Password: 'password'
Connection Database: 'blog_db'

```mongo -u user -p 'password' --authenticationDatabase flask_db```

#### create virtual environment

```virtualenv blog_env -p python3.7```

#### Activate the environment

```source blog_env/bin/activate```

#### Install all the dependency in blog_env
```pip install -r requirements.txt```


#### Run the Application
To run the application:
```python run.py```