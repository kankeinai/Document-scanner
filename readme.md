Works only for white paper (A4) with more or less constrast background.

– converter.py converts .heic images to .jpg, usage: python converter.py dir_name

– transform.py contains function four_point_transform(image, pts) that applies perspective transformation of the document

– scan.py saves transformed images to the folder "scanned" and creates output.pdf file with all images from your dir_name folder, usage: python scan.py dir_name

Before usage create virtual environment and install needed libraries: img2pdf, imutils, pyheif (for converter), cv2, skimage

Example:
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/56974757/111685728-7796cf00-8852-11eb-8546-7abc108bd1dd.png">
