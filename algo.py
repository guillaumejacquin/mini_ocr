import os
import sys
import pdftotext
import fitz
import bios
from getPosition import *

def mini_ocr(file):
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
        text = "\n\n".join(pdf)

    return text

def get_words(string, element):
    array_with_elements = []

    some_list = string.split()
    array_with_elements = ([x for x in some_list if element in x])
    return (array_with_elements)


def create_template(file_given, texte):
    with fitz.open(file_given) as doc:
        # POUR CREER UN NOUVEAU TEMPLATE, ON DONNE LE MOT IL PREND LE CARRE QU IL VA ENSUITE STOCKER DANS LE .YML
        for page in doc:
            # SEARCH
            text = texte
            text_instances_a = page.searchFor(text)
            # HIGHLIGHT
            text_instances_a = [
                num for num in text_instances_a[0] if isinstance(num, (int, float))]


def veriftemplates(file_given):

    pdf_txt = mini_ocr(file_given)
    template = False

    for root, dirs, files in os.walk("templates"):
        for file in files:
            maybefile = (os.path.join(root, file))

            my_dict = bios.read(maybefile)

            # print((all(my_dict['keywords'] in pdf_txt)))
            lefameux = (my_dict['keywords'])

            template = (all([w in pdf_txt for w in lefameux]))
            if template:
                break

    if not template:
        print("aucun modele trouvé, nous vous conseillons d'en créer un")
        sys.exit()

    with fitz.open(file_given) as doc:

        try:
            reference_position = my_dict['Référence'].split(",")
            RevisionPosition = my_dict['Révision'].split(",")
            TypeDocumentPosition = my_dict['Type de Document'].split(",")
            EtatDocumentPosition = my_dict['Etat du Document'].split(",")
            DesignDocPosition = my_dict['Désignation de doc'].split(",")

            for page in doc:
                Result_reference = page.get_textbox(reference_position)
                Revision = page.get_textbox(RevisionPosition)
                TypeDocument = page.get_textbox(TypeDocumentPosition)
                EtatDocument = page.get_textbox(EtatDocumentPosition)
                DesignDoc = page.get_textbox(DesignDocPosition)

        except :
            reference_position = my_dict['Référence'].split(",")
            RevisionPosition = my_dict['Révision'].split(",")
            TypeDocumentPosition = my_dict['Type de Document'].split(",")
            EtatDocumentPosition = my_dict['Etat du Document'].split(",")

            for page in doc:
                Result_reference = page.get_textbox(reference_position)
                Revision = page.get_textbox(RevisionPosition)
                TypeDocument = page.get_textbox(TypeDocumentPosition)
                EtatDocument = page.get_textbox(EtatDocumentPosition)
    try:
        data = {
            "Reference": Result_reference,
            "Revision": Revision,
            "TypeDocument": TypeDocument,
            "EtatDocument": EtatDocument,
            "désignation de doc": DesignDoc
        }
    except:
        data = {
            "Reference": Result_reference,
            "Revision": Revision,
            "TypeDocument": TypeDocument,
            "EtatDocument": EtatDocument
        }

        # print(pdf_txt)

    # Nouveau = get_words(pdf_txt, Revision)

    # for i in Nouveau:
    #     position_i = float((getPostionOneELement(i, file_given)))
    #     print(position_i)
    #     print(RevisionPosition)
    #     print(type(RevisionPosition[0]))
    #     RevisionPosition[0] = float(RevisionPosition[0])
    #     if (position_i[0] > RevisionPosition[0] and position_i[2]< RevisionPosition[2] and position_i[1] > RevisionPosition[1]and position_i[3] < RevisionPosition[3]):
    #         print("pouet")
    return data


def main():
    # create_template("test1.pdf", "Synapture")
    print(veriftemplates("test1.pdf"))


main()
