from github import Github

def lambda_handler(event, context):
    print("Starting functions\n---------------------------------------------")

    if event["input"] == "Hello":
        return "World"
    else:
        raise
