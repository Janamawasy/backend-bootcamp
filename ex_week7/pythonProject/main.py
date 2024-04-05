from fastapi import FastAPI, Path, Query

app = FastAPI()
# GET - return info
# POST - create / add data
# PUT - update
# DELETE

# # end points
@app.get("/")
def home():
    return {"data": "testing"}
#
@app.get("/about")
def about():
    return {"data": "about"}
# API - application programming interface

inventory = {
        1 : {
            "name":"Milk",
            "price": 3.99,
            "brand": "Regular"
        }
    }
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(..., description="ID of the item", gt=0, lt=2)):
    return inventory[item_id]

#query paramaters
app.get("/get-by-name")
def get_item(name:str = Query(..., title="name", description="name of item")):
    print(name)
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"data": "not found"}