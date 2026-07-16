from app.opaque.oprf import evaluate


async def start_registration(data):

    evaluated = evaluate(int(data.blinded_password))

    return {
        "server_public_key": "SERVER_PUBLIC_KEY_TEMP",
        "evaluated_password": str(evaluated)
    }


async def finish_registration(data, db):

    existing = await db.users.find_one({
        "$or": [
            {"username": data.username},
            {"email": data.email}
        ]
    })

    if existing:

        return {
            "success": False,
            "message": "User already exists."
        }

    await db.users.insert_one({

        "username": data.username,

        "email": data.email,

        "credential_record": data.credential_record,

        "envelope": data.envelope

    })

    return {

        "success": True,

        "message": "Registration Complete."

    }