# Copy an event

These are instructions on what to do when organizers from some city want to organize a second (or third, or fourth) edition. 

## Instructions

1. Go to http://djangogirls.org/admin/core/event/
2. Find the last event in this city. It's important that this is the last (most recent) event in the city, not any other. Note the ID of the event (you can see it in URL of the event).
3. Go to your terminal and run this command:
```
heroku run python manage.py copy_event --app djangogirls
```
4. Answer questions:

> First, give me the ID of the Event object we're gonna copy. Don't mix it up with EventPage object. If there is more than one event in this city already, give me ID of the latest one: **[ENTER ID FROM POINT 2 HERE]**  
What is the number of the event in this city? If this is a second event, write 2. If third, then 3. You got it: **[ENTER NUMBER OF THE EVENT]**  
What is the date of this new event? (Format: DD/MM/YYYY or MM/YYYY): **[ENTER DATE]**

> OK! That's it. Now I'll copy your event.  
Website is ready here: http://djangogirls.org/berlin  
Congrats on yet another event!  

:tada:!