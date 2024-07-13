<h2>API that Creates, Reads, Updates, and Deletes items from a DynamoDB table. The API will run serverless, so there is no management of the underlying infrastructure and scaling is done automatically.</h2>

**When you invoke your HTTP API, API Gateway routes the request to your Lambda function. The Lambda function interacts with DynamoDB, and returns a response to the API Gateway. The API Gateway then returns a response to you.**

<div align="center"><img src="https://github.com/Sathwik-git/api-http-crud/assets/126125648/3ebef6da-cf5a-41aa-8a1c-e5c6d9072c43"></div>


**Create a DynamoDB table**
<div align="center"><img src="images/dynamodb.png"></div>


**Create a lambda function**
<div align="center"><img src="images/lambda_fn.png"></div>

**Create an HTTP API**
<div align="center"><img src="images/api.png"></div>

**Create routes and attach integration(lambda function) to routes**
<div align="center"><img src="images/api_routes.png"></div>

**Testing the API**
<div align="center"><img src="images/dynamodb_final.png"></div>




