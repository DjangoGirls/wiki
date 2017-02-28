# List of custom management commands

## In core:

* [`add_organizer`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/add_organizer.py): can be used to add people to event. It's easier to [do it in admin](https://djangogirls.org/admin/core/event/add_organizers/).
* [`backup_postgres_to_s3.py`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/backup_postgres_to_s3.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/) to backup our database.
* [`copy_event.py`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/copy_event.py): command use to copy event to create a new one in the same city. You can also do it in admin while [triaging event requests](https://djangogirls.org/admin/organize/eventapplication/).
* [`handle_emails`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/handle_emails.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/) that will send thank you, check-in and stats request emails to organizers.
* [`new_event.py`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/new_event.py): can be used to create a new event. You can also do it in admin while [triaging event requests](https://djangogirls.org/admin/organize/eventapplication/).
* [`prepare_dispatch`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/prepare_dispatch.py): return a list of events that happened, are new or still have open registration since the previous Dispatch.
* [`sync_events_dashboard`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/sync_events_dashboard.py): sync all events in a [Trello board](https://trello.com/b/nWNEA8bf/events-calendar) to get a easy to read list of next events.
* [`update_coordinates`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/update_coordinates.py): update coordinates of event cities.

## In patreonmanager:

* [`download_csv`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/download_csv.py) and [`import_csv`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/import_csv.py): used to get a fresh list of our patreon supporters. [More info here](../howto/patreon-rewards.md).
* [`fundraising_status`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/fundraising_status.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/). Publish our patreon revenue in the "notifications" channel on Slack.
* [`listpatrons`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/listpatrons.py): list Patrons who need a reward to be sent to them.

## In story:

* [`fetch_stories`](https://github.com/DjangoGirls/djangogirls/blob/master/story/management/commands/fetch_stories.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/). Fetch Django Girls stories from our blog.
