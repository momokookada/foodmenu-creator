import sys
sys.path.append("/Users/yamadamomoko/Library/Python/3.9/lib/python/site-packages")

from flask import Flask, render_template, request, redirect, url_for
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# モックデータ
recipes = [
    {"id": 1, "name": "和風卵かけごはん", "ingredients": ["ごはん", "卵"], "calories": 450, "protein": 14, "carbs": 60, "fat": 12},
    {"id": 2, "name": "チキンソテー", "ingredients": ["鶏もも肉", "塩", "胡椒"], "calories": 600, "protein": 45, "carbs": 0, "fat": 35},
    {"id": 3, "name": "お味噌汁", "ingredients": ["味噌", "豆腐", "わかめ"], "calories": 90, "protein": 6, "carbs": 8, "fat": 3}
]
inventory = ["ごはん", "卵", "鶏もも肉", "塩", "胡椒", "味噌", "豆腐", "わかめ"]

next_id = 4


@app.route("/", methods=["GET", "POST"])
def index():
    global recipes, inventory, next_id
    if request.method == "POST":
        if "update_inventory" in request.form:
            inventory = [i.strip() for i in request.form["inventory"].replace("\n", ",").split(",") if i.strip()]
        elif "add_recipe" in request.form:
            recipes.append({
                "id": next_id,
                "name": request.form["name"],
                "ingredients": [i.strip() for i in request.form["ingredients"].split(",") if i.strip()],
                "calories": float(request.form["calories"]),
                "protein": float(request.form["protein"]),
                "carbs": float(request.form["carbs"]),
                "fat": float(request.form["fat"])
            })
            next_id += 1
        elif "edit_recipe" in request.form:
            rid = int(request.form["recipe_id"])
            for r in recipes:
                if r["id"] == rid:
                    r["name"] = request.form["name"]
                    r["ingredients"] = [i.strip() for i in request.form["ingredients"].split(",") if i.strip()]
                    r["calories"] = float(request.form["calories"])
                    r["protein"] = float(request.form["protein"])
                    r["carbs"] = float(request.form["carbs"])
                    r["fat"] = float(request.form["fat"])
        elif "delete_recipe" in request.form:
            rid = int(request.form["recipe_id"])
            recipes = [r for r in recipes if r["id"] != rid]
        elif "generate" in request.form:
            family_size = int(request.form["family_size"])
            return redirect(url_for("plan", family_size=family_size))

    return render_template("index.html", inventory_text=", ".join(inventory), recipes=recipes)


@app.route("/plan/<int:family_size>")
def plan(family_size):
    today = datetime.now().date()
    plan_data = {}
    for i in range(7):
        date_str = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        plan_data[date_str] = []
        for meal in ["朝食", "昼食", "夕食"]:
            recipe = random.choice(recipes)
            plan_data[date_str].append((meal, recipe, family_size))
    return render_template("plan.html", plan=plan_data, family_size=family_size, inventory_text=", ".join(inventory))


if __name__ == "__main__":
    app.run(debug=True)
