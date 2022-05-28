# Automated emails
Our website sends a lot of automated emails to organizers, support team and workshop attendees. This section of our documentation seeks to describe all the automated emails we are sending and how we are sending them for the purpose of making troubleshooting easier and letting users know which emails they can send manually. 

This document will cover the following:
- Email backend and APIs used by the website
- Event email creation
- Email sent by the contact app
- Emails sent by the organize app for event applications
- Emails sent by the core app for deployed events
- Emails sent by the applications app to workshop applicants and attendees
- What to do if automatic emails fail
- Adding a new email backend

## Email backend and APIs used by the website
We are currently using one email backend and two APIs to send emails from the website:
- [Sendgrid](https://sendgrid.com/) - is the email backend we are using to send emails from `hello@djangogirls.org` email address to event organizers and [Django Girls Support Team](). The details of the API are set using the Django setting `EMAIL_BACKEND = os.environ.get("EMAIL_BACKEND")`.
- [Gappssmtp](https://workspace.google.com/) - is the API we are using for events to send emails to workshop applicants and attendees using their event email acccounts which are [Gmail](https://mail.google.com/) accounts since our email provider is [Google](https://workspace.google.com/).
- [Mailchimp](https://mailchimp.com/) - is the API we are using to manage [newsletter signups](https://djangogirls.org/en/newsletter/) and send our [Django Girls Newsletter](https://djangogirls.org/en/newsletter/) using `hello@djangogirls.org`.

## Event email creation
Event email is created automatically when the event is deployed. 
The admin section has `Triage` options for event applications, which are `Accept application`, [Move to In Review](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L24-L25), [Move to Hold](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L16-L17) and `Reject application`. If an event application status is changed to [Move to in Review or Move to Hold](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L155-L156), a comment is added and the status is changed but no email is sent out to the organizers. 

However if an event application is [accepted or rejected](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L157-L172), an email is sent out to the organizers. We will give details about these emails below, in this section, we will only cover how the event email address is created when an event application is accepted.The process is as follows:

1. The `Accept application` triage option is selected and changes the status to [Accepted](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L168-L169) thereby trigering the [EventApplication.deploy()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/models.py#L212-L252) method which creates a new event or clones an existing one if a previous event for that city exists. 
2. This [new event](https://github.com/DjangoGirls/djangogirls/blob/main/organize/admin.py#L170-L172) will trigger the [EventApplication.send_deploy_email()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/models.py#L254-L266) method, which triggers the [get_or_create_gmail()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L121-L138) function from [core/gmail_accounts.py](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py) and then send login details to event organizers once the email is created or retrieved.
3. The [get_or_create_gmail()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L121-L138) function calls the [get_gmail_account()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L106-L118) which calls [make_email()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L43-L45) function if the event has past team members, or the [migrate_gmail_account()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L72-L103) then returns [create_gmail_account()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L48-L69) if the event has been organized us by different organizers before or [create_gmail_account()](https://github.com/DjangoGirls/djangogirls/blob/main/core/gmail_accounts.py#L48-L69) if the event is new in that city.

## Emails sent by the contact app
The contact app sends emails to either the `Django Girls Support Team` or [organizers of a selected Django Girls event](https://github.com/DjangoGirls/djangogirls/blob/main/contact/forms.py#L11-L15) via the [Contact form which is based on the contact model](https://github.com/DjangoGirls/djangogirls/blob/main/contact/models.py#L39-L54). The email is sent using `hello@djangogirls.org` via Sendgrid API.

## Emails sent by the organize app for event applications
The organize app sends a couple of emails from the start of the event application process to the end when the event is either are accepted or rejected. These are:

- Send Application Confirmation to event organizers applying to organize an event done by the [send_application_confirmation()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/emails.py#L6-L15) function called by the [OrganizeFormWizard.done()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/views.py#L47) method.
- Send Application Notification to Django Girls Support team that a new event application has been submitted via the [send_application_notification()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/emails.py#L18-L32) function called by the [OrganizeFormWizard.done()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/views.py#L48) method.
- Send Application Deployed Email to event organizers when their event application has been accepted and event deployed done by [send_application_deployed_email()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/emails.py#L35-L45) called by the []() method.
- Send Application Rejected Email to event organizers when their event application has been rejected done by [send_application_rejection_email()](https://github.com/DjangoGirls/djangogirls/blob/main/organize/emails.py#L48-L57) which is called by the []() method.

## Emails sent by the core app for deployed events 
The core app has a management command that is run as a scheduled task to send emails to organizers that meet a certain criteria. These are executed through the [handle_emails](https://github.com/DjangoGirls/djangogirls/blob/main/core/management/commands/handle_emails.py) management command which sends out the following emails:
- Thank you emails - these are handled by the [send_thank_you_emails()](https://github.com/DjangoGirls/djangogirls/blob/main/core/management/commands/handle_emails.py#L54-L68) function. They are sent to organizers who just run an event in the previous weekend to say thank you and congratulate them on the success of their event as well ask for statistics.
- Submit information emails - these are handled by the [send_submit_information_emails()](https://github.com/DjangoGirls/djangogirls/blob/main/core/management/commands/handle_emails.py#L71-L89) function. These are sent out to events which took place two weeks prior but have still not updated their statistics on number of applicants and workshop attendees. They are reminder to submit these important details.
- Offer help emails - these are handled by the [send_offer_help_emails()](https://github.com/DjangoGirls/djangogirls/blob/main/core/management/commands/handle_emails.py#L92-L125)function. These are sent to events which are deployed but still do not have a live website or live application form.

## Emails sent by the applications app to workshop applicants and attendees
Our [Organizer Manual](https://organize.djangogirls.org/) gives guidelines on sending [acceptance/rejection emails and RSVPS](https://organize.djangogirls.org/application_form/communication) to applicants and attendees. These emails are saved for each event by the [compose_email()](https://github.com/DjangoGirls/djangogirls/blob/main/applications/views.py#L211-L239) view and sent out out by the [communication()](https://github.com/DjangoGirls/djangogirls/blob/main/applications/views.py#L195-L208) view.

## What to do if automatic emails fail
1. **Contact Form emails sent by the contact app** - these can be viewed by registering the ContactForm model in the Django Girls admin as all emails are saved on submission.
2. **EventApplication emails sent by the organize app** - these are a bit difficult to resend once an event application has changed state. Organizers can be emailed manually that their event was accepted/rejected and then their event email account or Django Girls admin accounts reset.
3. **Event emails sent out by the `handle_emails` management command** - These can be resent automatically when the emails are working as they are sent by automated tasks. It is however important to ensure that these automated tasks are always running and haven't expired.
4. **Emails sent by the applications app to workshop applicants and attendees** - Organizers can download a CSV of their workshop applicants and attendees and send out the emails manually.

# Adding a new email backend/API
We have recently had some phishing emails sent to us using our own domain and to protect our domain we added a Sender Policy Framework (SPF) and DomainKeys Identified Mail (DKIM) policies to our domain on [Cloudfare](https://www.cloudflare.com/) to advertise domains authorized to send emails on behalf of our domain. 

This means adding a new email backend/API is not as simple and straightfoward as adding the API key to our environment variable. To add a new email backend/API follow the following steps:

1. Add the API key to the environment variables on [PythonAnywhere](https://www.pythonanywhere.com/). Login details are in [1password](https://1password.com/).
2. Get the new API's DKIM settings.
3. Login to [Cloudfare](https://www.cloudflare.com/) and create a `TXT` record for the new API (again login details are in [1password](https://1password.com/)).
4. Add the new API's domain to our `SPF` record on [Cloudfare](https://www.cloudflare.com/) and wait for at least 48hrs for the new domain settings to propagate. And you are all set!
