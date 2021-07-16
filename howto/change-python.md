# Bump Python Version for DjangoGirls.org Website

In order to bump up the Python version for the DjangoGirls.org website, you 
need to have access to our PythonAnywhere account, and follow these instructions:

1. [Login to PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/). Credentials can be found in 1Password.
2. Check if the Python version you want to upgrade to is supported by the current
system image used on PythonAnywhere by clicking on the pen icon on the Web Tab or
by [reading this](https://help.pythonanywhere.com/pages/ChangingSystemImage#:~:text=Once%20you%20have%20changed%20the,again%20to%20pick%20it%20up.).
 If yes, no need to change the system image. If system image needs to be changed, follow the instructions here.
3. Check which node version we are using opening the `Bash Console` and type 
```which node```
4. Change the system image if necessary (skip this step if version is supported by
current image).
5. Navigate to the ```.virtualenvs``` folder.
6. Create a new virtual environment.
7. Navigate to the ```djangogirls.com``` folder and run ```pip install -r requirements.txt```. 
This ensures that even if when you get to run the ```deploy.sh``` script and it fails,
you still have a working virtual environment with all the packages required to run the website.
8. Copy the ```postactivate``` file from the old virtual environment's ```bin``` folder and
paste it into the ```bin``` folder of the new virtual environment. This file 
should **only be** installed only in production.
9. Go to the `Web Tab` and point the virtual environment to the new virtual environment.
10. Modify the ```deploy.sh``` script to point to the new virtual environment
by changing the value of `ENV`.
11. Install node by following [these instructions](https://help.pythonanywhere.com/pages/Node/).
12. Run ```./deploy.sh``` to check if deployment works fine.
 
You are all set! 

:tada:!

