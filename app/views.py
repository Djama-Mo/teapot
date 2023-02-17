from flask import render_template, request, Response, stream_template, redirect, url_for

from exceptions.custom_exceptions import (IncorrectValueOfVolume, BoiledWater)
from application import app, teapot
from journal import get_data as journal_data


@app.route('/')
def home():
    data: dict = teapot.get_data()
    return render_template('home.html', data=data)


@app.route('/fill-teapot', methods=["POST"])
def fill_teapot():
    data: dict = teapot.get_data()

    try:
        water = float(request.form.get("water_volume"))
    except ValueError:
        data["error"] = "INCORRECT INPUT!"
        return render_template('incorrect_volume.html', data=data)

    try:
        teapot.fill_teapot(water)
    except IncorrectValueOfVolume:
        data["error"] = "Not enough :("
        return render_template('incorrect_volume.html', data=data)

    return redirect(url_for('home'))


@app.route('/boil')
def boil():
    data: dict = teapot.get_data()

    try:
        teapot.check_before_boiling()
    except IncorrectValueOfVolume:
        data["error"] = "Teapot is empty :("
        return render_template('incorrect_volume.html', data=data)

    except BoiledWater:
        data["error"] = "Water's already boiled"
        return render_template('incorrect_volume.html', data=data)

    rows = teapot.turn_on()
    return Response(stream_template('boiling.html', rows=rows))


@app.route('/stop-boil')
def stop_boil():
    teapot.turn_off()
    return redirect(url_for('home'))


@app.route('/journal')
def get_journal():
    data = journal_data()
    return render_template('journal.html', data=data)
