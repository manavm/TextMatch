# -*- coding: utf-8 -*-
import unirest
from unidecode import unidecode

class Match(object):

	currMultiDict = {}
	emailKeyDict = {}
	emailMultiDict = {}
	currDict = {}
	emailDict = {}
	score = 0
	grade = 0
	currFile = ""
	emailFile = ""


	def __init__(self, curr, email):
		self.currFile = curr
		self.emailFile = email

	def readFile(self, file):
		fileObj = open(file, "r+")
		string = fileObj.read()
		return string

	def run(self):
		self.curr = unidecode(self.readFile(self.currFile))
		self.email = self.readFile(self.emailFile)
		self.currKeyDict = self.extractKeywords(self.curr)["keyword_extractor"]["keywords"]
		self.emailKeyDict = self.extractKeywords(self.email)["keyword_extractor"]["keywords"]
		self.emailMultiDict = self.extractKeyPhrases(self.email)["multiword_terms"]
		self.getCurrTopics(self.currKeyDict)
		self.getEmailTopics(self.emailKeyDict, self.emailMultiDict)
		self.finalScore(self.currDict, self.emailDict)

	def extractKeywords(self, input):
		string = self.convertToUrl(input)
		response = unirest.get("https://cilenisapi.p.mashape.com/keyword_extractor?lang_input=en&text=" + string + "",
		  headers={
		    "X-Mashape-Key": "r61UivN0bLmshiVlIxwVjgtA1Rsqp1ZrzBPjsnkCWpNj1gM4B7"
		  }
		)
		output = response.body
		return output

	def extractKeyPhrases(self, input):
		string = self.convertToUrl(input)
		response = unirest.get("https://cilenisapi.p.mashape.com/multiword_extractor?lang_input=en&text=" + string + "",
		  headers={
		    "X-Mashape-Key": "r61UivN0bLmshiVlIxwVjgtA1Rsqp1ZrzBPjsnkCWpNj1gM4B7"
		  }
		)
		output = response.body
		return output

	def convertToUrl(self, inputTxt):
	    strList = inputTxt.split()
	    output=strList[0]
	    for word in strList[1:]:
	        output = output + "+" + word
	    return output

	def getCurrTopics(self, currKeyDict):
		currDict = {}
		# print self.currKeyDict
		highScore = self.currKeyDict[0]["term"]
		count = 11
		local = 1
		for obj in self.currKeyDict[:10]:
			print obj["term"].lower()
			if obj["score"] == highScore:
				local += 1
				currDict[obj["term"].lower()] = count
			if obj["score"] < highScore:
				currDict[obj["term"].lower()] = count - local
				local = 1
				count = count - local
		print currDict
		self.currDict = currDict

	def getEmailTopics(self, emailKeyDict, emailMultiDict):
		emailDict = {}
		count = 10
		i = 0
		j = 0
		while count >= 0:
			if count % 2 == 0:
				emailDict[self.emailMultiDict[i]["multiword_term"].lower()] = count
				i += 1
				count -= 1
			else:
				emailDict[self.emailKeyDict[j]["term"].lower()] = count
				j += 1
				count -= 1
		print emailDict
		self.emailDict = emailDict

	def finalScore(self, currDict, emailDict):
		score = 0
		for i in self.currDict.keys():
			if i in self.emailDict:
				score += self.currDict[i] + self.emailDict[i]
				print i
				print score
		self.score = score
		grade = score % 25
		if grade == 0:
			grade += 1
		self.grade = grade

if __name__ == "__main__":
	obj = Match(curr = "curr.txt", email = "email1.txt")
	obj.run()

