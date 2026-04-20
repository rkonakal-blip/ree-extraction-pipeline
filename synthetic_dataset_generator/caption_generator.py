import random
from config import CAPTION_STYLES, CAPTION_WEIGHTS, CAPTION_LENGTH_RANGE, REE_WORD_BANK


def generate_caption(figure_id, caption_style=None):
    """Return (style_key, full_caption_text).

    style_key is the raw style string from CAPTION_STYLES (e.g. 'Fig. N.').
    full_caption_text has 'N' replaced with the actual figure_id number.
    """
    if caption_style is None:
        caption_style = random.choices(CAPTION_STYLES, weights=CAPTION_WEIGHTS, k=1)[0]

    n_words = random.randint(*CAPTION_LENGTH_RANGE)
    words = random.choices(REE_WORD_BANK, k=n_words)
    body = " ".join(words) + "."

    if caption_style == "none":
        return "none", ""

    prefix = caption_style.replace("N", str(figure_id))
    full = f"{prefix} {body}"
    return caption_style, full
