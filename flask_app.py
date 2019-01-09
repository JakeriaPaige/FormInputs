from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    # found in ../templates/
    return render_template("main_page.html")



def Weapon(Weapon_Choice):
    if Weapon_Choice == "Blaster" or Weapon_Choice == "Splattershot":
        return "Inkling"
    else:
        return "Octoling"

@app.route('/process_inputs', methods=['POST'])
def process_inputs():
    name = request.form.get('input_name', '')
    dropdown = request.form.get('input_dropdown', '')

    select = request.form.get('input_select', '')
    freeform = request.form.get('input_freeform', '')
    cephalpod = Weapon(dropdown)
    return render_template("main_page.html", input_data=dropdown,
            output = "You're an %s" % (cephalpod))
