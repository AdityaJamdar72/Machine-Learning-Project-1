from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,predict_pipe
app=Flask(__name__)

@app.route("/")
def show_data():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict_data():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data=CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race"),
           parental_level_ofeducation=request.form.get("education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("testprepare"),
            reading_score=request.form.get("read_score"),
            writing_score=request.form.get("write_score"))
    
    df_model = CustomData.get_dataframe(data)
    prediction=predict_pipe()
    pred=prediction.predict(df_model)
    
    return render_template("home.html",results=pred[0])

if __name__=="__main__":
    print("Running server...")
    app.run(debug=True)

    