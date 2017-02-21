# Copy an event

These are instructions on what to do when organizers from some city want to organize a second (or third, or fourth) edition.

## Instructions

1. Go to http://djangogirls.org/admin/core/event/
2. Find the last event in this city. It's important that this is the last (most recent) event in the city, not any other. Note the ID of the event (you can see it in URL of the event).
3. Go to PythonAnywhere, login, and open bash. Then type following commands:
```
$ workon djangogirls.com
$ cd djangogirls.com
$ python manage.py copy_event
```
4. Answer questions:

> First, give me the ID of the Event object we're gonna copy. Don't mix it up with EventPage object. If there is more than one event in this city already, give me ID of the latest one: **[ENTER ID FROM POINT 2 HERE]**
What is the number of the event in this city? If this is a second event, write 2. If third, then 3. You got it: **[ENTER NUMBER OF THE EVENT]**
What is the date of this new event? (Format: DD/MM/YYYY or MM/YYYY): **[ENTER DATE]**

> OK! That's it. Now I'll copy your event.
Website is ready here: http://djangogirls.org/berlin
Congrats on yet another event!

5. Contact the organizers using this [email template](../howto/emails/copy_event.md).

:tada:!

## If you're copying a one year old event

1. Copy the previous event
2. [Add organizer](../howto/add-organizer.md) if necessary
3. Check if the event has a dedicated email account ([nameofthecity]@djangogirls.org) and add it to the [event](https://djangogirls.org/admin/core/event/) if it's missing.
4. Use this [email template](../howto/emails/copy_year_old_event.md) and send it to the team <3

## Instructions if the whole team is changing

First, change the previous event:

1. Go to [PythonAnywhere](http://pythonanywhere.com/) and copy the previous event to create a new one.
2. Go to [Google Apps admin](http://admin.google.com/).
3. Search and select the email account you want to edit.
4. Rename it in [CityMonthYear]@djangogirls.org, where month and year are the previous event date. For example, if the last event in Paris took place in April 2015, the email account will become: paris042015@djangogirls.org
5. On the same page, go in `Account` and remove the alias [city]@djangogirls.org that was automatically created. Don't forget to save this modification.
6. Go in [Django Girls admin](http://djangogirls.org/admin/). Search and select the previous event.
7. Update the `Email` field.
8. Remove everyone from the organizing team (don't forget the `main organizer` field).
9. Send this [email](../howto/emails/old-team-email-transfer.md) to the previous team to keep them posted about this change.

You're done! Let's move to the new event!

1. [Add new organizers](../howto/add-organizer.md).
2. Go back to [Google Apps admin](http://admin.google.com/) and create a new email account for the event ([city]@djangogirls.org). Copy the password.
3. Go back to [Django Girls admin](http://djangogirls.org/admin/). Search and select the new event.
4. Update the `email` and `Main organizer` fields. Don't forget to save your modifications.
5. Send the new team this [email](../howto/emails/copy-event-new-team-setup.md).

Congrats!

### Why do we need to create a new email account?

We want to respect people privacy: the new team shouldn't be able to access the old team emails :D

## What's happening in the background:

[`copy_event`](https://github.com/DjangoGirls/djangogirls/blob/master/core/management/commands/copy_event.py) is a management command: it copies previous event's website content and menu, previous event's basic details (city, cover picture, etc) and previous event's organizers. It also increment event's URL: previous event will be `djangogirls.org/city1`, new event `djangogirls.org/city`.

Organizers don't receive an email saying their new event was created: you need to contact them.
