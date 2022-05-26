# How new organizers are added and invited to Slack
When a new event is deployed, there are a lot of things that are done for that event automatically. These include creating an event website, creating an email address for the event, adding organizers of the event listed in the event application to the event as well as inviting these organizers, if they are new organizers, to join Django Girls Slack Channel. 

Here we share how and where in the code for our website the new organizers are currently being added to Slack.

## Where in the code this is taking place
The process through the code is:
1. `EventApplication.deploy()` ([here](https://github.com/DjangoGirls/djangogirls/blob/main/organize/models.py#L206))
2. `Event.add_organizer(organizer.email, organizer.first_name, organizer.last_name)` ([here](https://github.com/DjangoGirls/djangogirls/blob/main/organize/models.py#L232) & [here](https://github.com/DjangoGirls/djangogirls/blob/main/organize/models.py#L242))
3. `Event.invite_organizer_to_team(user, created, password)` ([here](https://github.com/DjangoGirls/djangogirls/blob/main/core/models.py#L242))
4. `User.invite_to_slack()` ([here](https://github.com/DjangoGirls/djangogirls/blob/main/core/models.py#L57))
5. `user_invite(self.email, self.first_name)` ([here](https://github.com/DjangoGirls/djangogirls/blob/main/core/slack_client.py#L7))

And finally:
```
def user_invite(email, first_name):
    return slack.users.post('users.admin.invite', params={
        'email': email,
        'first_name': first_name,
        'set_active': True
    })
```

The email used here is the value in the `core.User` model.

## How is this being done
The process is as follows:
1. Deploy event - This is handled by the `EventApplication.deploy()` method. This method creates a new Event or clones the previous Event if it exists. It also adds the main organizer of the event to the Event and adds the co-organizers as well. 

    *TODO* - remove previous organizers if they are not part of the new organizers.

2. Add organizers to Event - This is handled by the Event.add_organizer() method. This method is called for each organizer in the EventApplication. It creates an account for new organizers if a user with that email does not exist already or gets the user and adds them to the new event. It also calls the  `Event.invite_organizer_to_the_team()` method.

3. Invite the organizer to the team - This is handled by the `Event.invite_organizer_to_team()` method. The method calls the `User.invite_to_slack()` method and notifies the user that they have been added to an event, sending them their login details.

4. Invite the user to slack - This is handled by the `User.invite_to_slack()` method and it only calls the `user_invite()` function from `slack_client.py`.

5. Inviting the user to slack - This is handled by the `user_invite()` function which takes the user's first name and email and posts them to the Slack API, setting the user's `set_active` status to `True`.

## Sending the invite manually to organizers if the automatic process fails
Usually all the processes of deploying an event and organizers work up to the point of inviting organizers to Slack. Many organizers do not get their invites to Slack. Should this happen, they can be added manually if they reach out to `hello@djangogirls.org` by following the guidelines given [here](../howto/add_people_slack.md).

## API being used to integrate to Slack
At the moment, [Slacker API](https://github.com/os/slacker) is being used to integrate our website to Slack. However, since Slacker was archived in 2020 because Slack had developed their own API, work is being done to move from Slacker to [Slack API](https://api.slack.com/).

