import os
import datetime
import jwt

def create_token():
    # Get environment variables or use default values
    issuer = os.getenv("ISSUER", "graphlit")
    audience = os.getenv("AUDIENCE", "https://portal.graphlit.io")
    role = os.getenv("ROLE", "Owner")

    # Get other environment variables
    environment_id = os.getenv("ENVIRONMENT_ID")
    organization_id = os.getenv("ORGANIZATION_ID")
    secret_key = os.getenv("SECRET_KEY")

    # Specify the expiration (one hour from now)
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    # Define the payload
    payload = {
        "https://graphlit.io/jwt/claims": {
            "x-graphlit-environment-id": environment_id,
            "x-graphlit-organization-id": organization_id,
            "x-graphlit-role": role,
        },
        "exp": expiration,
        "iss": issuer,
        "aud": audience,
    }

    # Sign the JWT
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token
