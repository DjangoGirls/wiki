# How to add a new subdomain redirection?

Say you want to have `sparkle.djangogirls.org` redirect to `https://https://en.wikipedia.org/wiki/Sparkle`.


# Step 1: Create a webapp on PythonAnywhere
- Log in to PythonAnywhere, go to the Web tab and click on "Add a new web app"
- For the domain, use "sparkle.djangogirls.org"
- Choose Python 3.4 (it doesn't actually matter)
- Choose a manual installation
- Edit the WSGI file, delete everything and put in (replace `url` accordingly):
```
    def application(environ, start_response):
        url = 'https://https://en.wikipedia.org/wiki/Sparkle'
        response_headers = [('Location', url)]
        start_response('301 Moved Permanently', response_headers)
        yield 'We moved to %s' % url
```
- Save the WSGI file then reload the app (green button)
- Write down the CNAME of the app (something like "webapp-12345.pythonanywhere.com")

# Step 2: Add a `CNAME` record in the DNS
- Log in to CloudFlare, go to the DNS tab and add a new CNAME record:
  - Type: CNAME
  - Name: sparkle
  - Domain Name: webapp-12345.pythonanywhere.com


# Step 3: Enjoy the redirection

That's it! :tada:

It should work now, though you might have to wait a bit for DNS to propagate.
