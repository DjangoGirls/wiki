# Bump Python Version for DjangoGirls.org Website

The Django Girls website is currently running on Python 3.10 and Node 14.17.3. 

Should there be need to bump up the Python version for the DjangoGirls.org website, you need to have access to our PythonAnywhere account, and follow these instructions:

* [Login to PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/). 
  * Credentials can be found in 1Password.

* Check if the Python version you want to upgrade to is supported by the current
system image used on PythonAnywhere. 
You can do so by clicking on the pen icon on the Web tab or by 
[reading this](https://help.pythonanywhere.com/pages/ChangingSystemImage#available-python-versions-for-system-images).
 If the version of Python is already supported by the current image, there is 
 no need to change the system image. 
 If the version is not supported by the current system image, then the system
 image needs to be upgraded. 

* Check which `node` version we are using opening the `Bash Console` and 
type this command

  ```bash
  which node
  ```

  Write down the version of `node` you get from this step and save it for later 
use. You will need to reinstall it in the new image. (Skip this if image stays the same)

* Change the system image following 
[these instructions](https://help.pythonanywhere.com/pages/ChangingSystemImage#available-python-versions-for-system-images). 
(skip this step if version is supported by current image).

* Navigate to the `.virtualenvs` folder by typing 

    ```bash
    cd .virtualenvs
    ```

## Creating a new virtualenv manually    
* Create a new virtual environment. Make sure to specify the Python version in 
the command. Replace `*` with specific version number.

    ```bash
    python3.* -m venv new-venv-name
    ```

* Activate the virtual environment.

    ```bash
    source new-venv-name/bin/activate
    ```

* Navigate to the `djangogirls.com` folder and  install requirements by 
running these commands.
 
    ```
    cd ../djangogirls.com
    pip install -r requirements.txt
    ```

    This ensures that even if when you get to run the ```deploy.sh``` script and
it fails, you still have a working virtual environment with all the required 
packages to run the website.

* Using the `File` tab, copy the contents of `postactivate` file from the old virtual environment's `bin` folder and
paste it into a new file with the same name you create in the `bin` folder 
of the new virtual environment. 
This file should **only be** installed in production.

* Install node by following 
[these instructions](https://help.pythonanywhere.com/pages/Node/) (skip if 
image stays the same).

## Creating a new virtualenv using a script
* Alternatively, all these commands are written in a script in the root folder `.upgrade_image.sh` and you can edit it with the new virtual environment name, change the path from where to copy the `postactivate` script and the destination folder to be the new virtualenv you will be creating. 

You can the run `./upgrade_image.sh` in a new bash console after changing the image. The script should take a few minutes to run and after it completes and if there are no errors, it should take care of all the steps mentioned in the `Creating a new virtualenv manually`.

## Update the web apps to point to new virtualenv
* Go to the `Web` tab and change the value of Python version to the new Python
 version and point the virtual environment to the new virtual environment for
 `djangogirls2.pythonanywhere.com`, `djangogirls.org` and `www.djangogirls.org`
  web apps.

* Navigate to `Files` tab and locate the `deploy.sh` script in the root folder
`djangogirls2`. 
Modify the `deploy.sh` script to point to the new virtual environment
by changing the value of `ENV`.

* Open a new `Bash Console` and run 

    ```bash
    ./deploy.sh
    ``` 

    to check if the deployment works fine. If it fails, some troubleshooting may 
    be required.
    
* If running `.deploy.sh` fails, you will need to manually reload the website
so the changes can be effected via the `Web` tab by clicking the `Reload` 
button.

You are all set! 

:tada:!
