def taskEntity(db_item) -> dict:
    return {
        "id": str(db_item['_id']),
        "title": str(db_item['title']),
        "description": str(db_item['description']),
        "checkbox": bool(db_item['checkbox']),
    }

def listTaskEntity(db_item_list) -> list:
    list_task = []
    for item in db_item_list:
        list_task.append(taskEntity(item))
    return list_task