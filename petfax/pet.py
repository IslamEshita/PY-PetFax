import json
from flask import (Blueprint, render_template)


bp = Blueprint('pet', __name__, url_prefix="/pets")

pets = json.load(open('pets.json'))
print(pets)


@bp.route('/')
def index():
    return render_template('index.html', pets=pets)


@bp.route('/<int:petId>')
def showpet(petId):
    # Get the pet
    pet = pets[petId]
    # Render the template
    return render_template('show.html', pet=pet)
