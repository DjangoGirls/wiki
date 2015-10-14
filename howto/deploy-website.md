# Deploy DjangoGirls.org

In order to update DjangoGirls.org website, you need to have access to our PythonAnywhere account, and follow these instructions:

1. [Login to PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/). Credentials can be found in Meldium.

2. Open bash console in PythonAnywhere

3. Type following commands:

```
cd /home/djangogirls/djangogirls.com
git pull origin master
workon djangogirls.com
python manage.py collectstatic
```

4. Go to [web tab in PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/webapps/)

5. Reload `djangogirls2.pythonanywhere.com`, `djangogirls.org` and `www.djangogirls.org`.

:tada:!

## Git hooks

We use some git hooks to automate a few things. You can find them in the
`githooks` folder of the website repository.

### `post-merge`

This hook is run whenever you run `git pull origin master` and will notify
opbeat that new code has been deployed.

**This hook should only be installed on the server.**
