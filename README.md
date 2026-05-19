# Quarto Article Template

A Quarto template for academic articles with a custom PDF layout using XeLaTeX and KOMA-Script.

## Features

- Custom title block, abstract, and author block for PDF
- Libertinus Serif (body) + Source Sans 3 (headings, captions)
- Alternating running headers
- Word output via `docx: default`
- Single place to update title and subtitle (YAML front matter)

## Requirements

- [Quarto](https://quarto.org)
- XeLaTeX (via TeX Live or MacTeX)
- Python 3 (for the `center-images.py` post-render script)

## Structure

```
manuscript/        ← compile from here (quarto render article.qmd)
  article.qmd      ← main document
  _quarto.yml      ← output settings
  preamble.tex     ← LaTeX layout
  fonts/           ← embedded fonts (Libertinus + Source Sans 3)
references/        ← .bib and .csl files
figures/           ← images used in the article
drafts/            ← raw drafts (not published)
notes/             ← personal notes (not published)
```

## Usage

1. Clone or use this template to create a new repository.
2. Edit `manuscript/article.qmd`:
   - Set `title` and `subtitle` in the YAML front matter.
   - Replace author name, affiliation, and ORCID.
   - Replace abstract and keywords.
   - Write your article.
3. Add your `.bib` file to `references/` and update the `bibliography` path in the YAML.
4. Add your `.csl` file to `references/` and update the `csl` path in the YAML.
5. Render from inside the `manuscript/` folder:
   ```
   quarto render article.qmd
   ```

## Notes

- `\setheaderauthor` in `preamble.tex` must be updated with the author name for correct running headers.
- The `center-images.py` post-render script centres figures in the Word output. It can be removed from `_quarto.yml` if not needed.
