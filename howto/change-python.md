# Bump Python Version for DjangoGirls.org Website

In order to bump up the Python version for the DjangoGirls.org website, you 
need to have access to our PythonAnywhere account, and follow these instructions:

[Login to PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/). 
* Credentials can be found in 1Password.

* Check if the Python version you want to upgrade to is supported by the current
system image used on PythonAnywhere. 
You can do so by clicking on the pen icon on the Web Tab or by 
[reading this](https://help.pythonanywhere.com/pages/ChangingSystemImage#available-python-versions-for-system-images).
 If the version of Python is already supported by the current image, there is 
 no need to change the system image. 
 If the version is not supported by the current system image, then the system
 image needs to be upgraded. 

* Check which `node` version we are using opening the `Bash Console` and 
type this command

  ```which node```

  Write down the version of `node` you get from this step and save it for later 
use. You will need to reinstall it in the new image. (Skip this if image stays the same)

* Change the system image following 
[these instructions](https://help.pythonanywhere.com/pages/ChangingSystemImage#available-python-versions-for-system-images). 
(skip this step if version is supported by current image).

* Navigate to the `.virtualenvs` folder by typing 

    ```cd .virtualenvs```
    
* Create a new virtual environment. Make sure to specify the Python version in 
the command. Replace `*` with specific version number.

    ```python3.* -m venv new-venv-name```

* Activate the virtual environment.

    ```source new-venv-name/bin/activate```

* Navigate to the `djangogirls.com` folder and  install requirements by 
running these commands.
 
    ```
    cd ..
    cd djangogirls.com
    pip install -r requirements.txt
    ```

    This ensures that even if when you get to run the ```deploy.sh``` script and
it fails, you still have a working virtual environment with all the required 
packages to run the website.

* Using the `File` tab, copy the contents of `postactivate` file from the old virtual environment's `bin` folder and
paste it into a new file with the same name you create in the `bin` folder 
of the new virtual environment. 
This file should **only be** installed in production.

* Go to the `Web Tab` and point the virtual environment to the new virtual environment.

* Navigate to `Files` tab and locate the `deploy.sh` script in the root folder
`djangogirls2`. 
Modify the `deploy.sh` script to point to the new virtual environment
by changing the value of `ENV`.

* Install node by following 
[these instructions](https://help.pythonanywhere.com/pages/Node/).

* Open a new `Bash Console` and run 

    ```./deploy.sh``` 

    to check if the deployment works fine. If not, some troubleshooting may 
    be required.


You are all set! 

:tada:!

