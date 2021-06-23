
import fitz

def main():
## READ IN PDF
    doc = fitz.open("test2.pdf")

    for page in doc:
        ## SEARCH
        text = "BPA"
        text_instances = page.searchFor(text)
        
        print(text_instances[0].bottom_right)
        print(text_instances[0].bottom_left)
        print(text_instances[0].top_right)
        print(text_instances[0].top_left)

 

        ## HIGHLIGHT
        list_2 = [num for num in text_instances[0] if isinstance(num, (int,float))]
        print(list_2)

        # for inst in text_instances:
        #     print(inst)
        #     highlight = page.addHighlightAnnot(inst)
        #     print(inst)
        #     highlight.update()

        print(page.get_textbox(list_2))
        print(text_instances)
    doc.save("i.pdf", garbage=4, deflate=True, clean=True)

main()