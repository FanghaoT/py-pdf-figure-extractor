import fitz
import argparse
import os

if __name__ == '__main__':
    par = argparse.ArgumentParser(description='python pdf figure extractor')
    par.add_argument('--src', type=str)
    par.add_argument('--dst', type=str, default='./',help='output directory')
    args = par.parse_args()

    doc = fitz.open(args.src) #open document
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0] # image object number
            # Create a pixmap from an image contained in PDF doc identified by its xref
            pix = fitz.Pixmap(doc, xref)
            pix.writePNG(os.path.join(args.dst,"p%s-%s.png" % (i, xref)))
            pix = None