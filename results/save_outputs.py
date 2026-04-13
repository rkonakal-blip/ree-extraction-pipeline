import json, os, base64
from pathlib import Path
from datetime import datetime

OUTPUT_FOLDER  = r"C:\Users\Rithika\Desktop\ree-extraction-pipeline\results"
PDF_NAME       = "recent-advances-in-rare-earth-element-recovery-liquid-liquid-extraction-and-magnetophoretic-separation"
FIGURES_FOLDER = os.path.join(OUTPUT_FOLDER, "detected", "figures")
TABLES_FOLDER  = os.path.join(OUTPUT_FOLDER, "detected", "tables")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def img_b64(folder, fname):
    p = os.path.join(folder, fname)
    if os.path.exists(p):
        return base64.b64encode(open(p, 'rb').read()).decode()
    return None

# ─────────────────────────────────────────────────────────────────────────────
# EXTRACTION DATA (all held in memory — written once below)
# ─────────────────────────────────────────────────────────────────────────────
figures_data = []
tables_data  = []
failed_data  = []

ree_el = ["La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Y"]

# ── FIG 1  unknown (process schematic) ────────────────────────────────────────
figures_data.append({
    "filename":"page1_figure1.png","page":1,"chart_type":"unknown","confidence":"LOW",
    "data":{"chart_type":"unknown","confidence":"LOW","filename":"page1_figure1.png","data":None,
            "notes":"Process schematic: Traditional LLE vs Modified LLE (aqueous/non-aqueous/synergistic/magnetic). No quantitative data."}})

# ── FIG 2  pie (REE imports by country) ───────────────────────────────────────
figures_data.append({
    "filename":"page2_figure2.png","page":2,"chart_type":"pie","confidence":"HIGH",
    "data":{"chart_type":"pie",
            "figure_metadata":{"title":"Imported Sources — % of REE resources into the U.S.","notes":"Figure 1 in paper"},
            "data":{"slices":[{"label":"China","percentage":72.0},{"label":"Malaysia","percentage":11.0},
                              {"label":"Japan","percentage":6.0},{"label":"Estonia","percentage":5.0},
                              {"label":"Other","percentage":6.0}],"total":100.0},
            "confidence":"HIGH"}})

# ── FIG 3  bar_grouped (REO compositions) ─────────────────────────────────────
mp = [20.0,49.0,5.0,14.0,0.8,0.1,0.5,0.05,0.2,0.03,0.1,0.01,0.1,0.01,0.3]
bo = [23.0,50.0,6.0,17.0,1.0,0.1,0.6,0.05,0.2,0.02,0.1,0.01,0.1,0.01,0.2]
mw = [22.0,46.0,6.0,18.0,1.5,0.2,0.7,0.10,0.3,0.05,0.2,0.02,0.2,0.02,0.5]
sk = [ 5.0,14.0,2.0,10.0,1.8,0.3,1.2,0.30,1.0,0.20,0.5,0.10,0.5,0.05,4.0]
figures_data.append({
    "filename":"page2_figure3.png","page":2,"chart_type":"bar_grouped","confidence":"MEDIUM",
    "data":{"chart_type":"bar_grouped",
            "figure_metadata":{"title":"Average REO compositions (wt %) of selected ore deposits",
                               "orientation":"vertical",
                               "notes":"Figure 2. Broken Y-axis: main 0–50 wt%, minor elements <0.4 wt%. MEDIUM confidence for heavy REE."},
            "axes":{"category":{"label":"REO","unit":None,"categories":ree_el},
                    "value":{"label":"wt %","unit":"wt %","scale":"linear","range":[0,50],"ticks":[0,10,20,30,40,50]}},
            "data":{"series":[
                {"name":"Mountain Pass, United States","color":"blue",
                 "bars":[{"category":e,"value":v,"cumulative_bottom":None} for e,v in zip(ree_el,mp)]},
                {"name":"Bayan Obo, China","color":"red",
                 "bars":[{"category":e,"value":v,"cumulative_bottom":None} for e,v in zip(ree_el,bo)]},
                {"name":"Mount Weld, Australia","color":"green",
                 "bars":[{"category":e,"value":v,"cumulative_bottom":None} for e,v in zip(ree_el,mw)]},
                {"name":"Steenkampskraal, South Africa","color":"purple",
                 "bars":[{"category":e,"value":v,"cumulative_bottom":None} for e,v in zip(ree_el,sk)]}]},
            "special_additions":{"error_bars":None,"annotations":None,"reference_line":None},
            "confidence":"MEDIUM"}})

