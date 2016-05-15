# Add additional organizer to an existing event

So you want to add a new organizer to an existing event without much hassle.

## Instructions

1. Login to PythonAnywhere, go into bash
2. `workon djangogirls.com`
3. `cd djangogirls.com`
4. `python manage.py add_organizer`
5. Pass the ID of event (event, not eventpage!), name and email
6. This will add organizer to the website, print you login credentials, and automatically invite to Slack.
7. Add to django-girls-organizers mailing list: https://groups.google.com/forum/#!managemembers/django-girls-organizers/add
8. Send them an [email](../howto/emails/add_organizer.md)

Example welcome message:
> This is a private group for Django Girls organizers only. We plan to use it to exchange ideas, help each other and share knowledge :smile: Please, use this list for all your questions or concerns.
