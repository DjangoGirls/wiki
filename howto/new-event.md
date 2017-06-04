# Someone applied to organize Django Girls event...

..and now what?

## The ideal process

1. A person goes to the [Organize page](https://djangogirls.org/organize/) and fills out the form. We receive notification about it to hello@djangogirls.org.
2. The person provides enough details for us to realize that they:
 - have read the Organizer's Manual
 - they're pretty cool people
 - they will organize a workshop
3. We click the "accept" button.
4. :tada:

## What is happening in the background?

The [`organize` app](https://github.com/DjangoGirls/djangogirls/tree/master/organize) is behind the "organizer application form".

Organizers applications are [visible in the admin](https://djangogirls.org/admin/organize/eventapplication/) and should be triaged there.

An email containing applicant' answers is also sent to hello@djangogirls. If you want to interact with an applicant, move application to "in review" in the admin and "reply all" in Gmail.

### Accepting

Accept application if:
- Organizer candidate provided enough information to convince you that they can run a successful workshop, or it's a repeated organizer who's run a successful workshop before.

To accept, make sure there is no special characters or `-` in the `URL` field of the application, otherwise it may not work.

When clicking the accept button, following things will happen:  
- Application's status will be changed to "deployed"
- Website:
    - If there was a previous event in that city, the event will be copied over to a new URL (`/city`) and previous event will be renamed to `Django Girls City #3` with a URL changed to `/city3`
    - If it's a new event, a new templated website for the event will be created.
- Gmail:
    - If there was a previous event in that city, and there is at least one common organizers, the Gmail account will stay the same
    - If there was a previous event in that city, and there is no common organizers between them, the existing `city@djangogirls.org` will be renamed to `cityMONTHYEAR@djangogirls.org` and new `city@djangogirls.org` email will be created.
    - If it's a new event, new `city@djangogirls.org` email will be created.
- Organizers:
    - Organizers who applied will be given access to the event and receive e-mails with instructions and passwords
    - Organizers will be invited to join Slack
- Communication:
    - Entire team will receive a starter e-mail. [See content of the email](https://github.com/DjangoGirls/djangogirls/blob/master/templates/emails/organize/event_deployed.html)

### Rejecting

Reject application if:
- Organizer didn't provide sufficient information to judge whether they will organize a good workshop
- Organizer failed to organize a workshop previously

To reject, click the reject button and update the "comment" field describing why you rejected the event.

When clicking the reject button, following things will happen:
- Application's status will be changed to "rejected"
- Entire team will receive a rejection e-mail. [See content of the email](https://github.com/DjangoGirls/djangogirls/blob/master/templates/emails/organize/rejection.html)

### In review

Move application to in review when:
- You want to chat with applicant more via email

To move to in review, click the "in review" button and update the "comment" field describing why you want to investigate the event more.

When clicking the in review button, following things will happen:
- Application's status will be changed to "in review"

### On hold

Move application to on hold when:
- For some reason, application cannot be acted on right now

To move to on hold, click the "on hold" button and update the "comment" field describing why application is on hold.

When clicking the on hold button, following things will happen:
- Application's status will be changed to "on hold"

## Troubleshooting

#### You can't figure if they want to organize or attend an event

Send them the [organize or attend template e-mail](emails/organize_or_attend.md).

#### You can't really judge if the person meets the conditions from point 2

If they seem not ready, reject them, and they will receive a nice email encouraging them to check the Organizer Manual and contact us when they're more prepared.

#### Still not sure if this person should organize Django Girls event?

- Hangout with them on Google Hangouts.
- Find someone in the community to vouch for them.
- Talk to them more via emails.
- Recommend finding a co-organizer first.