# ── FIG 4  unknown (molecular structures) ─────────────────────────────────────
figures_data.append({
    "filename":"page3_figure4.png","page":3,"chart_type":"unknown","confidence":"LOW",
    "data":{"chart_type":"unknown","confidence":"LOW","filename":"page3_figure4.png","data":None,
            "notes":"Molecular structure diagrams: TBP, Cyanex-272, CMPO, P507, D2EHPA, DHOA, Cyanex-923, Aliquat 336."}})

# ── FIG 5  bar_grouped (publications per year) ────────────────────────────────
yrs = [str(y) for y in range(2010,2025)]
atp = [5,5,5,8,8,10,10,12,12,15,20,20,25,25,25]
naq = [45,50,50,55,60,70,75,85,95,110,115,130,150,155,155]
syn = [10,10,12,15,15,20,20,25,30, 35, 40, 45, 55, 60, 60]
figures_data.append({
    "filename":"page3_figure5.png","page":3,"chart_type":"bar_grouped","confidence":"MEDIUM",
    "data":{"chart_type":"bar_grouped",
            "figure_metadata":{"title":"Publications Per Year (2010–2024)","orientation":"vertical",
                               "notes":"Figure 4. Three categories. Values estimated; gridlines at 0/50/100/150/200."},
            "axes":{"category":{"label":"Year","unit":None,"categories":yrs},
                    "value":{"label":"Number of Publications","unit":None,"scale":"linear","range":[0,200],"ticks":[0,50,100,150,200]}},
            "data":{"series":[
                {"name":"Aqueous Two Phase System Solvent Extraction","color":"blue",
                 "bars":[{"category":y,"value":v,"cumulative_bottom":None} for y,v in zip(yrs,atp)]},
                {"name":"Non-aqueous Solvent Extraction","color":"red",
                 "bars":[{"category":y,"value":v,"cumulative_bottom":None} for y,v in zip(yrs,naq)]},
                {"name":"Synergistic Solvent Extraction","color":"green",
                 "bars":[{"category":y,"value":v,"cumulative_bottom":None} for y,v in zip(yrs,syn)]}]},
            "special_additions":{"error_bars":None,"annotations":None,"reference_line":None},
            "confidence":"MEDIUM"}})

# ── FIG 6  multipanel a/b/c/d → scatter_line ──────────────────────────────────
def sc(name, color, pts):
    return {"name":name,"marker":"circle","color":color,"points":[{"x":x,"y":y} for x,y in pts]}

p6_panels = {
    "a": {"note":"Panel (a): %E vs concentration — decreasing with concentration",
          "series":[sc("La","blue",  [(0,85),(1,80),(2,75),(3,65),(4,55)]),
                    sc("Ce","red",   [(0,90),(1,85),(2,78),(3,70),(4,60)]),
                    sc("Nd","green", [(0,88),(1,82),(2,75),(3,68),(4,58)]),
                    sc("Sm","purple",[(0,92),(1,88),(2,82),(3,73),(4,63)]),
                    sc("Eu","orange",[(0,93),(1,89),(2,83),(3,75),(4,65)])]},
    "b": {"note":"Panel (b): %E vs concentration — increasing with concentration",
          "series":[sc("La","blue",  [(0,60),(1,70),(2,78),(3,82),(4,85)]),
                    sc("Ce","red",   [(0,65),(1,73),(2,80),(3,85),(4,88)]),
                    sc("Nd","green", [(0,68),(1,76),(2,83),(3,87),(4,90)]),
                    sc("Sm","purple",[(0,72),(1,80),(2,86),(3,89),(4,92)]),
                    sc("Eu","orange",[(0,74),(1,82),(2,87),(3,90),(4,93)])]},
    "c": {"note":"Panel (c): %E vs concentration — rising from low baseline",
          "series":[sc("La","blue",  [(0,30),(1,45),(2,58),(3,68),(4,75)]),
                    sc("Ce","red",   [(0,35),(1,50),(2,63),(3,72),(4,78)]),
                    sc("Nd","green", [(0,40),(1,55),(2,67),(3,75),(4,82)]),
                    sc("Sm","purple",[(0,45),(1,60),(2,72),(3,79),(4,85)]),
                    sc("Eu","orange",[(0,48),(1,62),(2,74),(3,81),(4,86)])]},
    "d": {"note":"Panel (d): %E vs concentration — high-start declining",
          "series":[sc("La","blue",  [(0,95),(1,90),(2,82),(3,75),(4,68)]),
                    sc("Ce","red",   [(0,96),(1,91),(2,84),(3,77),(4,70)]),
                    sc("Nd","green", [(0,97),(1,92),(2,85),(3,78),(4,71)]),
                    sc("Sm","purple",[(0,98),(1,94),(2,87),(3,80),(4,73)]),
                    sc("Eu","orange",[(0,98),(1,95),(2,88),(3,82),(4,75)])]},
}
for pl, pd in p6_panels.items():
    figures_data.append({
        "filename":"page5_figure6.png","page":5,"panel":pl,"chart_type":"scatter_line","confidence":"LOW",
        "data":{"panel":pl,"chart_type":"scatter_line",
                "figure_metadata":{"title":pd["note"],
                                   "notes":"Part of Fig. 5 (page 5). LOW confidence — limited image resolution. Approximate values."},
                "axes":{"x":{"label":"Concentration","unit":"mol/L","scale":"linear","range":[0,4],"ticks":[0,1,2,3,4]},
                        "y":{"label":"%E","unit":"%","scale":"linear","range":[0,100],"ticks":[0,20,40,60,80,100]}},
                "data":{"series":pd["series"]},
                "special_additions":{"error_bars":None,"trendline":None,"annotations":None,"reference_line":None},
                "confidence":"LOW"}})

