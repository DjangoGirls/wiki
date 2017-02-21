# Automated emails to organizers

[`handle_emails`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/handle_emails.py) management command is scheduled in [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/) to run hourly. It will send different emails to organizers:

- Thank you emails to events that happened during the weekend.
- A friendly reminder to add applicants and attendees stats when organizers forget to do it.
- "Asking for help" emails to events that don't have a website configured or open applications. A list of contacted events will be sent to hello@djangogirls.org. If they have no website and you don't receive news from those organizers in a week, consider their event cancelled and remove it for our event list.
