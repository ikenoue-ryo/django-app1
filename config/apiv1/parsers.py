import json
import re
from django.conf import settings
from django.http.multipartparser import MultiPartParserError, \
    MultiPartParser as DjangoMultiPartParser
from rest_framework.exceptions import ParseError
from rest_framework.parsers import BaseParser, DataAndFiles


class PostParser(BaseParser):
    """
    Parser for multipart form data, which may include file data.
    """
    media_type = 'multipart/form-data'

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Parses the incoming bytestream as a multipart encoded form,
        and returns a DataAndFiles object.
        `.data` will be a `QueryDict` containing all the form parameters.
        `.files` will be a `QueryDict` containing all the form files.
        """
        parser_context = parser_context or {}
        request = parser_context['request']
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)
        meta = request.META.copy()
        meta['CONTENT_TYPE'] = media_type
        upload_handlers = request.upload_handlers

        try:
            parser = DjangoMultiPartParser(
                meta, stream, upload_handlers, encoding
            )
            data, files = parser.parse()
            data._mutable = True
            r = re.compile(r'tag\[\d+]')
            for key in data.keys():
                if r.match(key):
                    data[key] = json.loads(data[key])
            data._mutable = False
            return DataAndFiles(data, files)
        except MultiPartParserError as exc:
            raise ParseError('Multipart form parse error - %s' % str(exc))
