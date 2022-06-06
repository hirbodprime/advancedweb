from argparse import FileType
import mimetypes
import os
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Define function to download pdf file using template
def download(req):
    return render(req, 'file.html')

def download_file(request, filename=''):
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            try :
                filepath = BASE_DIR + '/filedownload/' + filename
                path = open(filepath, 'rb')
            except (FileNotFoundError , FileExistsError):
            # except FileNotFoundError:
                context = {"f":filename}
                return render(request , "file.html", context)
            mime_type, _ = mimetypes.guess_type(filepath) 
            # Set the return value of the HttpResponse
            response = HttpResponse(path, content_type=mime_type)
            # Set the HTTP header for sending to browser
            response['Content-Disposition'] = "attachment; filename=%s" % filename
            # Return the response value
            return response