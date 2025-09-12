def userEntity(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "name": str(db_item['user_name']),
        "idade": int(db_item['user_age']),
        "email": str(db_item['user_email']),
        "cel": int(db_item['user_tel'])
    }

def listUserEntity(db_item_list) -> list:
    list_user = []
    for item in db_item_list:
        list_user.append(userEntity(item))
    return list_user