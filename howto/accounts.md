# How to prepare the annual accounts

## How to obtain stats for events:

1. Login to PythonAnywhere. Go to Databases tab.
2. Start a Postgres Console
3. in Postgres type: 
\c djangogirls

Run SQL queries to get numbers (replace dates with those you are looking for):

*No of workshops:

select count(TO_DATE(date, 'YYYY-MM-DD')) as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD');

*No of organizers:

select count(distinct user_id) from core_event_team where core_event_team.event_id in (select id as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD'));

*No of coaches: 

select count(distinct coach_id) from core_eventpagecontent_coaches as cec join core_eventpagecontent as cep on cec.eventpagecontent_id = cep.id join core_event as ce on ce.id = cep.event_id where ce.id in (select id as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD'));

*No of attendees:

select sum(attendees_count) from core_event where id in (select id as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD'));

*No of countries: 

select count(distinct country) from core_event where id in (select id as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD'));

## How to obtain countries operated in when submitting accounts

*Open a Postgres console as above and use this command:

select distinct country from core_event where id in (select id as thedate from core_event where TO_DATE(date, 'YYYY-MM-DD') >= TO_DATE('2017-07-01', 'YYYY-MM-DD') AND TO_DATE(date, 'YYYY-MM-DD') <= TO_DATE('2018-06-30', 'YYYY-MM-DD'));
