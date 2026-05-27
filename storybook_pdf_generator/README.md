# Multi-page Watercolor Storybook PDF Generator

This project generates an 8-page beginner-friendly educational booklet:
**The Story of Ghrelin and Leptin**.

## Features
- Creates structured page outline and beginner-friendly page text.
- Stores page-by-page illustration prompts in a consistent watercolor style.
- Uses programmatic page composition so text stays crisp and readable.
- Produces decorative watercolor-style page art placeholders per page.
- Exports a print-friendly multi-page PDF.

## Project Structure

```
storybook_pdf_generator/
  main.py
  content/
    page_outline.json
    page_text.md
    illustration_prompts.md
  assets/
    generated_images/
  output/
    story_of_ghrelin_and_leptin.pdf
  requirements.txt
  README.md
```

## Run

```bash
cd storybook_pdf_generator
python main.py
```

## Outputs
- `output/story_of_ghrelin_and_leptin.pdf`
- `assets/generated_images/page_01_art.txt` ... `page_08_art.txt`
- content files in `content/`

## Notes
- The generator is implemented with a no-external-dependencies PDF pipeline so it runs reliably in restricted environments.
- If you want to extend this with API-based image generation, you can add an image client and feed generated assets into the same page layout workflow.
