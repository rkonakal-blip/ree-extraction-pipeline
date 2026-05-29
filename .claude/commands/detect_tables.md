# REE Pipeline — Table Detector (PDF)
**Pipeline:** REE Figure Extraction  
**Phase:** 0 — Detection (Tables)  
**Input:** Single digital PDF  
**Output:** Cropped table PNGs + detection summary

---

## Task

You are a table detection assistant for the REE Figure Extraction pipeline. Given a digital PDF, detect all tables on each page, crop them as PNG images with padding, and save them ready for the table extraction skill.

---

## Inputs required from user

1. Path to the PDF file
2. Output folder path
3. Padding in pixels (default: 25 — increase if crops are too tight)

---

## Steps

### STEP 1 — Write and execute a Python script

Write a Python script and run it immediately.

**Install dependency if needed:**
```python
pip install pymupdf
```

**Script logic:**

```python
import fitz  # PyMuPDF
import json
import os
from pathlib import Path

def detect_tables(pdf_path, output_folder, padding=25):
    os.makedirs(output_folder, exist_ok=True)
    filename = Path(pdf_path).stem
    doc = fitz.open(pdf_path)

    detected = []
    table_count = 0

    for page_num in range(len(doc)):
        page = doc[page_num]

        # Use PyMuPDF's built-in table finder
        tabs = page.find_tables()

        if not tabs.tables:
            continue

        for t_idx, table in enumerate(tabs.tables):
            bbox = table.bbox  # (x0, y0, x1, y1)

            # Skip tiny regions — likely false positives
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            if width < 80 or height < 40:
                continue

            # Add padding
            bbox_padded = (
                max(0, bbox[0] - padding),
                max(0, bbox[1] - padding),
                min(page.rect.width, bbox[2] + padding),
                min(page.rect.height, bbox[3] + padding)
            )

            # Render at 2x zoom for clean crop
            mat = fitz.Matrix(2.0, 2.0)
            clip = fitz.Rect(bbox_padded)
            pix = page.get_pixmap(matrix=mat, clip=clip)

            table_count += 1
            out_filename = f"{filename}_page{page_num+1}_table{t_idx+1}.png"
            out_path = os.path.join(output_folder, out_filename)
            pix.save(out_path)

            detected.append({
                "filename": out_filename,
                "page": page_num + 1,
                "table_index": t_idx + 1,
                "bbox": list(bbox),
                "bbox_padded": list(bbox_padded),
                "width_px": int(width * 2),
                "height_px": int(height * 2)
            })

            print(f"Page {page_num+1}, Table {t_idx+1}: {int(width)}x{int(height)}px → saved")

    doc.close()

    # Save detection summary
    summary = {
        "pdf": Path(pdf_path).name,
        "total_tables_detected": len(detected),
        "padding_px": padding,
        "tables": detected
    }
    summary_path = os.path.join(output_folder, f"{filename}_table_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    return detected
```

---

### STEP 2 — Print completion summary

Print to chat:
```
==================================================
REE PIPELINE — TABLE DETECTION COMPLETE
==================================================
PDF:              FILENAME.pdf
Tables detected:  X
Padding:          25px
--------------------------------------------------
Page 1, Table 1: XXXxXXX px → FILENAME_page1_table1.png
Page 3, Table 1: XXXxXXX px → FILENAME_page3_table1.png
...
--------------------------------------------------
Next step: Run table.md on each PNG above
==================================================
```

---

## Critical Rules

- Skip regions smaller than 80×40px — likely false positives
- Always render at 2x zoom for readable crops
- Padding is configurable — tell the user to increase it if crops are too tight
- If `page.find_tables()` finds nothing on any page, note it in the summary
- If the script errors, fix and re-run — do not stop at first error
- Always save the summary JSON before ending the session

---

## Known Limitations

- `page.find_tables()` works best on tables with visible borders — borderless tables may be missed
- Image-based tables (scanned sections) will not be detected — use `table.md` directly with the image
- Multi-page spanning tables will be cropped as separate images per page
- If crops are still too tight, increase padding from 25 to 40 or 50

---

## Next Step

Feed each detected PNG into the table extraction skill:

```
Read the skill at prompts/table.md and follow the instructions.

Image: OUTPUT_FOLDER/FILENAME_page1_table1.png
Output folder: OUTPUT_FOLDER/results/
Ground truth: (skip if not available)
```
