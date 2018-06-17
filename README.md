# andrew-webapp-google-cloud
### Environment setup with Google Cloud App Engine
	1. create account with Google Cloud Platform and create a project
	2. clone Google Cloud Python SDK to reference various Google Cloud API examples
		``` git clone //github.com/GoogleCloudPlatform/python-docs-samples```
	3. use the Cloud Shell to launch a local test server for your application
		``` dev_appserver.py app.yaml ```
		Your application can be viewed on http://localhost:8080/ 
		Stop your test server by pressing ```[CTRL] + C```
	4. deploy application using Coud Shell while currently in application root directory
		```gcloud app deploy```

### andrew-webapp-google-cloud