# Import Patreon data into our own manager

1. On the server, run: `./manage.py download_csv -u <our patreon email> -p <our patreon password> -d ~/downloads/patreon/`
   This will download a bunch of CSV files into `~/downloads/patreon/`.

2. Once the files have been downloaded, run `./manage.py import_csv ~/downloads/patreon/*.csv`. If you're running locally, and there is no rewards in your database, add `--create-rewards` flag.


# Sending out tweets

1. Log in to the admin and go to Patreon Manager > Payments

2. At the top, click on the month for which you want to send tweets.

3. For each reward tier >= $5, you will need to send an emoji tweet (you can use the filter to see only certain reward tiers).

Note: **Do not** use the "Completed" column to mark when you've sent the tweet. This column is currently used only to track the sending of physical package.


# Sending out rewards

1. Log in to the admin and go to Patreon Manager > Payments.

2. Display payments that need to be handled (`Completed: No` in filter).

3. For the "no reward", $1+ and $5+ rewards (filter), you can select all and choose the action "Mark completed" at the bottom. This is because those reward tiers do not require a package to be sent.

4. For the reward tier "Special Support Reward", each patron in the list needs to receive a package this month.

5. For the reward tiers above $10, a patron should receive a package every 3 months.

6. To figure out who needs a package, go to "Patron" model in Django Girls admin, and filter by "Show pending rewards".

8. Click on the patron's name to take you to its edit page. There, you can see their address and other information.
There's also a link to their payments next to the "view on site" and "history" links usually are.

9. Once you've sent the package, mark the 3 payments as "completed".


# Add Special Supporter

Sometimes there is a need to send someone a gift who doesn't contribute to our Patreon, but supports us in a non-financial way or sent us a donation to PayPal. Here is how to add a non-recurring, one time reward:

1. Go to [Adding Patrons in Django Girls Admin](https://djangogirls.org/admin/patreonmanager/patron/add/)
2. Fill out name and email in the first section. Provide address if available.
3. In the Payment section, fill out the following:
 - Month: [Click today]
 - Reward: Special Support Reward
 - Pledge: 0
 - Status: processed
 - Completed: leave unchecked
4. Hit Save, and you're done! :tada:
