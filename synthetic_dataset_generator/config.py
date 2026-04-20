import numpy as np

# ── Paper-level ──────────────────────────────────────────────────────────────
PAGES_OPTIONS = list(range(8, 26))
PAGES_WEIGHTS = np.array([
    1, 1, 2, 3, 4, 5, 5, 5, 4, 3,
    3, 3, 2, 2, 1, 1, 1, 1
], dtype=float)
PAGES_WEIGHTS /= PAGES_WEIGHTS.sum()

FIGURES_RANGE = (0, 15)
TABLES_RANGE  = (0, 10)

LAYOUT_OPTIONS = ["single", "double"]
LAYOUT_WEIGHTS = [4/20, 16/20]

# ── Figure classes ────────────────────────────────────────────────────────────
FIGURE_CLASSES = [
    "bar_plain", "bar_grouped", "bar_stacked",
    "scatter", "scatter_line",
    "line", "line_multiaxis",
    "spectra",
    "contour_filled", "contour_line", "contour_overlaid",
    "box_plot", "pie", "heatmap", "radar",
    "unknown",
]

CLASS_WEIGHTS = {
    "line":             0.13,
    "spectra":          0.12,
    "bar_plain":        0.11,
    "bar_grouped":      0.09,
    "scatter":          0.08,
    "scatter_line":     0.07,
    "heatmap":          0.06,
    "contour_filled":   0.04,
    "contour_line":     0.03,
    "contour_overlaid": 0.02,
    "line_multiaxis":   0.06,
    "bar_stacked":      0.04,
    "box_plot":         0.04,
    "radar":            0.03,
    "pie":              0.03,
    "unknown":          0.05,
}
CLASS_WEIGHTS_LIST = [CLASS_WEIGHTS[c] for c in FIGURE_CLASSES]

# ── Figure rendering ──────────────────────────────────────────────────────────
DPI_OPTIONS = [72, 96, 150, 300, 600]
DPI_WEIGHTS = [0.05, 0.10, 0.40, 0.35, 0.10]

WIDTH_RANGE  = (1.5, 6.5)
ASPECT_RANGE = (0.8, 2.5)

MULTIPANEL_PROB   = 0.30
PANEL_COUNT_RANGE = (2, 4)
IS_VECTOR_PROB    = 0.10

# ── Captions ──────────────────────────────────────────────────────────────────
CAPTION_STYLES   = ["Figure N.", "Fig. N.", "Fig N", "Figure N:", "FIGURE N."]
CAPTION_WEIGHTS  = [0.35, 0.30, 0.15, 0.15, 0.05]
CAPTION_LENGTH_RANGE = (3, 16)

REE_WORD_BANK = [
    "cerium", "lanthanum", "neodymium", "praseodymium", "samarium",
    "europium", "gadolinium", "terbium", "dysprosium", "ytterbium",
    "lutetium", "yttrium", "scandium", "holmium", "erbium",
    "XRD", "FTIR", "SEM", "TEM", "EDX", "ICP-MS",
    "calcination", "leaching", "solvent", "extraction", "precipitation",
    "nanoparticles", "oxide", "recovery", "concentration", "temperature",
    "pH", "efficiency", "selectivity", "adsorption", "isotherm",
    "kinetics", "luminescence", "magnetic", "ionic", "aqueous",
    "organic", "phase", "stripping", "raffinate", "D2EHPA", "Cyanex",
    "TBP", "EHEHPA", "saponification", "loading", "scrubbing",
    "spectra", "diffraction", "patterns", "analysis", "characterization",
    "morphology", "structure", "synthesis", "coating", "functionalized",
    "separation", "distribution", "coefficient", "equilibrium", "contact",
    "time", "stirring", "diluent", "kerosene", "aqueous-to-organic",
    "ratio", "synergistic", "mixture", "back-extraction", "purity",
    "yield", "mass", "transfer", "mechanism", "thermodynamics",
]

REE_BODY_TEMPLATES = [
    "Solvent extraction of {ree} from aqueous phase showed high {prop} at pH {ph:.1f}.",
    "The {ree} oxide nanoparticles were synthesized via {method} and characterized by {tech}.",
    "Recovery of {ree} reached {val:.1f}% under optimized {method} conditions.",
    "XRD patterns confirmed the formation of pure {ree} oxide after calcination at {temp:.0f} \u00b0C.",
    "The distribution coefficient of {ree} increased with increasing diluent chain length.",
    "FTIR spectra of the {ree}-loaded organic phase revealed characteristic absorption bands.",
    "Kinetic studies indicated that {ree} adsorption follows a pseudo-second-order model.",
    "Selective separation of {ree} over {ree2} was achieved using {solvent} as extractant.",
    "SEM images showed uniform {ree} particle morphology with an average size of {size:.0f} nm.",
    "The stripping efficiency of {ree} was {val:.1f}% using {conc:.2f} M HCl solution.",
    "Temperature significantly affected {ree} extraction, with optimum conditions at {temp:.0f} \u00b0C.",
    "Isotherm data for {ree} adsorption fit the Langmuir model with R\u00b2 = {r2:.3f}.",
    "An aqueous-to-organic ratio of {ratio} was found optimal for {ree} loading.",
    "Saponification of D2EHPA improved {ree} extraction efficiency by {val:.1f} percentage points.",
    "The synergistic effect between TBP and Cyanex 272 enhanced {ree} separation selectivity.",
    "Contact time experiments demonstrated that {ree} equilibrium was reached within {time:.0f} min.",
    "The effect of initial {ree} concentration on adsorption capacity was studied systematically.",
    "Thermodynamic analysis revealed that {ree} extraction by {solvent} is spontaneous and exothermic.",
    "Scrubbing with dilute HNO\u2083 removed co-extracted impurities while retaining {ree} in the organic phase.",
    "The separation factor between {ree} and {ree2} was {sf:.1f} under optimized conditions.",
]

# ── Tables ────────────────────────────────────────────────────────────────────
TABLE_CONTENT_TYPES   = ["numerical", "text+numerical", "text", "molecular"]
TABLE_CONTENT_WEIGHTS = [0.40, 0.35, 0.20, 0.05]

TABLE_ORIENTATIONS        = ["single_col", "across_2_col", "opposite_text", "across_2_pages"]
TABLE_ORIENTATION_WEIGHTS = [0.50, 0.25, 0.10, 0.15]

REE_ELEMENTS = [
    "La", "Ce", "Pr", "Nd", "Sm", "Eu", "Gd",
    "Tb", "Dy", "Ho", "Er", "Yb", "Lu", "Y", "Sc",
]

TABLE_COL_HEADERS = {
    "numerical":      ["Element", "Conc. (mg/L)", "Recovery (%)", "D value", "Sep. factor"],
    "text+numerical": ["Extractant", "pH", "Recovery (%)", "Selectivity", "Notes"],
    "text":           ["Condition", "Extractant", "Diluent", "Modifier", "Observation"],
    "molecular":      ["Compound", "Formula", "MW (g/mol)", "Purity (%)", "Supplier"],
}

MOLECULAR_FORMULAS = [
    ("Cerium(III) nitrate",   "Ce(NO3)3·6H2O",  434.22),
    ("Lanthanum oxide",       "La2O3",           325.81),
    ("Neodymium chloride",    "NdCl3",           250.60),
    ("D2EHPA",                "C16H35O4P",       322.42),
    ("Cyanex 272",            "C12H25O2PS",      272.36),
    ("TBP",                   "C12H27O4P",       266.32),
    ("Yttrium oxide",         "Y2O3",            225.81),
    ("Gadolinium nitrate",    "Gd(NO3)3·6H2O",  451.26),
    ("Europium oxide",        "Eu2O3",           351.92),
    ("Samarium sulfate",      "Sm2(SO4)3",       597.01),
]

# ── Journal metadata ──────────────────────────────────────────────────────────
JOURNAL_NAMES = [
    "Hydrometallurgy",
    "Separation and Purification Technology",
    "Chemical Engineering Journal",
    "Journal of Hazardous Materials",
    "Minerals Engineering",
    "Journal of Rare Earths",
    "Solvent Extraction and Ion Exchange",
]

