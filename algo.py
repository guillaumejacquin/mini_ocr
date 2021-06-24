import pdftotext
import fitz
import yaml
import os
import bios
import json


def mini_ocr(file):
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
        text = "\n\n".join(pdf)

    return(text)


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

    Result_reference = []
    Révision = []
    TypeDocument = []
    EtatDocument = []

    pdf_txt = mini_ocr(file_given)
    template = False

    for root, dirs, files in os.walk("templates"):
        for file in files:
            maybefile = (os.path.join(root, file))

            with open(maybefile, "rb") as f:

                my_dict = bios.read(maybefile)

                # print((all(my_dict['keywords'] in pdf_txt)))
                lefameux = (my_dict['keywords'])

                template = (all([w in pdf_txt for w in lefameux]))
                if template:
                    break

    if not template:
        print("aucun modele trouvé, nous vous conseillons d'en créer un")
        exit()

    with fitz.open(file_given) as doc:
        ReferencePosition = my_dict['Référence'].split(",")
        RevisionPosition = my_dict['Révision'].split(",")
        TypeDocumentPosition = my_dict['Type de Document'].split(",")
        EtatDocumentPosition = my_dict['Etat du Document'].split(",")

        for page in doc:
            Result_reference = page.get_textbox(ReferencePosition)
            Revision = page.get_textbox(RevisionPosition)
            TypeDocument = page.get_textbox(TypeDocumentPosition)
            EtatDocument = page.get_textbox(EtatDocumentPosition)

    print("reference = ", Result_reference)
    print("Revision = ", Revision)
    print("Type document =", TypeDocument)
    print("Etat document =", EtatDocument)


    with open('data.json', 'w') as f:
        json.dump(Result_reference, f)
        json.dump(Revision, f)
        json.dump(TypeDocument, f)
        json.dump(EtatDocument, f)

    data = {
    "Reference" : Result_reference,
    "Revision" : Revision,
    "TypeDocument" : TypeDocument,
    "EtatDocument" : EtatDocument    
    }

        
    # with open('data.json', 'w') as outfile:
    #     oui = json.dump(data, outfile)
    return(data)
def main():
    # create_template("test1.pdf", "Synapture")
    veriftemplates("test2.pdf")


main()
