# python broken class object

import requests;
import re;

#Broken URL checker class 
class URLC:
	# defualt constructor
	def __init__(self, config):
		# set default variable values
		self.URL_Map = {}
		self.URLListLength = -1
		
		# set configurations
		self.setURL_List(config["URL_List"])
		self.setRegularExpressions(config["regExpressions"])
		self.setReqHeaders(config["headers"])
		self.setURLsToSkip(config["URLsToSkip"])
		
	# URL List functions
	def setURL_List(self, *newURL_List):
		self.URL_List = newURL_List[0]
		self.URLListLength = len(self.URL_List)
	
	# return URL list 
	def getURL_List(self):
		return self.URL_List
	
	# return url with passed index from URL List
	def getURLFromList(self, index):
		return self.URL_List[index]
		
	# adds new url to URL list 
	# increments URL list length attribute
	def addToURLList(self, newURL):
		self.URL_List.append(newURL)
		self.URLListLength += 1
	
	# return length of URL list 
	def getURLListLength(self):
		return self.URLListLength
	
	# regular expression functions
	
	# set list of regular expressions
	def setRegularExpressions(self, *newRegExps):
		self.regExpressions = newRegExps[0]
	
	# return list of regular expressions used by checker
	def getRegularExpressions(self):
		return self.regExpressions
		
	# sets request headers 
	def setReqHeaders(self, newHeaders):
		self.reqHeaders = newHeaders
		
	# return request headers 
	def getReqHeaders(self):
		return self.reqHeaders
		
	# sets URL list of urls for URLChecker to skip
	def setURLsToSkip(self, newUrlsToSkip):
		self.URLsToSkip = newUrlsToSkip
	
	# returns list of URLs for URLChecker to skip
	def getURLsToSkip(self):
		return self.URLsToSkip
	
	# returns true if passed URL is of the URLs to skip list 
	def urlToSkip(self, url):
		for skipURL in self.URLsToSkip:
			if skipURL in url:
				return True
		
		return False
		
	# Overwrites URL Map 
	def setURLMap(self, newURLMap):
		self.URL_Map = newURLMap
		
	# returns URL Map 
	def getURLMap(self):
		return self.URL_Map
	
	# add to url and status from request to URL map 
	def addToURLMap(self, newURL, status):
		self.URL_Map[newURL] = status
	
	# remove url from URL Map 
	# return true if found, return false if not 
	def removeFromURLMap(self, url):
		if url in self.URL_Map:
			del self.URL_Map[url]
			return true
		
		return false
	
	# returns true if passed url is mapped, false if not 
	def URLMapped(self, url):
		return url in self.URL_Map
		
	# Request URL content via http(s) request
	# Return status code and content in dict/JSON object
	def requestURL(self, url):
		responseInfo = {"statusCode": -1, "content": None}
		
		try:
			response = requests.get(url, headers=self.reqHeaders)
			responseInfo["statusCode"] = response.status_code
			responseInfo["content"] = response.content
		except Exception as e:
			responseInfo = {"statusCode": -1, "content": None}
		
		return responseInfo
	
	# formats passed url for subsequent http request
	def formatURL(self, url):
		
		# if url starts with '//'
		if url.startswith("//"):
			# append "https" to beginning of url
			url = "https:" + url
		# if url does not start with http
		elif not url.startswith("http"):
			# if url does not start with "/"
			if not url.startswith("/"):
				# append "/" to beginning of url 
				url = "/" + url
			
			# append domain to beginning or url 
			url = self.getURLFromList(0) + url
			
		# remove all characters after trailing '#' character 
		if "#" in url:
			url = url[:url.find("#")]
			
		return url
	
	# Using list of regular expressions, parse any additional linkes from passed content
	def parseAdditionalLinks(self, content):
		# list of found URLs 
		foundURLs = []
		
		# for each regular expression in current URLChecker instance
		for reg_exp in self.regExpressions:
			# check for all matches in passed content
			# store resulting array in tmp_arr variable
			tmp_arr = re.findall(reg_exp, str(content))
			
			# for each found URL/ regex match
			for foundURL in tmp_arr:
				# if url is not on the URL skip list 
				if not self.urlToSkip(foundURL):
					# add url to found urls list 
					foundURLs.append(self.formatURL(foundURL))
					
		# return found urls		
		return foundURLs
		
		
		
	