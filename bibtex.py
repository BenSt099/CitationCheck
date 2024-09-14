import re

def clear_title(title_raw):
    title_raw = title_raw.strip()
    title_raw = title_raw[:-1]
    x = re.split(r"^title\s*=\s*", title_raw)
    title_cleaned = x[1]
    title_cleaned = title_cleaned[1:]
    return title_cleaned

def clear_doi(doi_raw):
    doi_raw  = doi_raw.strip()
    doi_raw = doi_raw[:-1]
    x = re.split(r"doi\s*=\s*", doi_raw)
    doi_cleaned = x[1]
    doi_cleaned = doi_cleaned[1:]
    if "https://doi.org/" in doi_cleaned:
        doi_cleaned = re.sub("https://doi.org/", "", doi_cleaned)     
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

            if re.search(r"^[a-zA-Z]+\{.+$", line):                
                x = re.split(r"\{", line)
                entry.append(x[1].strip())

            if re.search(r"^title\s*=\s*.+$", line):
                entry.append(clear_title(line))
            
            if re.search(r"doi\s*=\s*.+", line):
                entry.append(clear_doi(line))

        if entry == []:
            continue
        dict_ret.append(entry)
    return dict_ret

# aa = process_bibtex_file('refs.bib')
# print(aa)
# print(clear_title("title = {Fractals, fractal dimensions and landscapes - a review}"))
# print(clear_title('title="title"'))

# print(clear_doi(r"doi={https://doi.org/10.1021/ci025584y}"))
# print(clear_doi(r'-doi = {https://doi.org/10.1016/0378-4371(96)00127-6}'))
# print(clear_doi(r'doi="10.1007/978-3-642-61717-1"'))
# print(clear_doi(r'-doi="10.1007/978-3-642-61717-1"'))