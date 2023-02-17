from flask import render_template, request, Response, stream_template, redirect, url_for

from exceptions.custom_exceptions import (IncorrectValueOfVolume, BoiledWater)
from application import app, teapot
from journal import get_data as journal_data


@app.route('/')
def home():  # Home page
    data: dict = teapot.get_data()  # Get data from teapot (temperature, volume, state)
    return render_template('home.html', data=data)  # Pass "data" to home.html and return rendered template


@app.route('/fill-teapot', methods=["POST"])
def fill_teapot():  # If run this route, teapot's temperature sets to 25. It's like taking boiled water from teapot
    data: dict = teapot.get_data()  # Get data from teapot (temperature, volume, state)

    # If request.data is not a number
    try:
        water = float(request.form.get("water_volume"))
    except ValueError:
        data["error"] = "INCORRECT INPUT!"
        return render_template('incorrect_volume.html', data=data)

    # If water in teapot is not enough or request.data is negative number
    try:
        teapot.fill_teapot(water)
    except IncorrectValueOfVolume:
        data["error"] = "Not enough :("
        return render_template('incorrect_volume.html', data=data)

    # Redirecting home after teapot is already filled
    return redirect(url_for('home'))


@app.route('/boil')
def boil():  # Boil the water
    data: dict = teapot.get_data()  # Get data from teapot (temperature, volume, state)

    # Check teapot to empty volume or water in is already boiled
    try:
        teapot.check_before_boiling()
    except IncorrectValueOfVolume:
        data["error"] = "Teapot is empty :("
        return render_template('incorrect_volume.html', data=data)

    except BoiledWater:
        data["error"] = "Water's already boiled"
        return render_template('incorrect_volume.html', data=data)

    rows = teapot.turn_on()

    # Open the stream to see in realtime boiling
    return Response(stream_template('boiling.html', rows=rows))


@app.route('/stop-boil')
def stop_boil():  # Stop boiling the water
    teapot.turn_off()
    return redirect(url_for('home'))


@app.route('/journal')
def get_journal():  # Get all actions of teapot
    data = journal_data()
    return render_template('journal.html', data=data)
