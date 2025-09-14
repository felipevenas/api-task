def userEntity(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "name": str(db_item['name']),
        "age": int(db_item['age']),
        "email": str(db_item['email']),
        "tel": int(db_item['tel'])
    }

def listUserEntity(db_item_list) -> list:
    list_user = []
    for item in db_item_list:
        list_user.append(userEntity(item))
    return list_user