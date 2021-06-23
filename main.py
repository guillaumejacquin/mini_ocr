import pdftotext
import fitz
import yaml
import os
import bios

def mini_ocr(file):
    with open(file, "rb") as f:
        pdf = pdftotext.PDF(f)
        text = "\n\n".join(pdf)

    return(text)
    

def create_template(file_given, texte):
    with fitz.open(file_given) as doc:
        #POUR CREER UN NOUVEAU TEMPLATE, ON DONNE LE MOT IL PREND LE CARRE QU IL VA ENSUITE STOCKER DANS LE .YML
        for page in doc:
            ## SEARCH
            text = texte
            text_instances_a = page.searchFor(text)
            ## HIGHLIGHT
            text_instances_a = [num for num in text_instances_a[0] if isinstance(num, (int,float))]




def veriftemplates(file_given):
    
    Result_reference = []
    Révision = []
    TypeDocument = []
    EtatDocument = []

    pdf_txt = mini_ocr(file_given)
    template = False

    for root, dirs, files in os.walk("templates"):
        for file in files:
            if(template == True):
                break
            else:
                    maybefile = (os.path.join(root, file))

                    with open(maybefile, "rb") as f:

                
                        my_dict = bios.read(maybefile)
                        
                        # print((all(my_dict['keywords'] in pdf_txt)))
                        lefameux = (my_dict['keywords'])
                        

                        template = (all([w in pdf_txt for w in lefameux]))



        
        if not template:
            print("aucun modele trouvé, nous vous conseillons d'en créer un")

        else:
            with fitz.open(file_given) as doc:
                # #POUR CREER UN NOUVEAU TEMPLATE, ON DONNE LE MOT IL PREND LE CARRE QU IL VA ENSUITE STOCKER DANS LE .YML
                # for page in doc:
                #     ## SEARCH
                #     text = "Synapture"
                #     text_instances_a = page.searchFor(text)
                #     ## HIGHLIGHT
                #     text_instances_a = [num for num in text_instances_a[0] if isinstance(num, (int,float))]


                ReferencePosition = my_dict['Référence']
                ReferencePosition = ReferencePosition.split(",")

                RevisionPosition = my_dict['Révision']
                RevisionPosition = RevisionPosition.split(",")


                TypeDocumentPosition = my_dict['Type de Document']
                TypeDocumentPosition = TypeDocumentPosition.split(",")

                EtatDocumentPosition = my_dict['Etat du Document']
                EtatDocumentPosition = EtatDocumentPosition.split(",")



                for page in doc:
                    Result_reference = page.get_textbox(ReferencePosition)
                    Revision = page.get_textbox(RevisionPosition)
                    TypeDocument = page.get_textbox(TypeDocumentPosition)
                    EtatDocument = page.get_textbox(EtatDocumentPosition)


               


    print("reference = ", Result_reference)
    print("Revision = ", Revision)
    print("Type document =", TypeDocument)
    print("Etat document =", EtatDocument)    

def main():
    create_template("test1.pdf", "Synapture")
    veriftemplates("test1.pdf")

main()