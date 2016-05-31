# Deploy DjangoGirls.org

In order to update DjangoGirls.org website, you need to have access to our PythonAnywhere account, and follow these instructions:

1. [Login to PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/). Credentials can be found in 1Password.

2. Open bash console in PythonAnywhere

3. Type following command:

```
./deploy.sh
```

This script will download latest modifications from Django Girls website repository, install packages from `requirements.txt`, collect statics and reload the website.

:tada:!

## Git hooks

We use some git hooks to automate a few things. You can find them in the
`githooks` folder of the website repository.

### `post-merge`

This hook is run whenever you run `git pull origin master` and will notify
opbeat that new code has been deployed.

**This hook should only be installed on the server.**
