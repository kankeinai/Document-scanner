Works only for white paper (A4) with more or less constrast background.

– converter.py converts .heic images to .jpg, usage: python converter.py dir_name

– transform.py contains function four_point_transform(image, pts) that apply perspective transformation of the document

– scan.py saves transformed images to the folder "scanned" and creates output.pdf file with all images from your dir_name folder, usage: python converter.py dir_name

