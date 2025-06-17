import streamlit as st
from collections import defaultdict

# Paddle database with tags and brands
paddles = [
    {"name": "Holbrook Sport Dune/Midnight", "level": "Beginner", "price": "Under $100", "tags": ["Control", "Plush", "Forgiveness"], "shape": "Standard", "avg_weight": 7.7, "brand": "Holbrook"},
    {"name": "Diadem Warrior Edge", "level": "Beginner", "price": "$100-$180", "tags": ["Control", "Plush", "Forgiveness"], "shape": "Standard", "avg_weight": 8.0, "brand": "Diadem"},
    {"name": "Holbrook Mav Pro 16mm", "level": "Beginner", "price": "$180+", "tags": ["Balanced", "Plush", "Spin"], "shape": "Elongated", "avg_weight": 7.9, "brand": "Holbrook"},
    {"name": "Six Zero Ruby 16mm", "level": "Intermediate", "price": "$180+", "tags": ["Spin", "Plush", "Control"], "shape": "Elongated", "avg_weight": 8.1, "brand": "Six Zero"},
    {"name": "Six Zero Double Black Diamond 16mm", "level": "Intermediate", "price": "$180+", "tags": ["Control", "Plush", "Forgiveness"], "shape": "Elongated", "avg_weight": 8.1, "brand": "Six Zero"},
    {"name": "Franklin C45 14mm", "level": "Intermediate", "price": "$180+", "tags": ["Power", "Responsive", "Aggressive"], "shape": "Elongated", "avg_weight": 7.8, "brand": "Franklin"},
    {"name": "Honolulu J2K+ 16mm", "level": "Intermediate", "price": "$180+", "tags": ["Power", "Responsive", "Forgiveness"], "shape": "Elongated", "avg_weight": 8.2, "brand": "Honolulu"},
    {"name": "JOOLA Hyperion C2-Simone", "level": "Intermediate", "price": "$100-$180", "tags": ["Balanced", "Responsive", "All-Around"], "shape": "Elongated", "avg_weight": 8.0, "brand": "JOOLA"},
    {"name": "JOOLA Scorpeus CFS Anna Bright", "level": "Intermediate", "price": "$100-$180", "tags": ["Balanced", "Responsive", "All-Around"], "shape": "Standard", "avg_weight": 7.9, "brand": "JOOLA"},
    {"name": "Holbrook Pro Aero Metallic 16mm", "level": "Intermediate", "price": "$180+", "tags": ["Power", "Responsive", "Forgiveness"], "shape": "Elongated", "avg_weight": 7.85, "brand": "Holbrook"},
    {"name": "JOOLA Perseus Pro IV 16mm", "level": "Advanced", "price": "$180+", "tags": ["Max Power", "Responsive", "Aggressive"], "shape": "Elongated", "avg_weight": 8.1, "brand": "JOOLA"},
    {"name": "JOOLA Hyperion Pro IV 16mm", "level": "Advanced", "price": "$180+", "tags": ["Power", "Responsive", "Aggressive"], "shape": "Elongated", "avg_weight": 8.0, "brand": "JOOLA"},
    {"name": "CRBN TF Genesis Trufoam Hybrid", "level": "Advanced", "price": "$180+", "tags": ["Spin", "Plush", "Control"], "shape": "Elongated", "avg_weight": 8.2, "brand": "CRBN"},
    {"name": "Paddletek TKO 12.7 mm", "level": "Advanced", "price": "$180+", "tags": ["Max Power", "Responsive", "Aggressive"], "shape": "Elongated", "avg_weight": 7.95, "brand": "Paddletek"},
    {"name": "Selkirk LUXX Control Air Invikta", "level": "Advanced", "price": "$180+", "tags": ["Max Control", "Plush", "Control"], "shape": "Elongated", "avg_weight": 8.0, "brand": "Selkirk"}
]

# Streamlit App
st.title("Which Pickleball Paddle is Right for You?")
st.write("Answer the questions below to get highly personalized paddle recommendations.")

# Questions
skill = st.selectbox("What is your skill level?", ["Beginner", "Intermediate", "Advanced"])
style = st.selectbox("How would you describe your playing style?", ["Aggressive", "Control", "All-Around", "Quick Hands"])
power_control = st.selectbox("What do you want most from your paddle?", ["Max Power", "Mostly Power", "Balanced", "Mostly Control", "Max Control"])
feel = st.selectbox("How would you describe the feel you prefer?", ["Plush", "Responsive", "No Preference"])
shape = st.selectbox("Which paddle shape do you prefer?", ["Elongated", "Standard", "No Preference"])
weight = st.selectbox("Which paddle weight do you prefer?", ["Lighter", "Midweight", "Heavier", "No Preference"])
budget = st.selectbox("What’s your budget range?", ["Under $100", "$100-$180", "$180+"])
brand_pref = st.multiselect("Are there any brands you’re most interested in?", ["JOOLA", "Six Zero", "Selkirk", "Holbrook", "CRBN", "Paddletek", "Franklin", "Honolulu", "Diadem", "No Preference"])

# Start scoring
scores = defaultdict(int)

for paddle in paddles:
    if paddle["price"] != budget and budget != "$180+":
        continue

    if paddle["level"] == skill:
        scores[paddle["name"]] += 1

    if power_control == "Max Power" and "Max Power" in paddle["tags"]:
        scores[paddle["name"]] += 5
    elif power_control == "Mostly Power" and "Power" in paddle["tags"]:
        scores[paddle["name"]] += 5
    elif power_control == "Balanced" and "Balanced" in paddle["tags"]:
        scores[paddle["name"]] += 5
    elif power_control == "Mostly Control" and "Control" in paddle["tags"]:
        scores[paddle["name"]] += 5
    elif power_control == "Max Control" and "Max Control" in paddle["tags"]:
        scores[paddle["name"]] += 5

    if feel != "No Preference" and feel in paddle["tags"]:
        scores[paddle["name"]] += 3

    if style == "Aggressive" and "Power" in paddle["tags"]:
        scores[paddle["name"]] += 3
    if style == "Control" and "Control" in paddle["tags"]:
        scores[paddle["name"]] += 3
    if style == "All-Around" and "Balanced" in paddle["tags"]:
        scores[paddle["name"]] += 3
    if style == "Quick Hands" and "Forgiveness" in paddle["tags"]:
        scores[paddle["name"]] += 3

    if shape != "No Preference" and shape == paddle["shape"]:
        scores[paddle["name"]] += 2

    if weight == "Lighter" and paddle["avg_weight"] < 8.0:
        scores[paddle["name"]] += 1
    if weight == "Heavier" and paddle["avg_weight"] >= 8.0:
        scores[paddle["name"]] += 1

    if skill == "Advanced" and power_control == "Max Power" and feel == "Responsive" and paddle["name"] == "JOOLA Perseus Pro IV 16mm":
        scores[paddle["name"]] += 3
    if skill == "Advanced" and power_control == "Max Control" and feel == "Plush" and paddle["name"] == "Selkirk LUXX Control Air Invikta":
        scores[paddle["name"]] += 3

    if "No Preference" not in brand_pref and paddle["brand"] in brand_pref:
        scores[paddle["name"]] += 3

# Show recommendations
if st.button("Find My Paddle"):
    if scores:
        sorted_paddles = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        st.subheader("Your Top Paddle Recommendations:")
        for paddle, score in sorted_paddles[:3]:
            st.write("-", paddle)
    else:
        st.write("No strong matches found. Please visit us in-store for personalized help!")
