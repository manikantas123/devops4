[1mdiff --git a/app.py b/app.py[m
[1mindex 83b36c4..d28f0ea 100644[m
[1m--- a/app.py[m
[1m+++ b/app.py[m
[36m@@ -1,9 +1,12 @@[m
 from flask import Flask[m
[32m+[m
 app = Flask(__name__)[m
 [m
[31m-@app.route('/')[m
[32m+[m
[32m+[m[32m@app.route("/")[m
 def home():[m
     return "Hello, DevOps World!"[m
 [m
[31m-if __name__ == '__main__':[m
[32m+[m
[32m+[m[32mif __name__ == "__main__":[m
     app.run(debug=True)[m
[1mdiff --git a/test_app.py b/test_app.py[m
[1mindex e3bff5a..b15624d 100644[m
[1m--- a/test_app.py[m
[1m+++ b/test_app.py[m
[36m@@ -2,11 +2,12 @@[m
 [m
 from app import app[m
 [m
[32m+[m
 def test_home():[m
     # Use Flask's test client to simulate requests[m
     client = app.test_client()[m
[31m-    response = client.get('/')[m
[31m-    [m
[32m+[m[32m    response = client.get("/")[m
[32m+[m
     # Assert the response is OK[m
     assert response.status_code == 200[m
 [m
