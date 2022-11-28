from github import Github

def lambda_handler(event, context):
    print("Starting functions\n---------------------------------------------")

    if event["input"] == "Hello":
        return "World again"
    if event["input"] == "Hi":
        return "Hi there"    
    else:
        raise
