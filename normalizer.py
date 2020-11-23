import re 


def fix_prefix(input_text):
 '''Fixes Persian prefixes می/نمی/بی by adding a ZWNJ''' 
 pattern = r'\s*(ن?می)\s+'
 pattern_bi = r'\s*(بی)\s+' 
 output_text = re.sub(pattern, ' \\1‌', input_text)
 output_text = re.sub(pattern_bi, ' \\1‌', input_text)
 return output_text
 
def fix_suffix(input_text):
 '''Fixes Persian suffixes تر/ترین/ها/های by adding a ZWNJ''' 
 pass

def fix_english_quote(input_text):
 '''Replaces english quotation marks with Persian Gioumeh'''
 pass

def fix_numbers(input_text):
 '''Replaces Arabic and English numbers with Persian ones''' 
 numerals_dic = input_text.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
 arabic_numerals_dic = input_text.maketrans("١٢٣٤٥٦٧٨٩٠", "۱۲۳۴۵۶۷۸۹۰") 
 input_text = input_text.translate(numerals_dic)
 input_text = input_text.translate(arabic_numerals_dic)

 return input_text

def fix_en_numbers(input_text):
 '''Replaces Persian numbers with English ones in an English phrase'''
 pattern = r'[a-zA-Z\-_]{2,}[۰-۹]+|[۰-۹]+[a-zA-Z\-_]{2,}'
 translation_dic = input_text.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")
 input_text = input_text.split(' ')
 new_string = []

 for element in input_text:
  new_string.append(element.translate(translation_dic))

 new_string = ' '.join(new_string)
 return new_string

def fix_whole_numbers(input_text):
 input_text = fix_numbers(input_text)
 input_text = fix_en_numbers(input_text)

 return input_text


def fix_badchars(input_text):
 '''Repleaces ك and ي with ک and ی.'''
 input_text = input_text.replace("ي", "ی")
 input_text = input_text.replace("ك", "ک")

 return input_text
