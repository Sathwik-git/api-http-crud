<h2>API that Creates, Reads, Updates, and Deletes items from a DynamoDB table. The API will run serverless, so there is no management of the underlying infrastructure and scaling is done automatically.</h2>

**When you invoke your HTTP API, API Gateway routes the request to your Lambda function. The Lambda function interacts with DynamoDB, and returns a response to the API Gateway. The API Gateway then returns a response to you.**

<div align="center"><img src="https://github.com/Sathwik-git/api-http-crud/assets/126125648/3ebef6da-cf5a-41aa-8a1c-e5c6d9072c43"></div>

<ul>
<li>
    <p>Create a DynamoDB table</p>
    <img src="images/dynamodb.png">
</li>
<li>
    <p>Create a lambda function</p>
    <img src="images/lambda_fn.png">
</li>
<li>
    <p>Create an HTTP API</p>
    <img src="images/api.png">
</li>
<li>
    <p>Create routes and attach integration(lambda function) to routes</p>
    <img src="images/api_routes.png">
</li>
<li>
    <p>Testing the API</p>
    <img src="images/dynamodb_final.png">
</li>
</ul>