AFFILIATIONS_LIST = [
    "Department of Chemical Engineering, Jiangxi University of Science and Technology, Ganzhou 341000, China",
    "School of Metallurgy and Environment, Central South University, Changsha 410083, China",
    "Department of Chemistry, Stellenbosch University, Stellenbosch 7602, South Africa",
    "Institute of Hydrometallurgy, Chinese Academy of Sciences, Beijing 100190, China",
    "Department of Chemical Engineering, University of Cape Town, Cape Town 7701, South Africa",
    "School of Chemical Engineering, University of Queensland, Brisbane QLD 4072, Australia",
    "Department of Materials Science and Engineering, MIT, Cambridge MA 02139, USA",
]

PAPER_SECTIONS = [
    ("Introduction",
     "Rare earth elements (REEs) are critical materials in modern technology, with applications ranging "
     "from permanent magnets to phosphors and catalysts. The increasing demand for REEs has intensified "
     "research into efficient extraction and separation processes."),
    ("Materials and Methods",
     "All reagents used were of analytical grade. {solvent} was obtained from {supplier} with a purity "
     "greater than 98%. REE stock solutions were prepared by dissolving the corresponding nitrate salts "
     "in deionized water and adjusting to the desired pH with dilute HNO\u2083 or NaOH."),
    ("Results and Discussion",
     "The effect of pH on extraction efficiency was investigated over the range of {ph_min:.1f} to "
     "{ph_max:.1f}. As shown in Fig. 1, the extraction percentage increased with increasing pH, reaching "
     "a maximum of {val:.1f}% at pH {ph_opt:.1f}."),
    ("Conclusions",
     "In this study, the extraction behavior of {ree} from aqueous solutions using {solvent} was "
     "systematically investigated. The results demonstrated that high recovery (>{val:.0f}%) can be "
     "achieved under optimized conditions. The separation factor between {ree} and {ree2} was "
     "sufficient for practical application."),
    ("Acknowledgements",
     "The authors gratefully acknowledge the financial support of this work by the National Natural "
     "Science Foundation (Grant No. {grant}). The authors declare no competing interests."),
]

REF_TEMPLATES = [
    "{a1}, {a2}, {a3}. {title}. {journal} {year}, {vol}, {start}\u2013{end}.",
    "{a1}, {a2}. {title}. {journal} {year}, {vol} ({issue}), {start}\u2013{end}.",
    "{a1}, {a2}, {a3}, {a4}. {title}. {journal} {year}, {vol}, {start}\u2013{end}. "
    "DOI: 10.1016/j.{abbr}.{year}.{num:05d}.",
]

REF_JOURNALS = [
    "Hydrometallurgy",
    "Sep. Purif. Technol.",
    "Chem. Eng. J.",
    "J. Hazard. Mater.",
    "Miner. Eng.",
    "J. Rare Earths",
    "Solvent Extr. Ion Exch.",
    "J. Alloys Compd.",
]

REF_TITLES = [
    "Solvent extraction of {ree} from sulfate leach solution using D2EHPA",
    "Selective separation of light and heavy rare earth elements by Cyanex 272",
    "Recovery of {ree} from secondary resources via ion exchange",
    "Synergistic extraction of lanthanides with TBP and EHEHPA",
    "Adsorption of rare earth ions onto modified mesoporous silica",
    "Thermodynamic study of {ree} extraction by saponified D2EHPA",
    "Kinetics and mechanism of cerium extraction from nitrate medium",
    "Phase equilibrium in the {ree}—D2EHPA—kerosene system",
    "Separation of {ree} and {ree2} using hollow-fibre supported liquid membranes",
    "Precipitation of rare earth oxalates from acidic leach solutions",
]

# ── Page geometry (points) ────────────────────────────────────────────────────
PAGE_W    = 595.28
PAGE_H    = 841.89
MARGIN_T  = 57.0
MARGIN_B  = 48.0
MARGIN_L  = 42.5
MARGIN_R  = 42.5
GUTTER    = 11.0
HEADER_H  = 268.0   # fixed height for page-1 title+abstract area