# ── FIG 7  bar_grouped (ionic liquids %E) ─────────────────────────────────────
figures_data.append({
    "filename":"page6_figure7.png","page":6,"chart_type":"bar_grouped","confidence":"MEDIUM",
    "data":{"chart_type":"bar_grouped",
            "figure_metadata":{"title":"Effect of ILs (C4MIMCl vs C2MIMCl) on %E","orientation":"vertical",
                               "notes":"Figure 6. Black bars = Condition 1; open bars = Condition 2. Error bars present."},
            "axes":{"category":{"label":"Ionic Liquid","unit":None,"categories":["C\u2084MIMCl","C\u2082MIMCl"]},
                    "value":{"label":"%E","unit":"%","scale":"linear","range":[0,100],"ticks":[0,20,40,60,80,100]}},
            "data":{"series":[
                {"name":"Condition 1 (black bars)","color":"black",
                 "bars":[{"category":"C\u2084MIMCl","value":100.0,"cumulative_bottom":None},
                         {"category":"C\u2082MIMCl","value":100.0,"cumulative_bottom":None}]},
                {"name":"Condition 2 (open bars)","color":"white",
                 "bars":[{"category":"C\u2084MIMCl","value":35.0,"cumulative_bottom":None},
                         {"category":"C\u2082MIMCl","value":6.0,"cumulative_bottom":None}]}]},
            "special_additions":{"error_bars":[
                {"series_name":"Condition 1 (black bars)","values":[
                    {"category":"C\u2084MIMCl","error_plus":2.0,"error_minus":2.0},
                    {"category":"C\u2082MIMCl","error_plus":2.0,"error_minus":2.0}]},
                {"series_name":"Condition 2 (open bars)","values":[
                    {"category":"C\u2084MIMCl","error_plus":3.0,"error_minus":3.0},
                    {"category":"C\u2082MIMCl","error_plus":2.0,"error_minus":2.0}]}],
                "annotations":None,"reference_line":None},
            "confidence":"MEDIUM"}})

# ── FIG 8  line (DES phase diagram) ───────────────────────────────────────────
figures_data.append({
    "filename":"page8_figure8.png","page":8,"chart_type":"line","confidence":"MEDIUM",
    "data":{"chart_type":"line",
            "figure_metadata":{"title":"Binary phase diagram: ChCl + urea (DES) at 303 K",
                               "notes":"Figure 7(a). Solid-liquid solubility curves meeting at eutectic point E. Photo strip of tube samples at top."},
            "axes":{"x":{"label":"Concentration (B = urea)","unit":"wt%","scale":"linear","range":[0,100],"ticks":[0,20,40,60,80,100]},
                    "y1":{"label":"Temperature","unit":"\u00b0C","scale":"linear","range":[0,60],"ticks":[0,10,20,30,40,50,60]},
                    "y2":None},
            "data":{"series":[
                {"name":"Solubility curve — ChCl (A) side","line_style":"solid","marker":"circle","color":"blue","y_axis":"y1",
                 "points":[{"x":0,"y":30},{"x":10,"y":25},{"x":20,"y":20},{"x":30,"y":16},{"x":40,"y":12}]},
                {"name":"Solubility curve — urea (B) side","line_style":"solid","marker":"square","color":"red","y_axis":"y1",
                 "points":[{"x":100,"y":40},{"x":90,"y":34},{"x":80,"y":28},{"x":70,"y":20},{"x":60,"y":14},{"x":50,"y":12}]}]},
            "special_additions":{"error_bars":None,
                                 "annotations":["A: Solid A + saturated solution","B: Solid B + saturated solution",
                                                "C: Liquid (unsaturated)","E: Eutectic point"],
                                 "reference_line":None},
            "confidence":"MEDIUM"}})

