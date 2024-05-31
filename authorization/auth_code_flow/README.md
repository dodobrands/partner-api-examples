# Authorization Code Flow Dodo IS Example 

This is an example implementation of the Authorization Code Flow client for Dodo IS.
You can learn more about Authorization Code Flow by following the [link](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow).

## Required Dependencies

- Flask - lightweight web framework. Required to process requests
- pyopenssl - required to use HTTPS

## Before launch

You need to set environment variables `CLIENT_ID` with your client_id and `CLIENT_SECRET` with your client secret

## Launch via IDE

You can use IDE. For example VS Code or PyCharm. In this case, the page you need to start will open in your browser

## Manual launch

To run it manually you can use the command:

    flask  run --host=localhost --port=5001 --cert=adhoc

After launching the application you need to follow the login link in your browser. For example     

    https://auth.dodois.io/connect/authorize?client_id=<your_client_id_here>&scope=shared openid&response_type=code&redirect_uri=https://localhost:5001&code_challenge=51FaJvQFsiNdiFWIq2EMWUKeAqD47dqU_cHzJpfHl-Q&code_challenge_method=S256

Instead of `<your_client_id_here>` you need to substitute your client id

## I don't have a client id and client secret

You can get it [here](https://marketplace.dodois.io/dev/apps)


