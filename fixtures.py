import requests

def post(url, data):
    return requests.post("http://localhost:8000" + url, data=data).json()

folder_cdla = post("/api/folders/", {
    "name": "Chansons de l'année",
    "priority": 50,

})
song_jwitm = post("/api/songs/", {
    "folder": folder_cdla["id"],
    "name": "John Williams Is The Man",

})

song_roc = post("/api/songs/", {
    "folder": folder_cdla["id"],
    "name": "Rains of Castamere",
})

folder_arch = post("/api/folders/", {
    "name": "Archives",
    "priority": 40,

})

song_astro = post("/api/songs/", {
    "folder": folder_arch["id"],
    "name": "Astroboy",
})

sections = []
for section, color in [("Basse", "red"), ("Ténor", "yellow"), ("Alto", "green"), ("Soprano", "blue")]:
    sections.append(post("/api/sections/", {
        "name": section,
        "color": color,
    }))
basse, tenor, alto, soprano = sections

song_parts = []
for song in [song_roc, song_jwitm, song_astro]:
    for section in sections:
        song_parts.append(post("/api/song_parts/", {
            "name": section["name"],
            "song": song["id"],
            "section": section["id"],
        }))

users = []
singers = []
singer_data = [("ning", basse), ("frantisek", alto), ("lom-ali", tenor),
               ("mads", basse), ("谷中", soprano), ("yorda", alto),
               ("billy", tenor), ("tora", soprano)]

for name, section in singer_data:
    user = post("/api/users/", {
        "username": name,
        "name": name.title(),
    })
    users.append(user)
    singer = post("/api/singers/", {
        "user": user["id"],
        "main_section": section["id"],
        "is_active": True,
    })
    singers.append(singer)
    for song_part in song_parts:
        if song_part["section"] == section["id"]:
            post("/api/singer_parts/", {
                "is_main": True,
                "song_part": song_part["id"],
                "singer": singer["id"],
            })

# yorda is also soprano on rains of castamere
post("/api/singer_parts/", {
    "is_main": False,
    "song_part": song_parts[3]["id"],
    "singer": singers[5]["id"],
})

# post("/api/song_files/", {
#     "is_active": True,
#     "uploaded_by": users[0],
#     "path": jwitm2.xml,
#     "song": song_jwitm["id"],
#     "is_xml": True,
#     "is_score": False,

# })
