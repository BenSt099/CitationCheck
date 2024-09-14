from re import sub
from re import split
from re import search
from re import sub

def clear_title(title_raw):
    title_raw = title_raw.strip()
    title_raw = title_raw[:-1]
    x = split(r"^title\s*=\s*", title_raw)
    title_cleaned = x[1]
    title_cleaned = title_cleaned[1:]
    return title_cleaned

def clear_doi(doi_raw):
    doi_raw  = doi_raw.strip()
    doi_raw = doi_raw[:-1]
    x = split(r"doi\s*=\s*", doi_raw)
    doi_cleaned = x[1]
    doi_cleaned = doi_cleaned[1:]
    if "https://doi.org/" in doi_cleaned:
        doi_cleaned = sub("https://doi.org/", "", doi_cleaned)     
    return doi_cleaned

def process_bibtex_file(bibfile):
    content = ""
    with open(bibfile, mode="r", encoding="utf-8") as bib_file:
        content = bib_file.read()
    dict_ret = []
    for x in content.split("@"):
        x = x.strip()
        x = x[:-1]
        entry = []
        for line in x.split('\n'):
            line = line.strip()
            if line.endswith(','):
                line = line[:-1]

            if search(r"^[a-zA-Z]+\{.+$", line):                
                x = split(r"\{", line)
                entry.append(x[1].strip())

            if search(r"^title\s*=\s*.+$", line):
                entry.append(clear_title(line))
            
            if search(r"doi\s*=\s*.+", line):
                entry.append(clear_doi(line))

        if entry == []:
            continue
        dict_ret.append(entry)
    return dict_ret