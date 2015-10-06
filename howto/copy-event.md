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

:tada:!

## If you're copying a one year old event

1. Copy the previous event
2. [Add organizer](../howto/add-organizer.md) if necessary
2. Check if the team is on slack
3. Check if the event has a dedicated email account ([nameofthecity]@djangogirls.org) and add it to the [event](https://djangogirls.org/admin/core/event/) if it's missing.
4. Use this [email template](../howto/emails/copy_year_old_event.md) and send it to the team <3

### Check if the team is on Slack

1. Go to [slack admin interface](https://djangogirls.slack.com/admin)
2. Use the search function

### Add someone to Slack

If the team has changed or you can't find them:

1. Go to [slack admin interface](https://djangogirls.slack.com/admin)
2. Click on "Invite new members"
3. Click on "Full members"
3. Add as many people as you need and click on "Invite n person"

### Email account

Old events usually have an email account but sometimes not connected to their event in our database. Add it to the new event in the [admin interface](https://djangogirls.org/admin/core/event/).