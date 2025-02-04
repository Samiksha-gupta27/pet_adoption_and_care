from flask import Flask, request, jsonify
import json

app = Flask(__name__)


with open("pet_care.json", "r") as f:
        data = json.load(f)


@app.route('/pets', methods=['GET'])
def get_all_pets():
    return jsonify(data["pets"])

@app.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):
    for pet in data["pets"]:
        if pet["id"] == pet_id:
            return jsonify(pet)
    return jsonify({"message": "Pet not found"})

@app.route('/pets', methods=['POST'])
def add_pet():
    new_pet = request.get_json()
    new_pet["id"] = len(data["pets"]) + 1  
    data["pets"].append(new_pet)
    save_data()
    return jsonify(new_pet), 201

@app.route('/pets/<int:pet_id>', methods=['PUT'])
def update_pet(pet_id):
    updated_pet = request.get_json()
    for i, pet in enumerate(data["pets"]):
        if pet["id"] == pet_id:
            data["pets"][i] = updated_pet
            data["pets"][i]["id"] = pet_id 
            save_data()
            return jsonify(data["pets"][i])
    return jsonify({"message": "Pet not found"})

@app.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    for i, pet in enumerate(data["pets"]):
        if pet["id"] == pet_id:
            del data["pets"][i]
            save_data()
            return jsonify({"message": "Pet deleted"})
    return jsonify({"message": "Pet not found"})

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(data["users"])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    for user in data["users"]:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"})

@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user["id"] = len(data["users"]) + 1
    data["users"].append(new_user)
    save_data()
    return jsonify(new_user)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    updated_user = request.get_json()
    for i, user in enumerate(data["users"]):
        if user["id"] == user_id:
            data["users"][i] = updated_user
            data["users"][i]["id"] = user_id
            save_data()
            return jsonify(data["users"][i])
    return jsonify({"message": "User not found"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(data["users"]):
        if user["id"] == user_id:
            del data["users"][i]
            save_data()
            return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"})

@app.route('/adoptions', methods=['GET'])
def get_all_adoptions():
    return jsonify(data["adoptions"])

@app.route('/adoptions/<int:adoption_id>', methods=['GET'])
def get_adoption_by_id(adoption_id):
    for adoption in data["adoptions"]:
        if adoption["id"] == adoption_id:
            return jsonify(adoption)
    return jsonify({"message": "Adoption not found"})

@app.route('/adoptions', methods=['POST'])
def add_adoption():
    new_adoption = request.get_json()
    new_adoption["id"] = len(data["adoptions"]) + 1
    data["adoptions"].append(new_adoption)
    save_data()
    return jsonify(new_adoption), 201

@app.route('/adoptions/<int:adoption_id>', methods=['PUT'])
def update_adoption(adoption_id):
    updated_adoption = request.get_json()
    for i, adoption in enumerate(data["adoptions"]):
        if adoption["id"] == adoption_id:
            data["adoptions"][i] = updated_adoption
            data["adoptions"][i]["id"] = adoption_id
            save_data()
            return jsonify(data["adoptions"][i])
    return jsonify({"message": "Adoption not found"})

@app.route('/adoptions/<int:adoption_id>', methods=['DELETE'])
def delete_adoption(adoption_id):
    for i, adoption in enumerate(data["adoptions"]):
        if adoption["id"] == adoption_id:
            del data["adoptions"][i]
            save_data()
            return jsonify({"message": "Adoption deleted"})
    return jsonify({"message": "Adoption not found"})


@app.route('/pets/<int:pet_id>/applications', methods=['GET'])
def get_pet_applications(pet_id): 
    applications = [app for app in data["adoptions"] if app["pet_id"] == pet_id]
    return jsonify(applications)

@app.route('/users/<int:user_id>/applications', methods=['GET'])
def get_user_applications(user_id): 
    applications = [app for app in data["adoptions"] if app["user_id"] == user_id]
    return jsonify(applications)

@app.route('/pets/<int:pet_id>/apply', methods=['POST']) 
def apply_for_pet(pet_id):
    application_data = request.get_json()
    application_data["id"] = len(data["adoptions"]) + 1
    application_data["pet_id"] = pet_id
    data["adoptions"].append(application_data)
    save_data()
    return jsonify(application_data)

@app.route('/adoptions/<int:adoption_id>/approve', methods=['PUT'])
def approve_adoption(adoption_id):
    for adoption in data["adoptions"]:
        if adoption["id"] == adoption_id:
            adoption["status"] = "approved" 
            save_data()
            return jsonify(adoption)
    return jsonify({"message": "Adoption not found"})

@app.route('/adoptions/<int:adoption_id>/reject', methods=['PUT'])
def reject_adoption(adoption_id):
    for adoption in data["adoptions"]:
        if adoption["id"] == adoption_id:
            adoption["status"] = "rejected"
            save_data()
            return jsonify(adoption)
    return jsonify({"message": "Adoption not found"})


def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


@app.route('/pets/available', methods=['GET'])
def get_available_pets():
    available_pets = [pet for pet in data["pets"] if pet["available"]]
    return jsonify(available_pets)

@app.route('/pets/species/<string:species>', methods=['GET'])
def get_pets_by_species(species):
    pets_by_species = [pet for pet in data["pets"] if pet["species"].lower() == species.lower()]
    return jsonify(pets_by_species)

@app.route('/users/<int:user_id>/pets', methods=['GET'])  
def get_pets_by_user(user_id):
    adopted_pet_ids = [adoption["pet_id"] for adoption in data["adoptions"] if adoption["user_id"] == user_id and adoption["status"] == "approved"]
    adopted_pets = [pet for pet in data["pets"] if pet["id"] in adopted_pet_ids]
    return jsonify(adopted_pets)

@app.route('/pets/<int:pet_id>/adopters', methods=['GET']) 
def get_adopters_by_pet(pet_id):
    adopter_user_ids = [adoption["user_id"] for adoption in data["adoptions"] if adoption["pet_id"] == pet_id]
    adopters = [user for user in data["users"] if user["id"] in adopter_user_ids]
    return jsonify(adopters)

@app.route('/adoptions/pending', methods=['GET']) 
def get_pending_adoptions():
    pending_adoptions = [adoption for adoption in data["adoptions"] if adoption["status"] == "pending"]
    return jsonify(pending_adoptions)

if __name__ == '__main__':
    app.run(debug=True)