from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel

from pyrebase import firebase

# Your web app's Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyBIVMAcggIA_GH2LQlN-55PPlH7rWxnOeg",
  "authDomain": "chat-app-5c065.firebaseapp.com",
  "projectId": "chat-app-5c065",
  "storageBucket": "chat-app-5c065.appspot.com",
  "messagingSenderId": "337160023458",
  "appId": "1:337160023458:web:0e09746743f882ee5156fb",
  "measurementId": "G-X8CFDMK6DL"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Login function
def login(email, password):
  try:
    # Call Firebase authentication function for login
    user = auth.sign_in_with_email_and_password(email, password)
    print("Logged in successfully:", user)
    # Redirect to dashboard or perform other actions as needed
  except Exception as e:
    # Login failed
    error_message = str(e)
    print("Login failed:", error_message)
    # Display error message to user or perform other error handling as needed

# Call the login function with email and password
email = "example@example.com"
password = "password123"
login(email, password)


# Initialize Firebase
firebase = firebase.FirebaseApplication('https://chat-app-5c065.firebaseio.com/', None)


PRIVATE_KEY = "d0eeee5a-cc9b-47fb-acb5-484c44182895"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




PRIVATE_KEY = "d0eeee5a-cc9b-47fb-acb5-484c44182895"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    username: str

@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put('https://api.chatengine.io/users/',
        data={
            "username": user.username,
            "secret": user.username,
            "first_name": user.username,
        },
        headers={ "Private-Key": PRIVATE_KEY }
    )
    return response.json()

