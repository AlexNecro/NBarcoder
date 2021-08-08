from pdf2image import convert_from_path, convert_from_bytes, pdfinfo_from_path, pdfinfo_from_bytes


def get_page_filename(filename, pagenum):
    page = get_page(filename, pagenum)
    newfilename = filename + "_" + str(pagenum) + ".png"
    page.save(newfilename, "PNG")
    return newfilename


def get_page(filename, pagenum):
    pages = convert_from_path(filename, dpi=300, first_page=pagenum, last_page=pagenum)
    return pages[0]


def get_pdfinfo_fromfiles(filenames):
    result = []
    for filename in filenames:
        print(filename)
        info = pdfinfo_from_path(filename)
        result.append(info)
    return result
