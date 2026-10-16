import math, json

def plural(n, one, many):
    return one if n == 1 else many

def fixed1(x):
    return f"{math.floor(x * 10 + 0.5) / 10:.1f}"

def seam_truth(feet, section):
    if not (feet > 0):
        raise ValueError("the run must be above zero")
    if not (section > 0):
        raise ValueError("the section length must be above zero")
    sections = math.ceil(feet / section - 1e-9)
    seams = max(0, sections - 1)
    if seams <= 2:
        verdict = "barely any drips honestly"
    elif seams <= 8:
        verdict = "a few future drips honestly"
    elif seams <= 20:
        verdict = "a row of future drips honestly"
    else:
        verdict = "a whole choir of drips honestly"
    return f"{feet} {plural(feet, 'foot', 'feet')} of eave against the {section}-foot section claim is {sections} {plural(sections, 'section', 'sections')} and {seams} {plural(seams, 'seam', 'seams')} - {verdict}."

def spout_truth(area, norm):
    if not (area > 0):
        raise ValueError("the roof area must be above zero")
    if not (norm > 0):
        raise ValueError("the downspout norm must be above zero")
    spouts = math.ceil(area / norm - 1e-9)
    if spouts == 1:
        verdict = "a single downspout honestly"
    elif spouts <= 3:
        verdict = "a modest set honestly"
    elif spouts <= 6:
        verdict = "a working set honestly"
    else:
        verdict = "a downspout on every corner honestly"
    return f"{area} {plural(area, 'square foot', 'square feet')} of roof against the {norm}-square-foot downspout norm is {spouts} {plural(spouts, 'downspout', 'downspouts')} - {verdict}."

def slope_truth(feet, rate):
    if not (feet > 0):
        raise ValueError("the run must be above zero")
    if not (rate > 0):
        raise ValueError("the slope norm must be above zero")
    fall = feet * rate / 10
    rounded = math.floor(fall * 10 + 0.5) / 10
    if rounded == 0:
        verdict = "barely a fall honestly"
    elif rounded <= 1:
        verdict = "a gentle fall honestly"
    elif rounded <= 3:
        verdict = "a working fall honestly"
    else:
        verdict = "a determined fall honestly"
    fall_part = "less than a tenth of an inch" if rounded == 0 else f"{fixed1(fall)} {plural(1 if rounded == 1 else 2, 'inch', 'inches')}"
    return f"{feet} {plural(feet, 'foot', 'feet')} at the {rate}-inch-per-ten-feet slope norm falls {fall_part} toward the downspout - {verdict}."

FNS = {"seamTruth": seam_truth, "spoutTruth": spout_truth, "slopeTruth": slope_truth}

cases = [
 {"fn":"seamTruth","args":[120,10]},
 {"fn":"seamTruth","args":[8,10]},
 {"fn":"seamTruth","args":[85,10]},
 {"fn":"seamTruth","args":[220,10]},
 {"fn":"seamTruth","args":[600,10]},
 {"fn":"seamTruth","args":[10,10]},
 {"fn":"seamTruth","args":[0,10]},
 {"fn":"seamTruth","args":[120,0]},
 {"fn":"spoutTruth","args":[2400,600]},
 {"fn":"spoutTruth","args":[500,600]},
 {"fn":"spoutTruth","args":[1500,600]},
 {"fn":"spoutTruth","args":[5000,600]},
 {"fn":"spoutTruth","args":[600,600]},
 {"fn":"spoutTruth","args":[0,600]},
 {"fn":"spoutTruth","args":[2400,0]},
 {"fn":"slopeTruth","args":[40,0.25]},
 {"fn":"slopeTruth","args":[30,0.25]},
 {"fn":"slopeTruth","args":[100,0.25]},
 {"fn":"slopeTruth","args":[200,0.5]},
 {"fn":"slopeTruth","args":[40,0.5]},
 {"fn":"slopeTruth","args":[1,0.25]},
 {"fn":"slopeTruth","args":[0,0.25]},
 {"fn":"slopeTruth","args":[40,0]}
]

out = []
for c in cases:
    try:
        out.append({"fn": c["fn"], "args": c["args"], "out": FNS[c["fn"]](*c["args"])})
    except ValueError as e:
        out.append({"fn": c["fn"], "args": c["args"], "err": str(e)})
json.dump(out, open("expected.json", "w"), indent=1)
print(f"{len(out)} cases")
