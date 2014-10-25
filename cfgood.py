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
	curr = ""
	email = ""
	currKeyDict = {"keyword_extractor":{"keywords":[{"score":"21920.576886804","tags":"ENTITY","term":"Growth Mindset"},{"score":"15070.3282499389","tags":"N","term":"mentee"},{"score":"13700.2859800596","tags":"A","term":"own"},{"score":"8220.14175862925","tags":"A","term":"hard"},{"score":"6850.11191775954","tags":"V","term":"ve"},{"score":"6850.11191775954","tags":"A","term":"last"},{"score":"5480.08456267145","tags":"ENTITY","term":"Michael Jordan"},{"score":"4110.05969335821","tags":"ENTITY","term":"Tiger Woods"},{"score":"4110.05969335821","tags":"A","term":"innate"},{"score":"3940.69990895797","tags":"N","term":"mindset"},{"score":"2740.03730981307","tags":"A","term":"positive"},{"score":"2740.03730981307","tags":"A","term":"low"},{"score":"2740.03730981307","tags":"A","term":"successful"},{"score":"2740.03730981307","tags":"A","term":"high"},{"score":"2740.03730981307","tags":"A","term":"negative"},{"score":"2740.03730981307","tags":"ENTITY","term":"Ritual"},{"score":"2740.03730981307","tags":"A","term":"specific"},{"score":"1419.22538911675","tags":"N","term":"paragraph"},{"score":"1370.01741202925","tags":"A","term":"important"},{"score":"1370.01741202925","tags":"ENTITY","term":"Malcolm Gladwell"},{"score":"1370.01741202925","tags":"A","term":"magic"},{"score":"1370.01741202925","tags":"ENTITY","term":"Mentor Email Mentee Email Paragraph"},{"score":"1370.01741202925","tags":"A","term":"changeable"},{"score":"1370.01741202925","tags":"A","term":"sure"},{"score":"1370.01741202925","tags":"A","term":"small"},{"score":"1370.01741202925","tags":"ENTITY","term":"Email"},{"score":"1370.01741202925","tags":"ENTITY","term":"Do"},{"score":"1370.01741202925","tags":"A","term":"far"},{"score":"1370.01741202925","tags":"V","term":"s"},{"score":"1370.01741202925","tags":"ENTITY","term":"Growth"},{"score":"1370.01741202925","tags":"ENTITY","term":"Tiger"},{"score":"1370.01741202925","tags":"ENTITY","term":"Outliers"},{"score":"1370.01741202925","tags":"A","term":"accurate"},{"score":"1370.01741202925","tags":"A","term":"key"},{"score":"1370.01741202925","tags":"ENTITY","term":"Fixed Mindset"},{"score":"1370.01741202925","tags":"A","term":"big"},{"score":"1370.01741202925","tags":"A","term":"active"},{"score":"1370.01741202925","tags":"ENTITY","term":"AND"},{"score":"1370.01741202925","tags":"ENTITY","term":"SIGN OFF"},{"score":"1370.01741202925","tags":"A","term":"talented"},{"score":"1370.01741202925","tags":"A","term":"non-academic"},{"score":"1370.01741202925","tags":"N","term":"doesn"},{"score":"1370.01741202925","tags":"ENTITY","term":"Michael"},{"score":"1370.01741202925","tags":"ENTITY","term":"Email Mentor Tip"},{"score":"1370.01741202925","tags":"ENTITY","term":"YOU"},{"score":"776.043967663562","tags":"N","term":"mentor"},{"score":"684.00969059873","tags":"V","term":"emphasize"},{"score":"544.816081691926","tags":"V","term":"practice"},{"score":"414.210702344127","tags":"N","term":"definition"},{"score":"341.006922046109","tags":"N","term":"aptitude"},{"score":"295.210968792463","tags":"N","term":"s"},{"score":"272.406805202228","tags":"V","term":"re"},{"score":"272.406805202228","tags":"V","term":"validate"},{"score":"226.673636677544","tags":"N","term":"sociologist"},{"score":"225.562237153403","tags":"N","term":"success"},{"score":"194.007295764397","tags":"V","term":"restate"},{"score":"182.871671846147","tags":"V","term":"achieve"},{"score":"137.047767966151","tags":"V","term":"bear"},{"score":"135.208755863528","tags":"N","term":"basketball"},{"score":"103.549011780381","tags":"N","term":"tiger"},{"score":"97.6721621560672","tags":"N","term":"golf"},{"score":"94.0439405478117","tags":"N","term":"athlete"},{"score":"86.9464391536927","tags":"N","term":"belief"},{"score":"85.5724329309299","tags":"V","term":"fix"},{"score":"83.7624908741757","tags":"N","term":"goodbye"},{"score":"70.2250348035719","tags":"N","term":"similarity"},{"score":"63.3492133744376","tags":"V","term":"gift"},{"score":"57.6694402444292","tags":"N","term":"psychologist"},{"score":"54.6848015655164","tags":"N","term":"skill"},{"score":"54.4540341361639","tags":"N","term":"celebrity"},{"score":"54.285270163525","tags":"N","term":"hour"},{"score":"45.6313698078377","tags":"N","term":"practice"},{"score":"45.331827972246","tags":"V","term":"clarify"},{"score":"39.6496743038005","tags":"V","term":"define"},{"score":"38.2849153645466","tags":"N","term":"someone"},{"score":"38.000649190493","tags":"N","term":"experience"},{"score":"37.7199338887794","tags":"N","term":"example"},{"score":"37.2257521251461","tags":"N","term":"legend"},{"score":"34.1331616209089","tags":"V","term":"log"},{"score":"32.9429595733976","tags":"N","term":"intelligence"},{"score":"32.6981349390435","tags":"N","term":"conversation"},{"score":"30.3526628990683","tags":"V","term":"use"},{"score":"28.6771253888493","tags":"N","term":"word"},{"score":"28.034370457349","tags":"N","term":"champion"},{"score":"26.6184207540587","tags":"V","term":"wrap"},{"score":"26.0358084036258","tags":"V","term":"empower"},{"score":"25.5058766241783","tags":"N","term":"moment"},{"score":"24.9766755624534","tags":"N","term":"event"},{"score":"24.939212002996","tags":"N","term":"preparation"},{"score":"24.4225884029423","tags":"N","term":"participant"},{"score":"23.9254875125835","tags":"V","term":"motivate"},{"score":"23.4371212239624","tags":"N","term":"effort"},{"score":"19.5429588157173","tags":"V","term":"believe"},{"score":"16.014389466553","tags":"N","term":"life"},{"score":"15.9452693929536","tags":"V","term":"respond"},{"score":"14.7914072092065","tags":"N","term":"musician"},{"score":"14.5905461038988","tags":"N","term":"combination"},{"score":"14.3944847455817","tags":"N","term":"equivalent"},{"score":"13.8334440678613","tags":"V","term":"guarantee"},{"score":"11.9365349701277","tags":"N","term":"person"}],"text":"What is a Growth Mindset? Think about Tiger Woods and Michael Jordan. These two athletes are legends in their sports. How many times have you heard people say, â€œthey were born to play golf /basketball?â€ Do you believe when it comes to achieving success you were either born with the ability and skills to make it or not? There are two ways of looking at this: with a fixed mindset or a growth mindset. A fixed mindset is a belief that your intelligence is innate/you were born with it. A growth mindset, on the other hand, is a belief that success is a combination of the aptitude youâ€™re born with AND the amount of effort and hard work you put in. We don't know if Michael or Tiger were \"born champions\" but here's what we do know: Tiger started playing golf at age 2 and has practiced for hours every day since then to achieve the success he has today. Michael Jordan similarly practiced 3-4 hours every day to build on some of the innate skills he may have been born with. Without all of this practice and hard work, would these two champions have achieved the success they have today? Malcolm Gladwell, an author and sociologist, wrote a book called Outliers. In it, he says, \"The closer psychologists look at the careers of the gifted, the smaller the role innate talent seems to play and the bigger the role preparation seems to play.\" He found that the most talented students, musicians and athletes had gradually increased their practice while growing up until they had logged over 10,000 hours by the age of 20. The magic number seems to be 10,000 hours. That's the equivalent of about 20 hours of practice every week for 10 years. Mentee Email | Mentor Email Mentee Email Paragraph #1: Our Ritual: Share one â€œhighâ€ (or event, experience, moment that was very positive from the last week) and one â€œlowâ€ (event, experience, moment that was negative from the last week).Keep the conversation going by responding to your mentorâ€™s last email. Paragraph #2: In your own wordsâ€¦ - How would you define a Growth Mindset in your own words? -Do you believe that Tiger Woods and Michael Jordan use a Growth Mindset in their own lives? Why or why not? - Think of another example of someone you consider to be very successful (either a celebrity or someone in your own life) and talk about how that person has used a Growth Mindset to achieve their success. Paragraph #3: What about you? - Do you live by a Growth Mindset? How? -Tell your mentor about a specific example of how youâ€™ve used a Growth Mindset this school year. SIGN OFF: Wrap up your email and say goodbye. Mentor Email Mentor Tip:A Growth Mindset is a key non-academic skill we want our mentees to start embracing. To adopt a belief that YOU are in control of your own success because you can work hard and achieve your goals can be a very empowering outlook. As a mentor, constantly reminding your mentee that their hard work and effort can help them achieve their goals; that they are active participants in building their future will help keep them motivated to work toward the goals theyâ€™ve set for themselves. A fixed mindset is limiting, while a growth mindset allows us to believe that we can work hard toward anything. Obviously itâ€™s important to point out to your mentee that working hard does not guarantee success, nor does it mean that things wonâ€™t be challenging along the way, but working hard and putting the effort in will always get you farther than not doing those things. Paragraph #1: Our Ritual: Share one â€œhighâ€ (or event, experience, moment that was very positive from the last week) and one â€œlowâ€ (event, experience, moment that was negative from the last week). Keep the conversation going by responding to your menteeâ€™s thoughts about how they use a Growth Mindset in their own lives. -How have you seen your mentee use a Growth Mindset so far this year? -Validate how your mentee thinks theyâ€™ve used a Growth mindset and add on to what theyâ€™ve shared. -If your mentee doesnâ€™t agree with a Growth Mindset but rather believes that a Fixed Mindset is more accurate, restate the definition of each and help clarify the benefits of a Growth Mindset. Paragraph #2: In your own wordsâ€¦ - How would you define a Growth Mindset in your own words? Make sure to highlight the similarities in your definition and your menteeâ€™s definition and to emphasize that intelligence is changeable in your definition. Help your mentee understand what that really means. -Do you believe that Tiger Woods and Michael Jordan use a Growth Mindset in their own lives? Why or why not? - Think of another example of someone you consider to be very successful (either a celebrity or someone in your own life) and talk about how that person has used a Growth Mindset to achieve their success. Paragraph #3: What about you? - Do you live by a Growth Mindset? How? -Tell your mentee about a specific example of how youâ€™ve used a Growth Mindset recently"}}
	
	def __init__(self, curr, email):
		self.currFile = curr
		self.emailFile = email

	def readFile(self, file):
		fileObj = open(file, "r+")
		string = fileObj.read()
		return string

	def run(self):
		self.curr = self.readFile(self.currFile)
		self.email = self.readFile(self.emailFile)
		# self.currKeyDict = self.extractKeywords(self.curr)["keyword_extractor"]["keywords"]
		self.currKeyDict = self.currKeyDict["keyword_extractor"]["keywords"]
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
		highScore = self.currKeyDict[0]["term"]
		count = 21
		local = 1
		for obj in self.currKeyDict[:20]:
			if obj["score"] == highScore:
				local += 1
				currDict[obj["term"].lower()] = count
			if obj["score"] < highScore:
				currDict[obj["term"].lower()] = count - local
				local = 1
				count = count - local
		self.currDict = currDict

	def getEmailTopics(self, emailKeyDict, emailMultiDict):
		emailDict = {}
		count = 20
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
		self.emailDict = emailDict

	def finalScore(self, currDict, emailDict):
		score = 0
		for i in self.currDict.keys():
			if i in self.emailDict:
				score += self.currDict[i] + self.emailDict[i]
		self.score = score
		grade = int(score/25)
		if grade == 0:
			grade += 1
		self.grade = grade

if __name__ == "__main__":
	obj = Match(curr = "curr.txt", email = "email1.txt")
	obj.run()

