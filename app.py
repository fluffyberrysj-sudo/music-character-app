from flask import Flask, render_template, request
app = Flask(__name__)

GENRES = ["Pop", "Hip-hop", "K-pop", "EDM or Dance", "Indie Pop", "R&B"]
GENDERS = ["male", "female"]
HOBBIES = ["reading or writing", "watching", "hiking", "listening to music", "sports", "gaming"]


def normalize(text):
    return " ".join(str(text).lower().split())


base_names = {
    "pop": {"male": "Pixel Pop Boy", "female": "Pixel Pop Girl"},
    "hip-hop": {"male": "Rap Runner", "female": "Rap Spark"},
    "k-pop": {"male": "K-Star Boy", "female": "K-Star Girl"},
    "edm or dance": {"male": "Dance Pulse", "female": "Dance Glow"},
    "indie pop": {"male": "Indie Dream", "female": "Indie Moon"},
    "r&b": {"male": "R&B Soul", "female": "R&B Breeze"},
}

image_map = { 

    "pop|reading or writing": {"male": "images/pop_reading_writing_male.png", "female": "images/pop_reading_writing_female.png"}, 
    "pop|watching": {"male": "images/pop_watching_male.png", "female": "images/pop_watching_female.png"}, 
    "pop|hiking": {"male": "images/pop_hiking_male.png", "female": "images/pop_hiking_female.png"}, 
    "pop|listening to music": {"male": "images/pop_listening_to_music_male.png", "female": "images/pop_listening_to_music_female.png"}, 
    "pop|sports": {"male": "images/pop_sports_male.png", "female": "images/pop_sports_female.png"}, 
    "pop|gaming": {"male": "images/pop_gaming_male.png", "female": "images/pop_gaming_female.png"}, 

    "hip-hop|reading or writing": {"male": "images/hiphop_reading_writing_male.png", "female": "images/hiphop_reading_writing_female.png"}, 
    "hip-hop|watching": {"male": "images/hiphop_watching_male.png", "female": "images/hiphop_watching_female.png"}, 
    "hip-hop|hiking": {"male": "images/hiphop_hiking_male.png", "female": "images/hiphop_hiking_female.png"}, 
    "hip-hop|listening to music": {"male": "images/hiphop_listening_to_music_male.png", "female": "images/hiphop_listening_to_music_female.png"}, 
    "hip-hop|sports": {"male": "images/hiphop_sports_male.png", "female": "images/hiphop_sports_female.png"}, 
    "hip-hop|gaming": {"male": "images/hiphop_gaming_male.png", "female": "images/hiphop_gaming_female.png"}, 

    "k-pop|reading or writing": {"male": "images/kpop_reading_writing_male.png", "female": "images/kpop_reading_writing_female.png"}, 
    "k-pop|watching": {"male": "images/kpop_watching_male.png", "female": "images/kpop_watching_female.png"}, 
    "k-pop|hiking": {"male": "images/kpop_hiking_male.png", "female": "images/kpop_hiking_female.png"}, 
    "k-pop|listening to music": {"male": "images/kpop_listening_to_music_male.png", "female": "images/kpop_listening_to_music_female.png"}, 
    "k-pop|sports": {"male": "images/kpop_sports_male.png", "female": "images/kpop_sports_female.png"}, 
    "k-pop|gaming": {"male": "images/kpop_gaming_male.png", "female": "images/kpop_gaming_female.png"}, 

    "edm or dance|reading or writing": {"male": "images/edmordance_reading_writing_male.png", "female": "images/edmordance_reading_writing_female.png"}, 
    "edm or dance|watching": {"male": "images/edmordance_watching_male.png", "female": "images/edmordance_watching_female.png"}, 
    "edm or dance|hiking": {"male": "images/edmordance_hiking_male.png", "female": "images/edmordance_hiking_female.png"}, 
    "edm or dance|listening to music": {"male": "images/edmordance_listening_to_music_male.png", "female": "images/edmordance_listening_to_music_female.png"}, 
    "edm or dance|sports": {"male": "images/edmordance_sports_male.png", "female": "images/edmordance_sports_female.png"}, 
    "edm or dance|gaming": {"male": "images/edmordance_gaming_male.png", "female": "images/edmordance_gaming_female.png"}, 

    "indie pop|reading or writing": {"male": "images/indiepop_reading_writing_male.png", "female": "images/indiepop_reading_writing_female.png"}, 
    "indie pop|watching": {"male": "images/indiepop_watching_male.png", "female": "images/indiepop_watching_female.png"}, 
    "indie pop|hiking": {"male": "images/indiepop_hiking_male.png", "female": "images/indiepop_hiking_female.png"}, 
    "indie pop|listening to music": {"male": "images/indiepop_listening_to_music_male.png", "female": "images/indiepop_listening_to_music_female.png"}, 
    "indie pop|sports": {"male": "images/indiepop_sports_male.png", "female": "images/indiepop_sports_female.png"}, 
    "indie pop|gaming": {"male": "images/indiepop_gaming_male.png", "female": "images/indiepop_gaming_female.png"}, 

    "r&b|reading or writing": {"male": "images/rnb_reading_writing_male.png", "female": "images/rnb_reading_writing_female.png"}, 
    "r&b|watching": {"male": "images/rnb_watching_male.png", "female": "images/rnb_watching_female.png"}, 
    "r&b|hiking": {"male": "images/rnb_hiking_male.png", "female": "images/rnb_hiking_female.png"}, 
    "r&b|listening to music": {"male": "images/rnb_listening_to_music_male.png", "female": "images/rnb_listening_to_music_female.png"}, 
    "r&b|sports": {"male": "images/rnb_sports_male.png", "female": "images/rnb_sports_female.png"}, 
    "r&b|gaming": {"male": "images/rnb_gaming_male.png", "female": "images/rnb_gaming_female.png"}, 

}

