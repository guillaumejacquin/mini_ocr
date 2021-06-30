
import fitz

folder = "/templates/"

#POur avoir les 4 elements d'un coup (positions)
def get_position_templates(reference, revisio, type, etat):
## READ IN PDF
    doc = fitz.open("test2.pdf")

    for page in doc:
        Reference = ""

        ## SEARCH

        Result_reference = reference
        text_instances = page.searchFor(Result_reference)
        ResultPosition = [num for num in text_instances[0] if isinstance(num, (int,float))]      #FAIRE 4 FOIS CA plz
        Result_reference = str(ResultPosition[0]) + ', ' + str(ResultPosition[1]) + ', ' + str(ResultPosition[2]) + ', ' + str(ResultPosition[3])


        TypeDocument = type
        text_instances = page.searchFor(TypeDocument)
        TypeDocumentPosition = [num for num in text_instances[0] if isinstance(num, (int,float))]      #FAIRE 4 FOIS CA plz
        TypeDocument = str(TypeDocumentPosition[0]) + ', ' + str(TypeDocumentPosition[1]) + ', ' + str(TypeDocumentPosition[2]) + ', ' + str(TypeDocumentPosition[3])


        EtatDocument = etat
        text_instances = page.searchFor(EtatDocument)
        TypeDocumentPosition = [num for num in text_instances[0] if isinstance(num, (int,float))]      #FAIRE 4 FOIS CA plz
        EtatDocument = str(TypeDocumentPosition[0]) + ', ' + str(TypeDocumentPosition[1]) + ', ' + str(TypeDocumentPosition[2]) + ', ' + str(TypeDocumentPosition[3])
        

        Revision = revisio
        text_instances = page.searchFor(Revision)
        TypeDocumentPosition = [num for num in text_instances[0] if isinstance(num, (int,float))]      #FAIRE 4 FOIS CA plz
        Revision = str(TypeDocumentPosition[0]) + ', ' + str(TypeDocumentPosition[1]) + ', ' + str(TypeDocumentPosition[2]) + ', ' + str(TypeDocumentPosition[3])

        data = {
        "Reference" : Result_reference,
        "Revision" : Revision,
        "TypeDocument" : TypeDocument,
        "EtatDocument" : EtatDocument    
        }

    print(data)
    # doc.save("i.pdf", garbage=4, deflate=True, clean=True)





#Pour avoir la position a directement rentrer sur le.yaml
def getPostionOneELement(reference, pdf):
## READ IN PDF
    doc = fitz.open(pdf)

    for page in doc:
        Reference = ""

        ## SEARCH

        Result_reference = reference
        text_instances = page.searchFor(Result_reference)
        ResultPosition = [num for num in text_instances[0] if isinstance(num, (int,float))]      #FAIRE 4 FOIS CA plz
        Result_reference = str(ResultPosition[0]) + ', ' + str(ResultPosition[1]) + ', ' + str(ResultPosition[2]) + ', ' + str(ResultPosition[3])


    return(Result_reference)
    # doc.save("i.pdf", garbage=4, deflate=True, clean=True)

# get_position_templates("BPA","BPA", "BPA", "BPA")

reference = getPostionOneELement("BPE", "test1.pdf")
print(reference)