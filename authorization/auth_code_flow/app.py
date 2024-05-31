from flask import Flask, request
import requests as http
import os
import webbrowser

#client id and client secret from https://marketplace.dodois.io/dev/apps
__client_id__ = os.getenv('CLIENT_ID') #pass your client id here
__client_secret__ = os.getenv('CLIENT_SECRET') #get your client secret from environment variable 
                                                #we do not recommend storing the secret directly in code

#PKCE for oauth2. you can read the details here https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-pkce
#for example we predefine codes for PKCE
__code_challenge__ = "51FaJvQFsiNdiFWIq2EMWUKeAqD47dqU_cHzJpfHl-Q" 
__code_verifier__ = "c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646"

__scopes__ = { "openid", "shared" } # your client scopes. you can find then https://marketplace.dodois.io/dev/apps
__redirect_url__ = "https://localhost:5001" # your app redirect url. by default `https://localhost:5001`

app = Flask(__name__)

# oauth2 code flow details https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow
@app.route("/") #endpoint for 5 step from the link above
def get_token():
    args = request.args
    code = args.get("code", default="", type=str) #get code from query param

    request_body = { #build request body for step 6
        "client_id": __client_id__,
        "client_secret": __client_secret__,
        "code_verifier": __code_verifier__,
        "scope":" ".join(__scopes__),
        "grant_type": "authorization_code", #indicate that we use authorization code flow 
        "redirect_uri": __redirect_url__,
        "code": code
    }
    auth_result = http.post("https://auth.dodois.io/connect/token", data=request_body)  #send request for token (step 6)

    access_token = auth_result.json()["access_token"] #get access token from response 
    save_token(access_token) #do what you want with this token

    return 'Success', 200 #success result

def save_token(token):
    print(token)
    #do what you need

#build user authorization url and open it in browser
def show_sign_in_page(clientId, scopes, redirect_url, code_challenge):
    print("Open this link in browser:")
    url = f'https://auth.dodois.io/connect/authorize?client_id={clientId}&scope={" ".join(scopes)}&response_type=code&redirect_uri={redirect_url}&code_challenge={code_challenge}&code_challenge_method=S256'
    print(url)
    webbrowser.open(url)

if __name__ == "__main__":
    show_sign_in_page(__client_id__, __scopes__, __redirect_url__, __code_challenge__) #open consent
    app.run(host="localhost", port=5001, ssl_context='adhoc') #run server on https://localhost:5001

https://auth.dodois.io/connect/authorize?client_id=<your_client_id_here>&scope=shared openid&response_type=code&redirect_uri=https://localhost:5001&code_challenge=51FaJvQFsiNdiFWIq2EMWUKeAqD47dqU_cHzJpfHl-Q&code_challenge_method=S256
https://auth.dodois.io/connect/authorize?client_id=<your_client_id_here>&scope=shared     openid&response_type=code&redirect_uri=https://localhost:5001&code_challenge=51FaJvQFsiNdiFWIq2EMWUKeAqD47dqU_cHzJpfHl-Q&code_challenge_metho d=S256