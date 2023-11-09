import json

def load_data():
    data = {
        "results": []
    }
    gohkennet = json.load(open("./soar_widgets/widget/gohkenet.json", "r"))
    # bprince = json.load(open("./soar_widgets/widget/benjaminprince.json", "r"))
    data["results"].append(gohkennet)
    # data["results"].append(bprince)
    return data