description_map = {
    "pop|reading or writing": "you are super cheerful and easily get excited over small things. random ideas just pop into your head and suddenly you feel like writing or sharing them with someone.",
    "pop|watching": "you can binge watch for hours without getting bored. once you find something good you instantly want your friends to watch it too.",
    "pop|hiking": "you love exploring new places and enjoying fresh air. for you hiking is not just tiring it is also a way to clear your mind.",
    "pop|listening to music": "music is part of your everyday life. no matter your mood there is always a song that fits your vibe.",
    "pop|sports": "you do not like staying still for too long. you enjoy moving around especially when you are doing activities with friends.",
    "pop|gaming": "you play games mainly for fun not to be overly competitive. that is what makes playing with you feel relaxed and enjoyable",

    "hip-hop|reading or writing": "your mind is full of unique and random ideas. the way you express yourself makes people curious about how you think.",
    "hip-hop|watching": "you enjoy shows with strong plots and unexpected twists. after watching you often create your own theories.",
    "hip-hop|hiking": "you prefer relaxed and flexible plans. exploring new places feels better when it is spontaneous.",
    "hip-hop|listening to music": "your playlist is very diverse and your mood changes quickly. that is what makes your vibe interesting.",
    "hip-hop|sports": "you like activities that boost your energy and adrenaline. sometimes you become competitive without realizing it.",
    "hip-hop|gaming": "you are the lively one during gaming sessions. sometimes a bit chaotic but it makes everything more fun",

    "k-pop|reading or writing": "you enjoy being in your own world. your imagination keeps going and even small things can turn into full ideas.",
    "k-pop|watching": "once you like something you go all in. you explore everything from soundtracks to small details.",
    "k-pop|hiking": "you like calm and aesthetic places to recharge your energy. peaceful environments make you feel better.",
    "k-pop|listening to music": "your playlist is full of songs that lift your mood. sometimes you sing along without noticing.",
    "k-pop|sports": "you enjoy staying active because it keeps your mind fresh. once you find something you like you stay consistent.",
    "k-pop|gaming": "you enjoy fun and lively gaming sessions. your energy makes people comfortable playing with you",

    "edm or dance|reading or writing": "ideas often come when you are alone with music. you like turning those thoughts into something creative.",
    "edm or dance|watching": "you prefer shows that keep your energy up. anything slow feels boring to you.",
    "edm or dance|hiking": "you like spontaneous trips to refresh your mood. even a short break can help you reset.",
    "edm or dance|listening to music": "music is your main source of energy. everything feels better when you have the right song.",
    "edm or dance|sports": "you enjoy activities that leave you feeling tired but satisfied. energetic environments motivate you more.",
    "edm or dance|gaming": "you bring fun energy into every game. even if you are not focused on winning you make it enjoyable",

    "indie pop|reading or writing": "you notice small details that others often miss. that is where your thoughts and ideas usually come from.",
    "indie pop|watching": "you watch content to feel calm and comfortable. relaxed vibes matter the most to you.",
    "indie pop|hiking": "you enjoy quiet and peaceful nature. slow walks feel meaningful and refreshing for you.",
    "indie pop|listening to music": "you like keeping your favorite songs for yourself and listening when you need peace. music is about feeling not hype.",
    "indie pop|sports": "you prefer light and relaxed activities that keep your body fresh without pressure.",
    "indie pop|gaming": "you play games to relax. conversations and moments matter more than the result",

    "r&b|reading or writing": "you enjoy quiet time to think or write. even simple moments can stay in your mind for a long time.",
    "r&b|watching": "resting while watching something calm is your favorite way to recharge.",
    "r&b|hiking": "you enjoy slow walks and taking your time. for you healing is about enjoying the moment.",
    "r&b|listening to music": "you connect deeply with smooth and mellow songs. music feels like your comfort space.",
    "r&b|sports": "you see physical activity as a way to refresh your mind not just your body.",
    "r&b|gaming": "you enjoy relaxed gaming sessions with friends. winning is not the focus the experience is"
}

character_map = {}
for genre in GENRES:
    normalized_genre = normalize(genre)
    for gender in GENDERS:
        for hobby in HOBBIES:
            key = f"{normalized_genre}|{normalize(hobby)}"
            description = description_map.get(f"{normalized_genre}|{normalize(hobby)}", "You have a unique interesting personality based on your choices.")
            character_map[key] = {
                "name": base_names[normalized_genre][gender],
                "description": description,
                "image": image_map[key][gender],
            }


def get_character(genre, gender, hobby):
    key = f"{normalize(genre)}|{normalize(gender)}|{normalize(hobby)}"
    entry = character_map.get(key, {
        "name": base_names.get(normalize(genre), {}).get(gender, "Mystery Character"),
        "description": description_map.get(f"{normalize(genre)}|{normalize(hobby)}", "You have a unique interesting personality based on your choices."),
        "image": image_map.get(f"{normalize(genre)}|{normalize(hobby)}", {}).get(gender, "images/default.svg"),
    })

    return {
        "name": entry["name"],
        "description": entry["description"],
        "image": entry["image"],
    }


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Friend").strip() or "Friend"
        genre = request.form.get("genre", GENRES[0])
        gender = request.form.get("gender", GENDERS[0])
        hobby = request.form.get("hobby", HOBBIES[0])
        user_choice = (genre, gender, hobby)
        character = get_character(genre, gender, hobby)

        return render_template(
            "result.html",
            name=name,
            genre=genre,
            gender=gender,
            hobby=hobby,
            character=character,
        )

    return render_template("index.html", genres=GENRES, genders=GENDERS, hobbies=HOBBIES)


if __name__ == "__main__":
    app.run(debug=True)
