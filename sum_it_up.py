
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
import re
from summarizer import Summarizer
model = Summarizer()

 ### Naive summarization based on word frequencies clustering

def resume(document, ratio = None, N=None):
    print(ratio)
    if ratio:
        print("yes")
        
        return model(document, ratio = ratio)
    else:
        print('NO')
        return model(document, num_sentences=N)


# def resume(document,N = 3):
#     """
#     document:
#     :param document: String sequence
#     :return summary: Summary of the text
#     """

#     # Removing Square Brackets and Extra Spaces
#     document = re.sub(r'\[[0-9]*\]', ' ', document)
#     document = re.sub(r'\s+', ' ', document)

#     # Removing special characters and digits
#     # document = re.sub('[^a-zA-Z]', ' ', document)
#     # document = re.sub(r'\s+', ' ', document)

#     document = document.replace("\n","")
#     document = document.replace("\r","")
#     document = document.replace("â€™","'")

#     # Object of automatic summarization.
#     auto_abstractor = AutoAbstractor()
#     # Set tokenizer.
#     auto_abstractor.tokenizable_doc = SimpleTokenizer()
#     # Set delimiter for making a list of sentence.
#     auto_abstractor.delimiter_list = [".", "\n"]
#     # Object of abstracting and filtering document.
#     abstractable_doc = TopNRankAbstractor()
#     # Summarize document.
#     result_dict = auto_abstractor.summarize(document, abstractable_doc)
#     doc_sentences = document.split(".")
#     # Output result.
#     sorted_index = sorted(result_dict['scoring_data'], key=lambda x: x[1], reverse=True)
#     top_indexes = [i[0] for i in sorted_index][:N]

#     summary = list()
#     for i in top_indexes:
#         summary.append(doc_sentences[i])
#     summary = ". ".join(summary) +"."
#     return summary



# def resume(document, ratio = 0.5):
# # https://pypi.org/project/bert-extractive-summarizer/

# # https://stackoverflow.com/questions/13965823/resource-corpora-wordnet-not-found-on-heroku   
# #     nlp = spacy.load('en')
# #     nlp.add_pipe(LanguageDetector(), name='language_detector', last=True)
# #     doc = nlp(text)
# #     lang = doc._.language['language']
#     # to use later after customizing library

    
#     if 'model' in locals():
#         pass
#     else:
#         model = Summarizer()
#     return model(document, ratio = ratio)


from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('logo3.png', 140, 8, 33)
        #         self.set_font('Arial', 'B', 15)
        self.set_font('DejaVu', '', 15)

        self.cell(80)  # Move to the right
        # Title
        #         self.set_draw_color(0, 80, 180)
        #         self.set_fill_color(230, 230, 0)
        self.set_text_color(65, 105, 225)
        self.cell(30, 10, "Here is your summary, thank you for using                        !", 0, 0, 'C')
        # Line break
        self.ln(40)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        #         self.set_font('Arial', 'I', 8)
        self.set_font('DejaVu', '', 12)

        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def chapter_body(self, text):
        # Read text file

        # Times 12
        # Output justified text
        self.multi_cell(0, 5, text)
        # Line break
        self.ln()

        # Mention in italics
        #         self.set_font('', 'I')
        #         self.cell(0, 5, '(end of excerpt)')


def text_to_pdf(summary):
    """Convert text to pdf file"""

    # Instantiation of inherited class
    #     summary = summary.encode('windows-1252')
    SYSTEM_TTFONTS = "C:\WINDOWS\FONTS"
    FPDF_CACHE_MODE = 0
    print(summary)
    pdf = PDF()
    pdf.set_doc_option('core_fonts_encoding', 'utf-8')
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.chapter_body(summary)
    import os
    print(os.getcwd())
    pdf.output('tmp1.pdf', 'F')
    #  D to download in browser, F for local file

import pyttsx3

def tts(text):
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 150)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 1 for female
    engine.setProperty('age', 60)  # changing index, changes voices. 1 for female

    # engine.say(text)
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(text, 'tmp.mp3')
    engine.runAndWait()

