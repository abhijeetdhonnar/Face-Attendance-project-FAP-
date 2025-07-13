import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "058382":
        {
            "name": "   Mahesh Kathe",
            "major": "tybcom",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2025-07-11 13:54:34"
        },
    "618383":
        {
            "name": "Gitanjali Dhonnar",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2025-07-11 12:54:34"
        },
    "649482":
        {
            "name": "sarvesh khambekar",
            "major": "Physics",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2025-05-11 9:54:34"
        },
"747381":
        {
            "name": "abhijeet dhonnar",
            "major": "Graduation",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2025-05-11 9:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)