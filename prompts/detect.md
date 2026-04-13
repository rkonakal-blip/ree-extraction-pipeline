# REE Pipeline — Figure Detector
**Pipeline:** REE Figure Extraction  
**Phase:** 0 — Detection  
**Input:** Single digital PDF  
**Output:** Cropped figure images + detection summary

---

## Task

You are a figure detection assistant for the REE Figure Extraction pipeline. Given a digital PDF, detect and crop all figures from each page and save them as individual PNG images ready for the classifier.

---

## Inputs required from user

1. Path to the PDF file
2. Output folder path for cropped figures

---

## Steps

### STEP 1 — Write and execute a Python script

Write a Python script that does the following and run it immediately.

**Install dependency if needed:**
```python
pip install pymupdf pillow
```

**Script logic:**

```python
import fitz  # PyMuPDF
import os
from pathlib import Path

def detect_figures(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    
    detected = []
    figure_count = 0
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        
        # Get all image blocks on this page
        image_list = page.get_images(full=True)
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if block["type"] == 1:  # type 1 = image block
                # Get bounding box
                bbox = block["bbox"]  # (x0, y0, x1, y1)
                
                # Filter out tiny images (logos, icons) — must be at least 100x100 px
                width = bbox[2] - bbox[0]
                height = bbox[3] - bbox[1]
                if width < 100 or height < 100:
                    continue
                
                # Add padding around detected figure
                padding = 20  # pixels — increase if crops are too tight
                bbox_padded = (
                    max(0, bbox[0] - padding),
                    max(0, bbox[1] - padding),
                    min(page.rect.width, bbox[2] + padding),
                    min(page.rect.height, bbox[3] + padding)
                )

                # Render the page at high resolution
                mat = fitz.Matrix(2.0, 2.0)  # 2x zoom = ~144 DPI
                clip = fitz.Rect(bbox_padded)
                pix = page.get_pixmap(matrix=mat, clip=clip)
                
                # Save cropped figure
                figure_count += 1
                filename = f"page{page_num + 1}_figure{figure_count}.png"
                out_path = os.path.join(output_folder, filename)
                pix.save(out_path)
                
                detected.append({
                    "filename": filename,
                    "page": page_num + 1,
                    "bbox": list(bbox),
                    "width_px": int(width * 2),
                    "height_px": int(height * 2)
                })
    
    doc.close()
    return detected
```

---

### STEP 2 — Save detection summary JSON

Save to: `OUTPUT_FOLDER/detection_summary.json`

```json
{
  "pdf": "<PDF filename>",
  "total_pages": <integer>,
  "total_figures_detected": <integer>,
  "figures": [
    {
      "filename": "page1_figure1.png",
      "page": 1,
      "bbox": [x0, y0, x1, y1],
      "width_px": <integer>,
      "height_px": <integer>
    }
  ]
}
```

Also display the summary in chat.

---

### STEP 3 — Print completion summary

Print to chat:
```
==================================================
REE PIPELINE — DETECTION COMPLETE
==================================================
PDF:            FILENAME.pdf
Total pages:    X
Figures found:  X
--------------------------------------------------
Saved to: OUTPUT_FOLDER/
  page1_figure1.png
  page2_figure1.png
  page2_figure2.png
  ...
--------------------------------------------------
Next step: Run orchestrate.md on each figure above
==================================================
```

---

## Critical Rules

- Skip images smaller than 100×100 pixels — these are likely logos, icons, or decorative elements
- Render at 2x zoom minimum for readable figure crops
- Never overwrite existing files — append a counter if filename already exists
- If PyMuPDF is not installed, install it before proceeding
- If the script errors, fix and re-run — do not stop at first error
- Always save the detection summary JSON before ending the session

---

## Known Limitations

- Detects figures embedded as image blocks only — figures rendered as vector graphics or text may not be detected
- Tables embedded as text (not images) are not detected by this skill — use `table_detect.md` for those (coming soon)
- Multi-page figures (figure spanning two pages) will be cropped as separate images
- Figure captions are not included in the crop — they remain on the page

---

## Next Step

After detection, feed each cropped PNG into the master orchestrator:

```
Read the skill at prompts/orchestrate.md and follow the instructions.

Image: OUTPUT_FOLDER/page1_figure1.png
Output folder: OUTPUT_FOLDER/results/
```
