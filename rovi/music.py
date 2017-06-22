# TODO
# How to include multiple parameters with one argument? e.g., include=Moods&include=Stlyes&include=Credits
# Is if not any([<list>]) the best way to check to make sure at least one argument is included in the list?
# How to validate formatid and imagesize parameters?

from .client import RoviClient
from .exceptions import RoviMissingArgumentsException, RoviRestrictedParameterException

import json
import requests

BASE_URL = 'api.rovicorp.com/data/v1.1'
INFO_URL = '/info'
CLASSICALREVIEW_URL = '/classicalreview'
CREDITS_URL = '/credits'
IMAGES_URL = '/images'
MOODS_URL = '/moods'
PRIMARYREVIEW_URL = '/primaryreview'
RELEASES_URL = '/releases'
SIMILIAR_URL = '/similiar'
STYLES_URL = '/styles'
THEMES_URL = '/themes'
TRACKS_URL = '/tracks'
DESCRIPTION_URL = '/description'
PARTS_URL = '/parts'
COMPOSITION_URL = '/composition'
RELEASE_URL = '/release'
PERFORMANCES_URL = '/performances'
APPEARANCES_URL = '/appearances'
REVIEW_URL = '/review'
SAMPLE_URL = '/sample'


class Album(RoviClient):
	'''
	Python Wrapper for Rovi Music API Album collection

	The Album collection presents an assembly of data about albums.
	'''
	def info(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		formatid = kwargs.get('formatid')
		imagecount = kwargs.get('imagecount')
		imageoffset = kwargs.get('imageoffset')
		imagesize = kwargs.get('imagesize')
		imagesort = kwargs.get('imagesort')
		include = kwargs.get('include')

		if not any([album, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: album, albumid, amgclassicalid, amgpopid')

		if any([formatid, imagecount, imageoffset, imagesize, imagesort]) and not (include=='All' or include=='Images'):
			raise RoviMissingArgumentsException('The arguments formatid, imagecount, imageoffset, imagesize, imagesort require the parameter include=All or include=Images')

		if include is not None and include not in ['All', 'ClassicalReview', 'Credits', 'Images', 'Moods', 'PrimaryReview', 'Releases', 'Similar', 'Styles', 'Themes', 'Tracks']:
			raise RoviRestrictedParameterException('The include parameter is restricted to All, ClassicalReview, Credits, Images, Moods, PrimaryReview, Releases, Similar, Styles, Themes, or Tracks')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if formatid is not None:
			payload['formatid'] = formatid

		if imagecount is not None:
			payload['imagecount'] = imagecount

		if imageoffset is not None:
			payload['imageoffset'] = imageoffset

		if imagesize is not None:
			payload['imagesize'] = imagesize

		if imagesort is not None:
			payload['imagesort'] = imagesort

		if include is not None:
			payload['include'] = include

		request_url = self.protocol + BASE_URL + '/album' + INFO_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def classicalreview(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		request_url = self.protocol + BASE_URL + '/album' + CLASSICALREVIEW_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def credits(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + CREDITS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def images(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		formatid = kwargs.get('formatid')
		imagecount = kwargs.get('imagecount')
		imageoffset = kwargs.get('imageoffset')
		imagesize = kwargs.get('imagesize')
		imagesort = kwargs.get('imagesort')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if formatid is not None:
			payload['formatid'] = formatid

		if imagecount is not None:
			payload['imagecount'] = imagecount

		if imageoffset is not None:
			payload['imageoffset'] = imageoffset

		if imagesize is not None:
			payload['imagesize'] = imagesize

		if imagesort is not None:
			payload['imagesort'] = imagesort

		request_url = self.protocol + BASE_URL + '/album' + IMAGES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def moods(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + MOODS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def primaryreview(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		request_url = self.protocol + BASE_URL + '/album' + PRIMARYREVIEW_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def releases(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + RELEASES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def similiar(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + SIMILIAR_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def styles(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		request_url = self.protocol + BASE_URL + '/album' + STYLES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def themes(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + THEMES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def tracks(self, *args, **kwargs):
		album = kwargs.get('album')
		albumid = kwargs.get('albumid')
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if album is not None:
			payload['album'] = album

		if albumid is not None:
			payload['albumid'] = albumid

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/album' + TRACKS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()


class Composition(RoviClient):
	'''
	Python Wrapper for Rovi Music API Composition collection

	The Composition collection brings together the parts, forms, period, key dates, 
	and a detailed background description of classical compositions. 
	A list of album releases that feature a performance of the composition 
	is also available so you can present links and supply more information.
	'''
	def info(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		compositionid = kwargs.get('compositionid')
		include = kwargs.get('include')

		if not any([amgclassicalid, compositionid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, compositionid')
		
		if include is not None and include not in ['All', 'Description', 'Parts', 'Releases']:
			raise RoviRestrictedParameterException('The include parameter is restricted to All, Description, Parts, or Releases')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if compositionid is not None:
			payload['compositionid'] = compositionid

		if include is not None:
			payload['include'] = include

		request_url = self.protocol + BASE_URL + '/composition' + INFO_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def description(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		compositionid = kwargs.get('compositionid')

		if not any([amgclassicalid, compositionid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, compositionid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if compositionid is not None:
			payload['compositionid'] = compositionid

		request_url = self.protocol + BASE_URL + '/composition' + DESCRIPTION_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def parts(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		compositionid = kwargs.get('compositionid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, compositionid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, compositionid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if compositionid is not None:
			payload['compositionid'] = compositionid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/composition' + PARTS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def releases(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		compositionid = kwargs.get('compositionid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, compositionid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, compositionid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if compositionid is not None:
			payload['compositionid'] = compositionid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/composition' + RELEASES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()


class Performance(RoviClient):
	'''
	Python Wrapper for Rovi Music API Performance collection

	The Performance collection brings together information about classical music performances, plus database IDs 
	you can use to request further information about the composer, performers, composition, and album release.
	'''
	def info(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		performanceid = kwargs.get('performanceid')
		include = kwargs.get('include')

		if not any([amgclassicalid, performanceid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, performanceid')
		
		if include is not None and include not in ['All', 'Composition', 'Credits', 'Images', 'Release']:
			raise RoviRestrictedParameterException('The include parameter is restricted to All, Composition, Credits, Images, or Release')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if performanceid is not None:
			payload['performanceid'] = performanceid

		if include is not None:
			payload['include'] = include

		request_url = self.protocol + BASE_URL + '/performance' + INFO_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def composition(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		performanceid = kwargs.get('performanceid')

		if not any([amgclassicalid, performanceid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, performanceid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if performanceid is not None:
			payload['performanceid'] = performanceid

		request_url = self.protocol + BASE_URL + '/performance' + COMPOSITION_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def credits(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		performanceid = kwargs.get('performanceid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, performanceid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, performanceid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if performanceid is not None:
			payload['performanceid'] = performanceid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/performance' + CREDITS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def images(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		performanceid = kwargs.get('performanceid')

		if not any([amgclassicalid, performanceid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, performanceid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if performanceid is not None:
			payload['performanceid'] = performanceid

		request_url = self.protocol + BASE_URL + '/performance' + IMAGES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def release(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		performanceid = kwargs.get('performanceid')

		if not any([amgclassicalid, performanceid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, performanceid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if performanceid is not None:
			payload['performanceid'] = performanceid

		request_url = self.protocol + BASE_URL + '/performance' + RELEASE_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()


class Release(RoviClient):
	'''
	Python Wrapper for Rovi Music API Release collection

	The Release collection presents information about the LPs, CDs, DVDs, cassettes, downloads, and other releases of an 
	album, plus database IDs you can use to request further information about songs, albums, compositions, and performances.
	'''
	def info(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		formatid = kwargs.get('formatid')
		imagecount = kwargs.get('imagecount')
		imageoffset = kwargs.get('imageoffset')
		imagesize = kwargs.get('imagesize')
		imagesort = kwargs.get('imagesort')
		include = kwargs.get('include')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		if any([formatid, imagecount, imageoffset, imagesize, imagesort]) and not (include=='All' or include=='Images'):
			raise RoviMissingArgumentsException('The arguments formatid, imagecount, imageoffset, imagesize, imagesort require the parameter include=All or include=Images')

		if include is not None and include not in ['All', 'ClassicalReview', 'Credits', 'Images', 'Moods', 'Performances', 'PrimaryReview', 'Styles', 'Themes', 'Tracks']:
			raise RoviRestrictedParameterException('The include parameter is restricted to All, ClassicalReview, Credits, Images, Moods, Performances, PrimaryReview, Styles, Themes, or Tracks')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if formatid is not None:
			payload['formatid'] = formatid

		if imagecount is not None:
			payload['imagecount'] = imagecount

		if imageoffset is not None:
			payload['imageoffset'] = imageoffset

		if imagesize is not None:
			payload['imagesize'] = imagesize

		if imagesort is not None:
			payload['imagesort'] = imagesort

		if include is not None:
			payload['include'] = include

		request_url = self.protocol + BASE_URL + '/release' + INFO_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def classicalreview(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		request_url = self.protocol + BASE_URL + '/release' + CLASSICALREVIEW_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def credits(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + CREDITS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def images(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		formatid = kwargs.get('formatid')
		imagecount = kwargs.get('imagecount')
		imageoffset = kwargs.get('imageoffset')
		imagesize = kwargs.get('imagesize')
		imagesort = kwargs.get('imagesort')

		if not any([albumid, albumid, amgclassicalid, amgpopid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: albumid, albumid, amgclassicalid, amgpopid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if formatid is not None:
			payload['formatid'] = formatid

		if imagecount is not None:
			payload['imagecount'] = imagecount

		if imageoffset is not None:
			payload['imageoffset'] = imageoffset

		if imagesize is not None:
			payload['imagesize'] = imagesize

		if imagesort is not None:
			payload['imagesort'] = imagesort

		request_url = self.protocol + BASE_URL + '/release' + IMAGES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def moods(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + MOODS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def performances(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + PERFORMANCES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def primaryreview(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		request_url = self.protocol + BASE_URL + '/release' + PRIMARYREVIEW_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def styles(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + STYLES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def themes(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + THEMES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def tracks(self, *args, **kwargs):
		amgclassicalid = kwargs.get('amgclassicalid')
		amgpopid = kwargs.get('amgpopid')
		eanid = kwargs.get('eanid')
		releaseid = kwargs.get('releaseid')
		upcid = kwargs.get('upcid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicalid, amgpopid, eanid, releaseid, upcid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicalid, amgpopid, eanid, releaseid, or upcid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicalid is not None:
			payload['amgclassicalid'] = amgclassicalid

		if amgpopid is not None:
			payload['amgpopid'] = amgpopid

		if eanid is not None:
			payload['eanid'] = eanid

		if releaseid is not None:
			payload['releaseid'] = releaseid

		if upcid is not None:
			payload['upcid'] = upcid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/release' + TRACKS_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()


class Song(RoviClient):
	'''
	Python Wrapper for Rovi Music API Song collection

	The Song collection presents reviews, samples, and lists of albums that songs appear on.
	'''
	def info(self, *args, **kwargs):
		'''
		Returns basic information about a song plus customized requests for all of the other Song content that is available.
		'''
		track = kwargs.get('track')
		isrcid = kwargs.get('isrcid')
		muzeid = kwargs.get('muzeid')
		trackid = kwargs.get('trackid')
		amgpoptrackid = kwargs.get('amgpoptrackid')
		amgclassicaltrackid = kwargs.get('amgclassicaltrackid')
		artist = kwargs.get('artist')
		include = kwargs.get('include')
		priority = kwargs.get('prority')

		if not any([track, isrcid, muzeid, trackid, amgpoptrackid, amgclassicaltrackid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: track, isrcid, muzeid, trackid, amgpoptrackid, amgclassicaltrackid')

		if any([artist, priority]) and track is None:
			raise RoviMissingArgumentsException('The arguments artist and priority require the parameter track')

		if include is not None and include not in ['All', 'Appearances', 'Review', 'Sample']:
			raise RoviRestrictedParameterException('The include parameter is restricted to All, Appearances, Review, or Sample')

		if priority is not None and priority not in ['popularity', 'bestnamematch', 'original']:
			raise RoviRestrictedParameterException('The priority parameter is restricted to popularity, bestnamematch, or original')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if track is not None:
			payload['track'] = track

		if isrcid is not None:
			payload['isrcid'] = isrcid

		if muzeid is not None:
			payload['muzeid'] = muzeid

		if trackid is not None:
			payload['trackid'] = trackid

		if amgpoptrackid is not None:
			payload['amgpoptrackid'] = amgpoptrackid

		if amgclassicaltrackid is not None:
			payload['amgclassicaltrackid'] = amgclassicaltrackid

		if artist is not None:
			payload['artist'] = artist

		if include is not None:
			payload['include'] = include

		if priority is not None:
				payload['priority'] = priority

		request_url = self.protocol + BASE_URL + '/song' + INFO_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def appearances(self, *args, **kwargs):
		'''
		Returns albums and videos that a song appears on.
		'''
		amgclassicaltrackid = kwargs.get('amgclassicaltrackid')
		amgpoptrackid = kwargs.get('amgpoptrackid')
		isrcid = kwargs.get('isrcid')
		muzeid = kwargs.get('muzeid')
		track = kwargs.get('track')
		trackid = kwargs.get('trackid')
		count = kwargs.get('count')
		offset = kwargs.get('offset')

		if not any([amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicaltrackid is not None:
			payload['amgclassicaltrackid'] = amgclassicaltrackid

		if amgpoptrackid is not None:
			payload['amgpoptrackid'] = amgpoptrackid

		if isrcid is not None:
			payload['isrcid'] = isrcid

		if muzeid is not None:
			payload['muzeid'] = muzeid

		if track is not None:
			payload['track'] = track

		if trackid is not None:
			payload['trackid'] = trackid

		if count is not None:
			payload['count'] = count

		if offset is not None:
			payload['offset'] = offset

		request_url = self.protocol + BASE_URL + '/song' + APPEARANCES_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def review(self, *args, **kwargs):
		'''
		Returns the most recent major review of a song.
		'''
		amgclassicaltrackid = kwargs.get('amgclassicaltrackid')
		amgpoptrackid = kwargs.get('amgpoptrackid')
		isrcid = kwargs.get('isrcid')
		muzeid = kwargs.get('muzeid')
		track = kwargs.get('track')
		trackid = kwargs.get('trackid')

		if not any([amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicaltrackid is not None:
			payload['amgclassicaltrackid'] = amgclassicaltrackid

		if amgpoptrackid is not None:
			payload['amgpoptrackid'] = amgpoptrackid

		if isrcid is not None:
			payload['isrcid'] = isrcid

		if muzeid is not None:
			payload['muzeid'] = muzeid

		if track is not None:
			payload['track'] = track

		if trackid is not None:
			payload['trackid'] = trackid

		request_url = self.protocol + BASE_URL + '/song' + REVIEW_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()

	def sample(self, *args, **kwargs):
		'''
		Returns URL to an audio sample of a song.
		'''
		amgclassicaltrackid = kwargs.get('amgclassicaltrackid')
		amgpoptrackid = kwargs.get('amgpoptrackid')
		isrcid = kwargs.get('isrcid')
		muzeid = kwargs.get('muzeid')
		track = kwargs.get('track')
		trackid = kwargs.get('trackid')

		if not any([amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid]):
			raise RoviMissingArgumentsException('The request must contain at least one of these arguments: amgclassicaltrackid, amgpoptrackid, isrcid, muzeid, track, trackid')

		payload = {
			'apikey': self.api_key,
			'sig': self.computesig(self.api_key, self.secret_key),
			'format': self.format,
			'country': self.country,
			'language': self.language,
		}

		if amgclassicaltrackid is not None:
			payload['amgclassicaltrackid'] = amgclassicaltrackid

		if amgpoptrackid is not None:
			payload['amgpoptrackid'] = amgpoptrackid

		if isrcid is not None:
			payload['isrcid'] = isrcid

		if muzeid is not None:
			payload['muzeid'] = muzeid

		if track is not None:
			payload['track'] = track

		if trackid is not None:
			payload['trackid'] = trackid

		request_url = self.protocol + BASE_URL + '/song' + SAMPLE_URL
		r = self.session.get(request_url, params=payload)
		r.raise_for_status()
		return r.json()




