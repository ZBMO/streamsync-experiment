import copy
import streamsync as ss

print("Good day sir!")

def click_handler(state, payload):
    if ("id" not in payload.keys()):
        print('no id found')
        return

    print("click_handler")
    print(payload)
    if (payload["id"] == "targeting_set-power"):
        state["power"] = state["temp_power"]

    if (payload["id"] == "targeting_set-target"):
        state["target"] = state["temp_target"]

def plotly_test_ten(state):
    print("ten")
    s = state["plotly_spec"]["data"]
    s[0]["y"][0] = 10
    state["plotly_spec"]["data"] = copy.copy(s)

def plotly_test_fifty(state):
    print("fifty")
    s = state["plotly_spec"]["data"]
    s[0]["y"][0] = 50
    state["plotly_spec"]["data"] = copy.copy(s)
        
def on_off(state, payload):
    print(payload)
    

def change_plotly_graph(state, value):
    index = state["selected_graph_index"]  
    s = state["plotly_spec"]["data"]
    s[0]["y"][int(index)] = value
    state["plotly_spec"]["data"] = copy.copy(s)

    
def select_handler(state, payload):
    print("select handler")
    print(payload)
    if (payload["id"] == "laser-toggle"):
        state["is_disabled"] = payload["value"]
    if (payload["id"] == "graph_index_picker"):
        state["selected_graph_index"] = payload["value"]
    if (payload["id"] == "graph_selector"):
        change_plotly_graph(state, payload["value"])
    if (payload["id"] == "targeting_laser-power"):
        state["temp_power"] = payload["value"]
    if (payload["id"] == "targeting_laser-target"):
        state["temp_target"] = payload["value"]

    
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
    "graph_index": {"0": "a", "1": "b", "2": "c"},
    "selected_graph_index": "",
    "plotly_spec": {
        "data": [
            {
                "x": ["a", "b", "c"],
                "y": [2, 2, 5],
                "type": "line",
            },
        ],
    },
    "chart_spec": {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
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


