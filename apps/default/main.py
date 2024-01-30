import streamsync as ss
import json

print("Good day sir!")

def click_handler(state, payload):
    print("click_handler")
    print(payload)
    if (payload["id"] == "set-power"):
        state["power"] = state["temp_power"]
    if (payload["id"] == "set-target"):
        state["target"] = state["temp_target"]

def plotly_test_ten(state):
    state["plotly_spec"]["data"][0]["y"][0] = 10

def plotly_test_fifty(state):
    state["plotly_spec"]["data"][0]["y"][1] = 50
        
def input_handler(state, payload):
    print("input payload:") 
    print(payload)
    if (payload["id"] == "laser-power"):
        state["temp_power"] = payload["value"]
    if (payload["id"] == "laser-target"):
        state["temp_target"] = payload["value"]
    if (payload["id"] == "graph-indexer"):
        state["change_index"] = payload["value"]
    if (payload["id"] == "graph-setter"):
        index = state["change_index"]
        state["chart_spec"]["data"]["values"][int(index)]["value"] = payload["value"]
        print(state["chart_spec"])
    

def select_handler(state, payload):
    print("select handler")
    print(payload)
    if (payload["id"] == "laser-toggle"):
        state["is_disabled"] = payload["value"]
    

# Initialise the state
initial_state = ss.init_state({
    "my_app": {
        "title": "giga pulse 2000"
    },
    "input_value": None,
    "selector_value": None,
    "temp_power": "5200",
    "temp_target": "",
    "target": "",
    "power": 0,
    "is_disabled": "no",
    "change_index": "", 
    "plotly_spec": {
        "data": [
            {
                "x": ["a", "b", "ddd"],
                "y": [22, 25, 29],
                "type": "bar",
            },
        ],
    },
    "chart_spec": {
        "$schema": "../vega-lite-schema.json",
        "description": "A simple bar chart with embedded data.",
        "width": 1000,
        "data": {
            "values": [
                {"time": 1000, "value": 90},
                {"time": 2000, "value": 11},
                {"time": 3000, "value": 12},
                {"time": 4000, "value": 13},
                {"time": 5000, "value": 17},
                {"time": 6000, "value": 37},
                {"time": 7000, "value": 50},
                {"time": 8000, "value": 70},
                {"time": 9000, "value": 100},
                {"time": 10000, "value": 0},
            ]
        },
        "mark": "point",
        "encoding": {
            "x": {"field": "time", "type": "quantitative", "title": "Time (milliseconds)"},
            "y": {"field": "value", "type": "quantitative", "title": "Value"}
        }
}})