# ── FIG 9  multipanel A/B/C → scatter_line (log D) ───────────────────────────
ree_x = ["Y","La","Ce","Pr","Nd","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"]
p9_panels = {
    "A":{"title":"Panel A: log D_Ln vs REE — TODGA/TBP and TODGA/DCE",
         "series":[{"name":"TODGA/TBP","color":"dark blue","marker":"filled circle",
                    "y":[-0.5,0.0,0.3,0.5,0.7,1.2,1.5,1.7,2.0,2.3,2.5,2.7,3.0,3.3,3.5]},
                   {"name":"TODGA/DCE","color":"black","marker":"open square",
                    "y":[-1.0,-0.5,0.0,0.2,0.3,0.8,1.0,1.2,1.5,1.8,2.0,2.2,2.5,2.8,3.0]}]},
    "B":{"title":"Panel B: log D_Ln vs REE — TODGA/TBP/IL and TODGA/TBP/nonane",
         "series":[{"name":"TODGA/TBP/IL","color":"blue","marker":"filled triangle",
                    "y":[2.0,2.2,2.5,2.7,2.9,3.3,3.6,3.8,4.0,4.2,4.3,4.4,4.5,4.5,4.5]},
                   {"name":"TODGA/TBP/nonane","color":"magenta","marker":"filled square",
                    "y":[0.5,0.7,1.0,1.2,1.4,1.8,2.0,2.2,2.4,2.5,2.6,2.7,2.8,2.9,3.0]}]},
    "C":{"title":"Panel C: log D_Ln vs REE — TODGA/IL/DCE and TODGA/IL",
         "series":[{"name":"TODGA/IL/DCE","color":"purple","marker":"filled triangle",
                    "y":[1.0,1.0,1.2,1.3,1.4,1.8,2.0,2.2,2.5,2.8,3.0,3.2,3.4,3.6,3.8]},
                   {"name":"TODGA/IL","color":"red","marker":"filled circle",
                    "y":[0.5,0.5,0.7,0.9,1.0,1.4,1.6,1.8,2.1,2.4,2.6,2.8,3.0,3.2,3.4]}]},
}
for pl, pd in p9_panels.items():
    sl = [{"name":s["name"],"marker":s["marker"],"color":s["color"],
           "points":[{"x":el,"y":y} for el,y in zip(ree_x,s["y"])]} for s in pd["series"]]
    figures_data.append({
        "filename":"page9_figure9.png","page":9,"panel":pl,"chart_type":"scatter_line","confidence":"MEDIUM",
        "data":{"panel":pl,"chart_type":"scatter_line",
                "figure_metadata":{"title":pd["title"],
                                   "notes":"Part of Fig. 8(a). X = REE element sequence. Y = log D_Ln. Values from visual reading."},
                "axes":{"x":{"label":"REE element","unit":None,"scale":"linear","range":[1,15],"ticks":ree_x},
                        "y":{"label":"log D_Ln","unit":None,"scale":"linear","range":[-1,5],"ticks":[-1,0,1,2,3,4,5]}},
                "data":{"series":sl},
                "special_additions":{"error_bars":None,"trendline":None,"annotations":None,"reference_line":None},
                "confidence":"MEDIUM"}})

# ── FIG 10  bar_grouped (separation factors, log scale) ───────────────────────
solvs = ["TODGA/DCE","TODGA/TBP","TODGA/IL","TODGA/IL/DCE","TODGA/TBP/nonane","TODGA/TBP/IL"]
figures_data.append({
    "filename":"page9_figure10.png","page":9,"chart_type":"bar_grouped","confidence":"MEDIUM",
    "data":{"chart_type":"bar_grouped",
            "figure_metadata":{"title":"Separation factors (Lu/La, Lu/Sm, Lu/Tb) for TODGA-based systems",
                               "orientation":"vertical",
                               "notes":"Figure 8(b). Log-scale Y-axis 0.1–1000. Values estimated from log-scale reading."},
            "axes":{"category":{"label":"Solvent System","unit":None,"categories":solvs},
                    "value":{"label":"Separation Factor","unit":None,"scale":"log","range":[0.1,1000],"ticks":[0.1,1,10,100,1000]}},
            "data":{"series":[
                {"name":"Lu/La","color":"blue",
                 "bars":[{"category":s,"value":v,"cumulative_bottom":None} for s,v in zip(solvs,[300,70,0.7,3.0,200,1200])]},
                {"name":"Lu/Sm","color":"red",
                 "bars":[{"category":s,"value":v,"cumulative_bottom":None} for s,v in zip(solvs,[30,12,0.5,0.4,28,50])]},
                {"name":"Lu/Tb","color":"green",
                 "bars":[{"category":s,"value":v,"cumulative_bottom":None} for s,v in zip(solvs,[5,4,0.4,0.3,5,6])]}]},
            "special_additions":{"error_bars":None,"annotations":None,"reference_line":None},
            "confidence":"MEDIUM"}})

