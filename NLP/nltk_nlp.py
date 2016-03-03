#-*- coding: utf-8 -*-
import nltk.data
import re
import pprint
import os
from nltk.stem.porter import *

def traverse(src):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    pstemmer = PorterStemmer()
    for filename in os.listdir(src):
        fin = open(src+'/'+filename)
        text = fin.read()
        get_count(text, sent_detector, pstemmer)

def get_count(text,sent_detector,pstemmer):
    asciitext = text.decode('utf-8')
    sentences = sent_detector.tokenize(asciitext.lower().strip())
    dic ={}
    for sentence in sentences:
        try:
            w = nltk.word_tokenize(sentence)
            tags = nltk.pos_tag(w)
            # print tags
            usedTags = ['NN.*','VB.*','JJ.*','RB.*']
            # NN = Nouns
            # VB = Verbs
            # JJ = Adjectives
            # RB = Adverbs

            reqdTags = "("+")|(".join(usedTags)+")"

            reqdWords = [a for (a, b) in tags if re.match(reqdTags, b) and re.match('[a-z].*',a)]

            # Stem the required words

            stemmedWords = [pstemmer.stem(a) for a in reqdWords]

            # print reqdWords
            for string in stemmedWords:
                if dic.has_key(string):
                    dic[string] += 1
                else:
                    dic[string] = 1
        except Exception,e:
            print "Error"
        # a = raw_input()
    pprint.pprint(dic)
    return dic

def stanfordNERExtractor(sentence):
    from nltk.tag.stanford import NERTagger
    st =  NERTagger('/usr/share/stanford-ner/classifiers/all.3class.distsim.crf.ser.gz',
               '/usr/share/stanford-ner/stanford-ner.jar')
    return st.tag(sentence.split())

traverse('../dat/content')

# stanfordNERExtractedLines = stanfordNERExtractor("New York")
# print stanfordNERExtractedLines #[('New-York', 'LOCATION')]


