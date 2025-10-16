from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret123"  # required for flashing messages

def bmi_category(bmi):
    """Return (category_name, css_class) for the BMI value."""
    if bmi < 18.5:
        return "Underweight", "underweight"
    if 18.5 <= bmi < 24.9:
        return "Normal", "normal"
    if 25 <= bmi < 29.9:
        return "Overweight", "overweight"
    return "Obese", "obese"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    category = None
    css_class = None

    if request.method == "POST":
        try:
            height = request.form.get("height", "").strip()
            weight = request.form.get("weight", "").strip()

            if not height or not weight:
                flash("Please enter both height and weight.", "error")
                return redirect(url_for("index"))

            height_cm = float(height)
            weight_kg = float(weight)

            if height_cm <= 0 or weight_kg <= 0:
                flash("Height and weight must be positive!", "error")
                return redirect(url_for("index"))

            height_m = height_cm / 100
            bmi = weight_kg / (height_m * height_m)
            bmi_rounded = round(bmi, 2)

            category, css_class = bmi_category(bmi_rounded)
            result = bmi_rounded

        except ValueError:
            flash("Enter only numeric values.", "error")
            return redirect(url_for("index"))
        except ZeroDivisionError:
            flash("Height cannot be zero!", "error")
            return redirect(url_for("index"))
        except Exception as e:
            flash(f"Unexpected error: {str(e)}", "error")
            return redirect(url_for("index"))

    return render_template("index.html", result=result, category=category, css_class=css_class)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
