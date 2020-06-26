# py-saxo
Python OpenAPI wrapper for Saxo Bank

### You'll need  
* Python 3.4 or above
* [requests](https://requests.readthedocs.io/en/master/) for Python
* [Saxo Developer Account](https://www.developer.saxo/)

### Info    
Create an app on your developer account (both DEMO/LIVE should work) using the following settings:

* Redirect URL: http://gttkeith.github.io/py-saxo/authcode
* Grant Type: Code
* Access control: ☑ Allow this app to be enabled for trading

Create a file params.json using the repo template. Fill params.json with your app's details from the developer page and you'll be good to go.

py-saxo negotiates the authentication procedure using the complete OAuth2 authorization flow. Sessions are proactively refreshed to prevent unexpected logouts.
