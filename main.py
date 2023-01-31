import pickle
from flask import Flask, render_template, request
#create an object of the class Flask
app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods =['GET','POST'])
def predict():
    try:
        prediction = model.predict([[request.form.get('area'),request.form.get('bedrooms'),
        request.form.get('bathrooms'),request.form.get('stories'),request.form.get('mainroad')
        ,request.form.get('guestroom'),request.form.get('basement'),request.form.get('hotwaterheating'),
        request.form.get('airconditioning'),request.form.get('parking'),request.form.get('prefarea')
        ,request.form.get('furnishingstatus')]])
        output = round(prediction[0])
        return render_template("index.html",prediction_text=f'Estimated Cost of House is ₹{output}/-')
    except:
        return render_template("index.html",prediction_text='Invalid Input!')


if __name__ == '__main__':
    app.run(debug = True)