# ── FIG 11  multipanel a (TRL) + b (heatmap ratings) ─────────────────────────
figures_data.append({
    "filename":"page11_figure11.png","page":11,"panel":"a","chart_type":"unknown","confidence":"MEDIUM",
    "data":{"panel":"a","chart_type":"unknown",
            "figure_metadata":{"title":"Technology Readiness Level (TRL) scale — REE separation technologies",
                               "notes":"Figure 10(a). TRL 1–9 arrow diagram. Estimated TRL per technology from arrow height."},
            "data":{"trl_scale":{"TRL 1":"Basic research","TRL 2":"Technology concept","TRL 3":"Proof-of-concept",
                                 "TRL 4":"Preliminary process dev.","TRL 5":"Process dev. industrial",
                                 "TRL 6":"Pilot trials industrial","TRL 7":"Optimized pilot plant",
                                 "TRL 8":"Full-scale commissioning","TRL 9":"Industrial plant in operation"},
                    "technologies":[
                        {"name":"T-LLE","full_name":"Traditional Liquid-Liquid Extraction","estimated_trl":9},
                        {"name":"ATPS","full_name":"Aqueous Two-Phase System","estimated_trl":6},
                        {"name":"NAS","full_name":"Non-Aqueous Solvent Extraction","estimated_trl":4},
                        {"name":"SA/AA","full_name":"Synergistic/Aqueous-Aqueous","estimated_trl":3},
                        {"name":"MS","full_name":"Magnetophoretic Separation","estimated_trl":3}]},
            "confidence":"MEDIUM"}})

figures_data.append({
    "filename":"page11_figure11.png","page":11,"panel":"b","chart_type":"heatmap","confidence":"LOW",
    "data":{"panel":"b","chart_type":"heatmap",
            "figure_metadata":{"title":"Environmental and economic ratings for REE technologies",
                               "notes":"Figure 10(b). Qualitative ratings: 1=best(blue), 4=worst(red). Values are estimated color readings."},
            "axes":{"rows":{"label":"Technology","labels":["T-LLE","ATPS","NAS","SA/AA","MS"]},
                    "columns":{"label":"Metric","labels":["Water consumption","Hazardous waste","Material costs","Energy expense"]},
                    "color_scale":{"label":"Rating (1=best, 4=worst)","unit":None,"range":[1,4]}},
            "data":{"matrix":[
                {"row":"T-LLE","values":[{"column":"Water consumption","value":3,"source":"estimated"},
                                         {"column":"Hazardous waste","value":4,"source":"estimated"},
                                         {"column":"Material costs","value":2,"source":"estimated"},
                                         {"column":"Energy expense","value":3,"source":"estimated"}]},
                {"row":"ATPS","values":[{"column":"Water consumption","value":1,"source":"estimated"},
                                        {"column":"Hazardous waste","value":1,"source":"estimated"},
                                        {"column":"Material costs","value":2,"source":"estimated"},
                                        {"column":"Energy expense","value":2,"source":"estimated"}]},
                {"row":"NAS","values":[{"column":"Water consumption","value":1,"source":"estimated"},
                                       {"column":"Hazardous waste","value":2,"source":"estimated"},
                                       {"column":"Material costs","value":3,"source":"estimated"},
                                       {"column":"Energy expense","value":3,"source":"estimated"}]},
                {"row":"SA/AA","values":[{"column":"Water consumption","value":2,"source":"estimated"},
                                         {"column":"Hazardous waste","value":2,"source":"estimated"},
                                         {"column":"Material costs","value":3,"source":"estimated"},
                                         {"column":"Energy expense","value":2,"source":"estimated"}]},
                {"row":"MS","values":[{"column":"Water consumption","value":1,"source":"estimated"},
                                      {"column":"Hazardous waste","value":1,"source":"estimated"},
                                      {"column":"Material costs","value":4,"source":"estimated"},
                                      {"column":"Energy expense","value":1,"source":"estimated"}]}]},
            "confidence":"LOW"}})

# ── TABLE 1  skipped (article metadata) ───────────────────────────────────────
tab_fname = f"{PDF_NAME}_page1_table2.png"
tables_data.append({
    "filename":tab_fname,"page":1,"confidence":"HIGH",
    "data":{"chart_type":"table","filename":tab_fname,"skipped":True,
            "reason":"Article submission metadata (Received: May 26 2025; Revised: Sep 22 2025; Accepted: Sep 24 2025; Published: Oct 6 2025) with journal cover thumbnail — not a data table.",
            "data":None}})

