from flask import Flask, request, jsonify
from models.meals import Meals
from database import db

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:admin123@127.0.0.1:3307/daily-diet-api"

db.init_app(app)


@app.route("/read-meals", methods=["GET"])
def read_meals():
    meals = Meals.query.all()
    meals_json = []

    for meal in meals:
        meals_dict = {
            "id": meal.id,
            "name_meal": meal.name_meal,
            "description_meal": meal.description_meal,
            "date": meal.date.strftime("%Y-%M-%D"),
            "hour": meal.hour.strftime("%H:%M:%S"),
            "in_the_diet": meal.in_the_diet
        }
        meals_json.append(meals_dict)
    return jsonify(meals_json)
    

@app.route("/create-meal", methods=["POST"])
def create_meal():
    data = request.json
    name_meal = data.get("name_meal")
    description_meal = data.get("description_meal")
    date = data.get("date")
    hour = data.get("hour")
    in_the_diet = data.get("in_the_diet")

    if name_meal == "":
        return jsonify({"message": "O nome refeição não pode estar vazio."}), 400
    
    meal = Meals(name_meal=name_meal, description_meal=description_meal, date=date, hour=hour, in_the_diet=in_the_diet)
    db.session.add(meal)
    db.session.commit()

    return jsonify({"message": "Refeição cadastrada com sucesso!"})


@app.route("/update-meal/<int:id_meal>", methods=["PUT"])
def update_meal(id_meal):
    data = request.json
    meal = Meals.query.get(id_meal)

    if meal and data.get("name_meal"):
        meal.name_meal = data.get("name_meal")
        meal.description_meal = data.get("description_meal")
        meal.date = data.get("date")
        meal.hour = data.get("hour")
        meal.in_the_diet = data.get("in_the_diet")
        db.session.commit()

        return jsonify({"message": "Refeição atualizada com sucesso."})
    
    return jsonify({"message": "Refeição não encontrada."}), 404


@app.route("/delete-meal/<int:id_meal>", methods=["DELETE"])
def delete_meal(id_meal):
    meal = Meals.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Refeição excluída com sucesso."})
    
    return jsonify({"message": "Refeição não encontrada."}), 404

@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
