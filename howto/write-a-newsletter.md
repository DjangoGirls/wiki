# How to write fortnight Django Girls Dispatch

Every month, we send Django Girls Dispatch. We hope that in time we will find a volunteer to continue the work but right now, the ambassador is doing it.

Right now, we only send a list of previous and next events but also events with open registration.

## How?

We use [Mailchimp](https://login.mailchimp.com/) to create our newsletters.
Instructions may look super scary and long but don't worry, most of it is automated now :D

1. Go to [https://login.mailchimp.com/](https://login.mailchimp.com/).
2. Use credentails from 1Password (under "Mailchimp") to log in.
3. Click on `Create Campaign`.
4. Fill the `Campaign name` field and choose `Regular Campaign`.
5. Depending of what you want to send, choose `Django Girls Newsletter` or `Shopify customers` in the drop down menu. Click on next (hidden at the bottom right of the page).
6. Fill `email subject` field.
6. Click on `Auto-tweet campaign as djangogirls` and `Auto-post to Facebook after sending` and fill those fields.
7. Click on next.
8. Select `Simple newsletter template` in `Saved Templates` tab.
9. Go to [PythonAnywhere](https://www.pythonanywhere.com/user/djangogirls2/consoles/) and select your bash console.
10. Type `./manage.py prepare_dispatch`. Answer the questions. Keep the tab open, you'll need it.
11. Go back to mailchimp.
12. Choose a nice picture from our [Flick account](https://www.flickr.com/photos/djangogirls/albums).
13. Select the main block and upload the selected picture.
14. In the toolbar, click on source `<>` and copy-past each section returned by the `prepare_dispatch` script from PythonAnywhere. NOTE: links will probably be broken because of end of line and copy-pasting "fun". Check if everything is okay :)
15. Update the `Support Us` section with latest numbers (footer of Django Girls website).
16. Change the `Support Us` picture if you want.
17. Test the newsletter (`preview and test` menu in Mailchimp) and make final adjustments.
18. Click on next, check everything one last time and click on send!
19. Go back to Mailchimp main page.
20. Go back to the Dashboard and click on `Campaigns` in the top menu.
21. Select the campaign you've just sent and move it to `Previous Newsletters`: it will update our [newsletter page](https://djangogirls.org/newsletter/) on Django Girls website.
22. Do a victory dance, you've earned it!

:tada:

## Where to look for resources?

We don't add extra content anymore. If it were to happen again someday, here is a list of where you can look to find nice things for the Dispatch:

* check tweets about Django Girls in last 2 weeks
* check new [Django Stories](https://djangogirls.org/story/) that appeared since last newsletter. Make sure to check our blog first, since website could have not the most recent stories linked.
* check our [blog](http://blog.djangogirls.org/) for other news, too.
* check events from last 2 weeks - have any of the organizers written something about their events? Any new photo albums, etc.?
* has anyone mentioned Django Girls in any article? Maybe we can add that to the newsletter, too!
* if we are planning or in the process of some important things (like hiring, working on some bigger project, starting some campaign) - make sure to mention it.
* check [GitHub](https://github.com/DjangoGirls/tutorial) - any big changes in last fortnight? Any new translations finished?
* add upcoming events.
* did you see a nice beginner friendly talk? If it was reccorded, add a link to it!
* add CFP of major Django and Python conferences.