# ─────────────────────────────────────────────────────────────────────────────
# STEP 6a — COMBINED JSON
# ─────────────────────────────────────────────────────────────────────────────
combined = {
    "source": f"{PDF_NAME}.pdf",
    "extract_type": "all",
    "total_figures": len(figures_data),
    "total_tables":  len(tables_data),
    "figures": figures_data,
    "tables":  tables_data,
    "failed":  failed_data
}
json_path = os.path.join(OUTPUT_FOLDER, f"{PDF_NAME}_extracted.json")
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)
print(f"JSON saved:  {json_path}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 6b — HTML REPORT  (summarise.md)
# ─────────────────────────────────────────────────────────────────────────────
def conf_badge(c):
    col = {"HIGH":"#22c55e","MEDIUM":"#f59e0b","LOW":"#ef4444"}.get(c,"#94a3b8")
    return f'<span style="background:{col};color:white;padding:2px 8px;border-radius:4px;font-size:12px;font-weight:600">{c}</span>'

def chart_badge(t):
    col = {"pie":"#8b5cf6","bar_grouped":"#3b82f6","scatter_line":"#06b6d4",
           "line":"#10b981","heatmap":"#f59e0b","unknown":"#94a3b8","table":"#64748b"}.get(t,"#3b82f6")
    return f'<span style="background:{col};color:white;padding:2px 8px;border-radius:4px;font-size:12px">{t}</span>'

def render_data(fig):
    ct  = fig.get("chart_type","unknown")
    raw = fig.get("data") or {}
    inner = raw.get("data") or raw

    if ct == "unknown":
        notes = raw.get("notes") or (raw.get("figure_metadata") or {}).get("notes","")
        trl   = (raw.get("data") or {}).get("technologies")
        if trl:
            rows = "".join(f"<tr><td><b>{t['name']}</b></td><td>{t['full_name']}</td><td style='text-align:center'>{t['estimated_trl']}</td></tr>" for t in trl)
            return f'<p style="color:#64748b;font-style:italic;font-size:13px">{notes}</p><table class="dt"><tr><th>Abbrev.</th><th>Full Name</th><th>Est. TRL</th></tr>{rows}</table>'
        return f'<div style="background:#f1f5f9;padding:16px;border-radius:6px;color:#64748b;font-style:italic">{notes or "No data extracted"}</div>'

    if ct == "pie":
        slices = (inner.get("data") or inner).get("slices", [])
        if not slices:
            slices = inner.get("slices",[])
        rows = "".join(f"<tr><td>{s['label']}</td><td style='text-align:right;font-weight:600'>{s['percentage']}%</td></tr>" for s in slices)
        return f'<table class="dt"><tr><th>Source</th><th>Share</th></tr>{rows}</table>'

    if ct == "bar_grouped":
        series = (inner.get("data") or {}).get("series") or inner.get("series",[])
        cats   = (inner.get("axes",{}).get("category") or {}).get("categories",[])
        if not cats and series:
            cats = [b["category"] for b in series[0].get("bars",[])]
        value_lbl = (inner.get("axes",{}).get("value") or {}).get("label","Value")
        scale     = (inner.get("axes",{}).get("value") or {}).get("scale","linear")
        hdrs = "".join(f"<th>{s['name']}</th>" for s in series)
        rows = ""
        for cat in cats:
            vals = []
            for s in series:
                bv = next((b["value"] for b in s.get("bars",[]) if b["category"]==cat), "—")
                vals.append(f"<td style='text-align:right'>{bv}</td>")
            rows += f"<tr><td><b>{cat}</b></td>{''.join(vals)}</tr>"
        note = f' <span style="font-size:11px;color:#94a3b8">(log scale)</span>' if scale=="log" else ""
        return f'<p style="font-size:12px;color:#64748b;margin:0 0 6px">{value_lbl}{note}</p><div style="overflow-x:auto"><table class="dt"><tr><th>Category</th>{hdrs}</tr>{rows}</table></div>'

    if ct in ("scatter_line","scatter","line"):
        series = (inner.get("data") or {}).get("series") or inner.get("series",[])
        xl = (inner.get("axes",{}).get("x") or {}).get("label","X")
        yl = ((inner.get("axes",{}).get("y") or inner.get("axes",{}).get("y1")) or {}).get("label","Y")
        out = ""
        for s in series:
            pts  = s.get("points",[])
            rows = "".join(f"<tr><td>{p['x']}</td><td style='text-align:right'>{p['y']}</td></tr>" for p in pts[:20])
            out += f'<p style="margin:10px 0 4px;font-weight:600;color:#334155;font-size:13px">{s["name"]}</p>'
            out += f'<table class="dt"><tr><th>{xl}</th><th>{yl}</th></tr>{rows}</table>'
        return out or '<div style="color:#94a3b8">No series data</div>'

    if ct == "heatmap":
        cols   = (inner.get("axes",{}).get("columns") or {}).get("labels",[])
        matrix = (inner.get("data") or inner).get("matrix",[])
        rc_map = {"1":"#22c55e","2":"#84cc16","3":"#f59e0b","4":"#ef4444"}
        hdrs = "".join(f"<th>{c}</th>" for c in cols)
        rows = ""
        for row in matrix:
            cells = "".join(
                f'<td style="text-align:center;background:{rc_map.get(str(v["value"]),"#e2e8f0")};color:white;font-weight:700">{v["value"]}</td>'
                for v in row.get("values",[]))
            rows += f"<tr><td><b>{row['row']}</b></td>{cells}</tr>"
        return f'<p style="font-size:12px;color:#64748b;margin:0 0 6px">1=best (green) → 4=worst (red)</p><table class="dt"><tr><th>Technology</th>{hdrs}</tr>{rows}</table>'

    if ct == "table":
        skipped = raw.get("skipped") or inner.get("skipped")
        reason  = raw.get("reason","") or inner.get("reason","")
        return f'<div style="background:#fef9c3;padding:16px;border-radius:6px;color:#854d0e;font-size:13px">{reason or "Pure text table — skipped"}</div>'

    return f'<div style="color:#94a3b8">chart_type: {ct}</div>'


def sid(fname, panel=None):
    base = fname.replace(".","_").replace(" ","_")
    return f"{base}_p{panel}" if panel else base

nav_links, sections = [], []
conf_counts = {"HIGH":0,"MEDIUM":0,"LOW":0}

for fig in figures_data:
    fname  = fig.get("filename","")
    page   = fig.get("page","?")
    ct     = fig.get("chart_type","unknown")
    conf   = fig.get("confidence","LOW")
    panel  = fig.get("panel")
    s_id   = sid(fname, panel)
    label  = fname + (f" — Panel {panel}" if panel else "")
    conf_counts[conf] = conf_counts.get(conf,0)+1
    nav_links.append(f'<a href="#{s_id}">{label}</a>')
    b64    = img_b64(FIGURES_FOLDER, fname)
    img_tag = (f'<img src="data:image/png;base64,{b64}" style="max-width:100%;border-radius:4px;border:1px solid #e2e8f0">'
               if b64 else '<div class="noimg">Image not found</div>')
    panel_info = f' &mdash; Panel <strong>{panel}</strong>' if panel else ''
    sections.append(f'''
<div id="{s_id}" class="card">
  <div class="card-hdr">
    <span class="card-title">{label}{panel_info}</span>
    {chart_badge(ct)} {conf_badge(conf)}
    <span class="pg">Page {page}</span>
  </div>
  <div class="card-body">
    <div class="img-col">{img_tag}</div>
    <div class="data-col">{render_data(fig)}</div>
  </div>
</div>''')

for tbl in tables_data:
    fname = tbl.get("filename","")
    page  = tbl.get("page","?")
    conf  = tbl.get("confidence","LOW")
    s_id  = sid(fname)
    conf_counts[conf] = conf_counts.get(conf,0)+1
    nav_links.append(f'<a href="#{s_id}">{fname} [table]</a>')
    b64   = img_b64(TABLES_FOLDER, fname)
    img_tag = (f'<img src="data:image/png;base64,{b64}" style="max-width:100%;border-radius:4px;border:1px solid #e2e8f0">'
               if b64 else '<div class="noimg">Image not found</div>')
    sections.append(f'''
<div id="{s_id}" class="card">
  <div class="card-hdr">
    <span class="card-title">{fname}</span>
    {chart_badge("table")} {conf_badge(conf)}
    <span class="pg">Page {page}</span>
  </div>
  <div class="card-body">
    <div class="img-col">{img_tag}</div>
    <div class="data-col">{render_data(tbl)}</div>
  </div>
</div>''')

paper_short = "Recent Advances in REE Recovery: LLE &amp; Magnetophoretic Separation"
failed_html = ""
if failed_data:
    rows = "".join(f'<tr><td>{f["filename"]}</td><td>{f.get("reason","")}</td></tr>' for f in failed_data)
    failed_html = f'<div class="card" style="border-color:#fecaca"><div class="card-hdr" style="background:#fef2f2"><span class="card-title" style="color:#dc2626">Failed ({len(failed_data)})</span></div><div style="padding:16px"><table class="dt"><tr><th>File</th><th>Reason</th></tr>{rows}</table></div></div>'

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>REE Pipeline Report — {paper_short}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f8fafc;color:#0f172a}}
.nav{{position:sticky;top:0;z-index:200;background:white;border-bottom:2px solid #e2e8f0;padding:10px 24px;display:flex;gap:6px;flex-wrap:wrap;align-items:center}}
.nav-title{{font-weight:800;font-size:14px;color:#1e3a5f;margin-right:10px;white-space:nowrap}}
.nav a{{color:#3b82f6;text-decoration:none;padding:3px 9px;border-radius:4px;font-size:12px;white-space:nowrap;transition:background .15s}}
.nav a:hover{{background:#eff6ff}}
.header{{background:linear-gradient(135deg,#1e3a5f 0%,#2563eb 100%);color:white;padding:36px 40px 28px}}
.header h1{{font-size:20px;font-weight:700;margin-bottom:6px;line-height:1.3}}
.header p{{font-size:13px;opacity:.8;margin-bottom:20px}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:10px}}
.stat{{background:rgba(255,255,255,.15);border-radius:8px;padding:12px;text-align:center}}
.stat-num{{font-size:26px;font-weight:800}}
.stat-lbl{{font-size:11px;opacity:.8;margin-top:3px}}
.content{{max-width:1440px;margin:24px auto;padding:0 24px}}
.card{{background:white;border:1px solid #e2e8f0;border-radius:10px;margin-bottom:28px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.05)}}
.card-hdr{{background:#f8fafc;padding:12px 18px;border-bottom:1px solid #e2e8f0;display:flex;align-items:center;gap:8px;flex-wrap:wrap}}
.card-title{{font-weight:700;font-size:14px;color:#0f172a}}
.pg{{margin-left:auto;font-size:12px;color:#94a3b8}}
.card-body{{display:grid;grid-template-columns:minmax(200px,40%) 1fr;min-height:180px}}
.img-col{{padding:16px;border-right:1px solid #e2e8f0;display:flex;align-items:flex-start;justify-content:center}}
.img-col img{{max-width:100%;height:auto;border-radius:4px}}
.data-col{{padding:16px;overflow-x:auto}}
.noimg{{background:#f1f5f9;width:100%;min-height:120px;display:flex;align-items:center;justify-content:center;color:#94a3b8;border-radius:4px;font-size:13px}}
table.dt{{border-collapse:collapse;width:100%;font-size:12px;margin-top:4px}}
table.dt th{{background:#f1f5f9;padding:7px 10px;text-align:left;border:1px solid #e2e8f0;font-weight:600;white-space:nowrap}}
table.dt td{{padding:6px 10px;border:1px solid #e2e8f0;vertical-align:middle}}
table.dt tr:nth-child(even) td{{background:#f8fafc}}
@media(max-width:800px){{
  .card-body{{grid-template-columns:1fr}}
  .img-col{{border-right:none;border-bottom:1px solid #e2e8f0}}
  .header{{padding:24px 20px}}
  .content{{padding:0 12px}}
}}
</style>
</head>
<body>
<nav class="nav">
  <span class="nav-title">REE Pipeline</span>
  {''.join(nav_links)}
</nav>
<div class="header">
  <h1>{paper_short}</h1>
  <p>{PDF_NAME}.pdf &bull; Generated {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
  <div class="stats">
    <div class="stat"><div class="stat-num">{len(figures_data)}</div><div class="stat-lbl">Figures</div></div>
    <div class="stat"><div class="stat-num">{len(tables_data)}</div><div class="stat-lbl">Tables</div></div>
    <div class="stat"><div class="stat-num">{len(failed_data)}</div><div class="stat-lbl">Failed</div></div>
    <div class="stat"><div class="stat-num">{conf_counts['HIGH']}</div><div class="stat-lbl">HIGH conf.</div></div>
    <div class="stat"><div class="stat-num">{conf_counts['MEDIUM']}</div><div class="stat-lbl">MEDIUM conf.</div></div>
    <div class="stat"><div class="stat-num">{conf_counts['LOW']}</div><div class="stat-lbl">LOW conf.</div></div>
  </div>
</div>
<div class="content">
{''.join(sections)}
{failed_html}
</div>
</body>
</html>"""

html_path = os.path.join(OUTPUT_FOLDER, f"{PDF_NAME}_report.html")
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"HTML saved:  {html_path}")

# ─────────────────────────────────────────────────────────────────────────────
# STEP 6c — RUN SUMMARY JSON
# ─────────────────────────────────────────────────────────────────────────────
summary = {
    "run_timestamp":   datetime.now().isoformat(),
    "input":           f"{PDF_NAME}.pdf",
    "extract_type":    "all",
    "report":          True,
    "validate":        False,
    "total_figures":   len(figures_data),
    "total_tables":    len(tables_data),
    "total_failed":    len(failed_data),
    "confidence_breakdown": conf_counts,
    "chart_types_extracted": ["pie","bar_grouped","scatter_line","line","heatmap","unknown"],
    "outputs": {
        "combined_json": json_path,
        "html_report":   html_path
    }
}
summ_path = os.path.join(OUTPUT_FOLDER, "run_summary.json")
with open(summ_path, 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)
print(f"Summary:     {summ_path}")
print("ALL OUTPUTS SAVED.")
