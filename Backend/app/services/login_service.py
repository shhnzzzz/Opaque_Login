from app.opaque.oprf import evaluate


async def login_start(data, db):

    user = await db.users.find_one({
        "username": data.username
    })

    if not user:

        return None

    evaluated = evaluate(int(data.blinded_password))

    return {

        "evaluated_password": str(evaluated),

        "server_public_key": "SERVER_PUBLIC_KEY_TEMP",

        "credential_record": user["credential_record"],

        "envelope": user["envelope"]

    }


async def login_finish(data, db):

    user = await db.users.find_one({
        "username": data.username
    })

    if user is None:
        return {
            "success": False,
            "message": "User not found"
        }

    if user["credential_record"] != data.shared_secret:

        return {
            "success": False,
            "message": "Invalid Password"
        }

    return {

        "success": True,

        "message": "Login Successful"

    }