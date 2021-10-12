from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
   {
   'id':1,
   'contact':u'9987644456',
   'name':u'Raju',
   'done':False
   },
   {
   'id':2,
   'contact':u'9876543222',
   'name':u'Rahull',
   'done':False
   }
]
@app.route("/add-data",methods=["POST"])
def add_task():
   if not request.json:
      return jsonify({
         "status":"error",
         "message":"Please provide data."
       },400)
   task={
      'id':tasks[-1]['id']+1,
      'contact':request.json['contact'],
      'name':request.json.get('name',""),
      'done':False
      }
   tasks.append(task)
   return jsonify({
      "status":"success",
      "message":"Task added successfully!"
   })
@app.route("/get-data")
def get_task():
   return jsonify({
      "data":tasks
   })
if(__name__=="__main__"):
   app.run(debug=True)