import streamsync as ss

print("Good day sir!")

def click_handler(state, payload):
    if (payload == None): 
        print("no payload found")
    else:
        if (payload["id"] == "set-power"):
            state["power"] = state["temp_power"]
        if (payload["id"] == "set-target"):
            state["target"] = state["temp_target"]
        

def input_handler(state, payload):
    print("input payload:") 
    print(payload)
    if (payload["id"] == "laser-power"):
        state["temp_power"] = payload["value"]
    if (payload["id"] == "laser-target"):
        state["temp_target"] = payload["value"]
    
        

def select_handler(state, payload):
    print("select handler")
    print(payload)
    state["inputs_disabled"] = payload["value"]
    

# Initialise the state
initial_state = ss.init_state({
    "my_app": {
        "title": "giga pulse 2000"
    },
    "input_value": None,
    "selector_value": None,
    "inputs_disabled": "no",
    "temp_power": "5200",
    "temp_target": "",
    "target": "",
    "power": 0,
    "my_var": "dooot",   
})