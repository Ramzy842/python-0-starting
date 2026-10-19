from typing import Any

def all_thing_is_obj(object: Any) -> int:
    if object is None:
        return
    types = { 
            list: "List",
            tuple: "Tuple",
            set: "Set",
            dict: "Dict",
        }
    tp = type(object)
    if tp in types:
        print(f"{types[tp]} : {tp}")
    elif tp is int:
        print("Type not found")
    elif tp is str:
        print(f"{object} is in the kitchen : <class 'str'>")
    return 42
