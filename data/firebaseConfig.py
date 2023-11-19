import pyrebase



firebaseConfig= {
    'apiKey': "AIzaSyDIVfFFVPeS-IItgh2ExPr2JPLCjh7gufI",
    'authDomain': "groovy-bonus-310519.firebaseapp.com",
    'databaseURL': "https://groovy-bonus-310519-default-rtdb.firebaseio.com",
    'projectId': "groovy-bonus-310519",
    'storageBucket': "groovy-bonus-310519.appspot.com",
    'messagingSenderId': "509390918244",
    'appId': "1:509390918244:web:84a5624f3ef04d23d20571",
    'measurementId': "G-DYE6S50CY9"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()


