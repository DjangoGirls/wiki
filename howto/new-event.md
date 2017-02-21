# Someone applied to organize Django Girls event...

..and now what?

## The ideal process

1. A person goes to the [Organize page](https://djangogirls.org/organize/) and fills out the form.
2. The person provides enough details for us to realize that they:
 - have read the Organizer's Manual
 - they're pretty cool people.
3. We follow the [Deploy to city process](../howto/deploy-city.md).
4. :tada:

## What is happening in the background?

The [`organize` App](https://github.com/DjangoGirls/djangogirls/tree/master/organize) is behind the "organizer application form". Organizer applications are [visible in admin](https://djangogirls.org/admin/organize/eventapplication/). In the future, it will be possible to triage organizers requests from here. For the moment, an email containing applicant' answers is sent to hello@djangogirls: if you need to interact with an applicant, do a "reply all".

When you have reviewed an application, send applicant an [acceptance](../howto/emails/application_accepted.md) or [refusal](../howto/emails/not_enough_pre_planning.md) email. Then, follow to the [Deploy to city process](../howto/deploy-city.md).

## Troubleshooting

#### You can't figure if they want to organize or attend an event

Send them the [organize or attend template e-mail](emails/organize_or_attend.md).

#### You can't really judge if the person meets the conditions from point 2

If they seem not ready, send them the [not enough pre-planning e-mail template](emails/not_enough_pre-planning.md). Hopefully, they will check the Organizer Manual and contact us when they're more prepared.

#### They already have a good idea on how they want to organize their workshop and have read the Organizer Manual

Send them the [acceptance e-mail](emails/application_accepted.md).

#### Still not sure if this person should organize Django Girls event?

- Hangout with them on Google Hangouts.
- Find someone in the community to vouch for them.
- Talk to them more via emails.
- Recommend finding a co-organizer first.
