import json
from flask import (Blueprint, render_template)


bp = Blueprint('pet', __name__, url_prefix="/pets")

pets = json.load(open('pets.json'))
print(pets)


@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)


@bp.route('/<int:petId>')
def showpet(petId):
    for current_pet in pets:
        print(current_pet)
        if current_pet["pet_id"] == petId:
            pet = current_pet
            return render_template('pets/show.html', pet=pet)

    # Show the error page
