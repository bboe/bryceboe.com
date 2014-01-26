Title: Submitting Binaries to VirusTotal
Date: 2010-09-01 01:12
Category: all
Tags: python, security
Slug: submitting-binaries-to-virustotal

[VirusTotal][] is a web service that essentially performs a virus scan
of an uploaded file, or url against many of the top virus scanners ([see
full list][]). I recently needed to submit over 100 binaries to
VirusTotal, and being a computer scientist I knew this task, like many
other things I do, could be perfectly automated. I was thrilled to see
that VirusTotal provides both a simple [API][] as well as some python
code examples demonstrating the file submission and report checking
process.

Two days ago (2010/09/30) I attempted to run their file upload and scan
example when I encountered some server errors. I quickly contacted
VirusTotal via email to which I received a reply from Emiliano who
informed me he corrected the issues on their end. Thanks Emiliano!
Meanwhile I wrote a fairly simple, self contained python script which
retrieves a VirusTotal report for a given binary, uploading the file if
necessary. The following script is loosely based off the API examples,
and contains modified code from [this snippet][] that was already
required to run the scan file example.

~~~~ {lang="python" line="1"}
#!/usr/bin/env python
import hashlib, httplib, mimetypes, os, pprint, simplejson, sys, urlparse

DEFAULT_TYPE = 'application/octet-stream'

REPORT_URL = 'https://www.virustotal.com/api/get_file_report.json'
SCAN_URL = 'https://www.virustotal.com/api/scan_file.json'

API_KEY = 'YOUR KEY HERE'

# The following function is modified from the snippet at:
# http://code.activestate.com/recipes/146306/
def encode_multipart_formdata(fields, files=()):
    """
    fields is a dictionary of name to value for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be
    uploaded as files.
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for key, value in fields.items():
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' %
                 (key, filename))
        content_type = mimetypes.guess_type(filename)[0] or DEFAULT_TYPE
        L.append('Content-Type: %s' % content_type)
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body

def post_multipart(url, fields, files=()):
    """
    url is the full to send the post request to.
    fields is a dictionary of name to value for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be
    uploaded as files.
    Return body of http response.
    """
    content_type, data = encode_multipart_formdata(fields, files)
    url_parts = urlparse.urlparse(url)
    if url_parts.scheme == 'http':
        h = httplib.HTTPConnection(url_parts.netloc)
    elif url_parts.scheme == 'https':
        h = httplib.HTTPSConnection(url_parts.netloc)
    else:
        raise Exception('Unsupported URL scheme')
    path = urlparse.urlunparse(('', '') + url_parts[2:])
    h.request('POST', path, data, {'content-type':content_type})
    return h.getresponse().read()

def scan_file(filename):
    files = [('file', filename, open(filename, 'rb').read())]
    json = post_multipart(SCAN_URL, {'key':API_KEY}, files)
    return simplejson.loads(json)

def get_report(filename):
    md5sum = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    json = post_multipart(REPORT_URL, {'resource':md5sum, 'key':API_KEY})
    data = simplejson.loads(json)
    if data['result'] != 1:
        print 'Result not found, submitting file.'
        data = scan_file(filename)
        if data['result'] == 1:
            print 'Submit successful.'
            print 'Please wait a few minutes and try again to receive report.'
        else:
            print 'Submit failed.'
            pprint.pprint(data)
    else:
        pprint.pprint(data['report'])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: %s filename' % sys.argv[0]
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print '%s is not a valid file' % filename
        sys.exit(1)

    get_report(filename)
~~~~

Be sure to change the API\_KEY value on line 8 to reflect your
VirusTotal API key. The entire script can be [downloaded here][] to save
you a copy and paste.

  [VirusTotal]: http://www.virustotal.com/
  [see full list]: http://www.virustotal.com/about.html
  [API]: http://www.virustotal.com/advanced.html#publicapi
  [this snippet]: http://code.activestate.com/recipes/146306/
  [downloaded here]: /images/2010/09/virustotal_report.py
