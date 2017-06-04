# List of custom management commands

## In core:

* [`backup_postgres_to_s3.py`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/backup_postgres_to_s3.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/) to backup our database.
* [`prepare_dispatch`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/prepare_dispatch.py): return a list of events that happened, are new or still have open registration since the previous Dispatch.
* [`update_coordinates`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/update_coordinates.py): update coordinates of event cities.

## In patreonmanager:

* [`download_csv`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/download_csv.py) and [`import_csv`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/import_csv.py): used to get a fresh list of our patreon supporters. [More info here](../howto/patreon-rewards.md).
* [`fundraising_status`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/fundraising_status.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/). Publish our patreon revenue in the "notifications" channel on Slack.
* [`listpatrons`](https://github.com/DjangoGirls/djangogirls/blob/master/patreonmanager/management/commands/listpatrons.py): list Patrons who need a reward to be sent to them.

## In story:

* [`fetch_stories`](https://github.com/DjangoGirls/djangogirls/blob/master/story/management/commands/fetch_stories.py): scheduled task on [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/schedule/). Fetch Django Girls stories from our blog.
