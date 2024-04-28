import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Fetch the service account key JSON file contents
cred = credentials.Certificate('/Users/amelibaev/IdeaProjects/untitled/howimetyourmotherboard-328fb-firebase-adminsdk-lhdr0-fd9eb2c8cc.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://howimetyourmotherboard-328fb-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regardless of Security Rules
ref = db.reference('server/saving-data/fireblog')
print(ref.get())

users_ref = ref.child('imagedata')
users_ref.set({
    'image1': {
        'base_64encoded': 'asdfadsflkj',
    },
})

