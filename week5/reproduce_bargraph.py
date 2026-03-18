import matplotlib.pyplot as plt
import numpy as np

# ── Data from extracted markdown table (Step 6) ──
categories = ["2011", "2012", "2013", "2014", "2015",
              "2016", "2017", "2018", "2019", "2020"]

separation       = [130, 155, 175, 195, 250, 280, 335, 420, 450, 470]
solvent_extraction = [35, 45, 65, 70, 100, 110, 150, 210, 175, 170]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 5))

ax.bar(x - width/2, separation, width, label="Separation", color="black")
ax.bar(x + width/2, solvent_extraction, width, label="Solvent Extraction", color="red")

ax.set_xlabel("Year", fontsize=12, fontweight="bold")
ax.set_ylabel("Number of Papers", fontsize=12, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha="right", fontsize=9)
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.set_ylim(0, 500)
ax.legend(loc="upper left", fontsize=9, frameon=True)
ax.tick_params(labelsize=10)

plt.tight_layout()
plt.savefig(
    r"C:\Users\Rithika\Desktop\ree-extraction-pipeline\results\bargraph\grouped_bargraph_reproduced.png",
    dpi=300,
)
plt.close()
print("Reproduced figure saved.")
