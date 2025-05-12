import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # ───── Detect which type of event this is ──────
    if "Records" in event and event["Records"][0].get("s3"):
        # ► existing S3‐upload logic
        record     = event["Records"][0]["s3"]
        bucket     = record["bucket"]["name"]
        key        = record["object"]["key"]
        msg        = f"New file uploaded: {key} in bucket: {bucket}"
        logger.info(msg)
        return {
            "statusCode": 200,
            "body": json.dumps(msg)
        }
    else:
        # ► HTTP→Lambda via API Gateway
        path       = event.get("rawPath", event.get("path", "/"))
        response = {
            "message": f"Hello from Lambda! You hit {path}"
        }
        logger.info(f"API hit: {path}")
        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json" },
            "body": json.dumps(response)
        }

