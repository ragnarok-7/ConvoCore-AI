import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

def get_brochures():

    folder = os.path.join(BASE_DIR, "database", "brochures")

    if not os.path.exists(folder):

        return []

    files = os.listdir(folder)

    return files


def get_download_links():

    brochures = get_brochures()

    links = []

    for file in brochures:

        links.append(f"Download: {file}")

    return links