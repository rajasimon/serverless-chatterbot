# serverless-chatterbot
Bring back chatterbot to live using AWS Lambda

This examples promising ready to deploy your application in serverless namingly AWS Lambda. This example uses `chalice` library. It's maintain by AWS and packed with lots of cool stuff. Very familier api promising easy development with Chalice.

## Notes

Chalice can't deploy non wheel application to lambda yet. So we need to manually build those libraries and generate package to aws. See the Dockerfile for how to build those packages. After that placed that in vendor folder so chalice will pick that libraries. 

Also please make sure to add `DATABASE_URI` in environment variable `.chalice/config.json`



