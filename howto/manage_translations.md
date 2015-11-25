# How to manage translations?

We have 3 tools to manage and publish translations of the main tutorial:
* [GitHub](https://github.com/DjangoGirls/tutorial/) for the code.
* [Crowdin](https://crowdin.com/project/django-girls-tutorial) for translating the material. You can manage translations, translators and proofreaders [here](https://crowdin.com/project/django-girls-tutorial/settings).
* [GitBook](https://www.gitbook.com/@djangogirls) to publish the tutorial online.

Volunteers will need your help on those two things:
* Be added to a existing translation team or start a new one.
* Deploy new translations.

You can contact our translations managers at this address: `translations@djangogirls.org`

## Translation teams management
 
### Invite new translator

To add someone to an existing team, send them this link: `https://crowdin.com/project/django-girls-tutorial/invite/`. Do not use the link provided by Crowdin: it won't work! If possible, send them the [Translation guide](http://translate.djangogirls.org/).

If you need to create a new language team:

1. Click on the `Target Languages` button in the `Translations` section [here](https://crowdin.com/project/django-girls-tutorial/settings#translations).
2. Click on the language you want to add and click on `update`.
3. Invite new translators with this link: `https://crowdin.com/project/django-girls-tutorial/invite/`. Don't forget to send them the [Translation guide](http://translate.djangogirls.org/).

### Translators and proofreaders role

A translator will be able to translate and vote (blue progress bar). To get a translation approved, you will need one or two persons to proofread it one last time (green process bar): their approval will freeze the translation.

To give proofreader status to someone:

1. Go in the [Translators](https://crowdin.com/project/django-girls-tutorial/settings#members) section.
2. Use the search function: we have many contributors <3
3. Double click on the person you want to make proofreader.
4. Change their role from translator to proofreader and close.
5. They should received an email saying they've be promoted to proofreader but don't hesitate to notice them on Slack or by private message in Crowdin :sparkles:.

## How to deploy a new translation?

First thing: congratulate translators and proofreaders! They made an amazing job!

There's still some work to do before a translation can be available on GitBook. You will need to check if the translation is 100% approved. If it's not the case, add proofreaders to the team and ask them to contact you again when this last part is done.

When a translation is 100% approved:

1. Send to the team the last build for their language and a file with the name of every person who contributed to their translation (see below).
2. Ask them to do the final tasks listed [here](http://translate.djangogirls.org/when_its_ready.html).
3. Review their pull request [here](https://github.com/DjangoGirls/tutorial/) and merge it when it's ready.
4. Check if the book is building on [GitBook](https://www.gitbook.com/book/djangogirls/djangogirls-tutorial/activity) and fix problem if there is any. 
5. Celebrate and ask someone from the support team to announce the new translation on Twitter! :tada:

### Build project

1. Go to the [Crowdin settings](https://crowdin.com/project/django-girls-tutorial/settings#translations) page.
2. Click on the `Build project` button.
3. After the build is done, click on the `Download` button next to the language you want to publish.


### List of contributors

1. Go to the ["Reports" tab](https://crowdin.com/project/django-girls-tutorial/settings#reports-details) in the Crowdin project settings.
2. Choose `Custom report` from the left.
3. Show the report for `Words translated` and choose the language you want.
4. Click on `Generate`. You will get a list of all contributors to your language, sorted by how much each has contributed. Yay!

## Maintaining a translation

Check on [GitHub](https://github.com/DjangoGirls/tutorial/) if there are pending pull requests linked to translation. People tends to send typo fixes after a workshop ;)

Keep translators posted if there is any major change happening in the tutorial.