# text = '''
# CIA Report Finds Concerns With Ties to New York Police - The New York Times
# NYTimes.com no longer supports Internet Explorer 9 or earlier. Please upgrade your browser.
# N.Y. / Region|CIA Report Finds Concerns With Ties to New York Police
# CIA Report Finds Concerns With Ties to New York Police
# Four Central Intelligence Agency officers were embedded with the New York Police Department in the decade after Sept. 11, 2001, including one official who helped conduct surveillance operations in the United States, according to a newly disclosed CIA inspector general's report.
# That officer believed there were "no limitations" on his activities, the report said, because he was on an unpaid leave of absence, and thus exempt from the prohibition against domestic spying by members of the CIAAnother embedded CIA analyst — who was on its payroll — said he was given "unfiltered" police reports that included information unrelated to foreign intelligence, the CIA report said.
# The once-classified review, completed by the CIA inspector general in December 2011, found that the four agency analysts — more than had previously been known — were assigned at various times to "provide direct assistance" to the local police. The report also raised a series of concerns about the relationship between the two organizations.The CIA inspector general, David B. Buckley, found that the collaboration was fraught with "irregular personnel practices," that it lacked "formal documentation in some important instances," and that "there was inadequate direction and control" by agency supervisors."While negative public perception is to be expected from the revelation of the agency's close and direct collaboration with any local domestic police department, a perception that the agency has exceeded its authorities diminishes the trust placed in the organization," Mr. Buckley wrote in a cover memo to David H. Petraeus, then the CIA director.The declassification of the executive summary, in response to a Freedom of Information Act suit, comes at a time of intense interest in domestic spying after leaks by a former contractor for the National Security Agency.It also comes amid lawsuits against the Police Department alleging unconstitutional surveillance of Muslim communities and mosques in New Jersey and New York. And a group of plaintiffs from a 1971 lawsuit over harassment of political groups by the Police Department's so-called Red Squad has asked a judge to tighten guidelines stemming from that case on police investigations involving political or religious activity.
# Paul J. Browne, a police spokesman, said that the lawsuits were without merit. He also said that the inspector general had found nothing illegal and that the last embedded CIA official left the police in 2012."We're proud of our relationship with CIA and its training," he said, saying it was partly responsible for the absence of casualties from a terror attack in New York in the years since Sept. 11 and the anthrax attacks. He added that the terrorists "keep coming and we keep pushing back."The CIA-Police Department partnership dates from 2002, when David Cohen, a former CIA officer who became deputy commissioner for intelligence at the Police Department after the Sept. 11 attacks, reached out to his former agency in building up its counterterrorism abilities.
# The inspector general's office began the investigation in August 2011 after The Associated Press published an article about the CIA's relationship with the Police Department's intelligence division. It was part of a series about New York police surveillance of Muslims that was later awarded a Pulitzer Prize for investigative reporting.When the classified report was completed in 2011, spokesmen for the CIA and the Police Department said it had concluded that the CIA had not violated a law and an executive order that prohibited it from domestic spying or performance of law-enforcement powers. But the document shows that that conclusion was not the whole story. The inspector general warned in his cover letter that the collaboration raised "considerable and multifaceted" risks for the agency.
# This week, it released an executive summary and cover memo in response to a Freedom of Information Act lawsuit filed by the Electronic Privacy Information Center, a nonprofit civil-liberties group, which provided it to The New York Times."The CIA is not permitted to engage in domestic surveillance," said Ginger McCall, the director of the group's Open Government Project. "Despite the assurances of the CIA's press office, the activities documented in this report cross the line and highlight the need for more oversight."Dean Boyd, a CIA spokesman, said the inspector general found no legal violations or evidence that the agency's support to the Police Department constituted "domestic spying."
# "It should come as no surprise that, after 9/11, the CIA stepped up its cooperation with law enforcement on counterterrorism issues or that some of that increased cooperation was in New York," he said in an e-mail. "The agency's operational focus, however, is overseas, and none of the support we have provided to N.Y.P.D. can rightly be characterized as ‘domestic spying' by the CIA Any suggestion along those lines is simply wrong."The report shows that the first of the four embedded agency officers began as an adviser in 2002 and went on an unpaid leave from the agency from 2004 to 2009. During that latter period, it said, he participated in — and directed — "N.Y.P.D. investigations, operations, and surveillance activities directed at U.S. persons and non-U.S. persons."The official received a Police Department paycheck. He told the inspector general that he "did not consider himself an agency officer and believed he had ‘no limitations' as far as what he could or could not do." CIA lawyers said that officials on unpaid leave who are "acting in a personal capacity and not subject to CIA direction" are not constrained by the law barring the agency from domestic security functions, the report said.Another CIA analyst was detailed to the Police Department in early 2008 and remained on the agency's payroll. From about February to April 2008, he told the inspector general he had received daily files, including the police intelligence division's investigative reports "that he believed were unfiltered."
# That meant they had not been prescreened to remove information unrelated to foreign intelligence information, like evidence of domestic criminal activity. Later, the report says, the system was changed and police analysts gave him printouts of only those reports deemed to have potential foreign-intelligence information — about 10 to 12 a day.Still, a former Police Department intelligence analyst who now works for the CIA's National Clandestine Service maintained that the embedded CIA official had not had "unrestricted or unfiltered access" to the reports. The inspector general did not clear up the discrepancy.
# Meanwhile, the Police Department sent a detective to the CIA from October 2008 to November 2009 to "receive agency operational training to enhance the capability" of its intelligence division's counterterrorism efforts in the metropolitan area.Two other agency officials also worked for a period at the Police Department. One "spent considerable time and effort trying to help N.Y.P.D. improve its volatile relationship with the local F.B.I.," and the report said senior agency officials expressed concern that the arrangement had "placed the agency in the middle of a contentious relationship.""The revelation of these issues," Mr. Buckley wrote, "leads me to conclude that the risks associated with the Agency's relationship with the N.Y.P.D. were not fully considered and that there was inadequate direction and control by the agency managers responsible for the relationship."
# A version of this article appears in print on June 27, 2013, on page A1 of the New York edition with the headline: CIA Sees Concerns on Ties to New York Police.
# Accessibility concerns? Email us at accessibility@nytimes.com. We would love to hear from you.
# '''
# count_nouns(text)
