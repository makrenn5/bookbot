def word_count(book):
	with open(book) as text:
		txt_string = text.read()
		words_list = txt_string.split()
		count = len(words_list)
	return count

def count_chars(book):
	chars_dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,' ':0,'.':0,',':0,';':0,':':0,'[':0,']':0,'{':0,'}':0,'&':0,'/':0,'*':0,'-':0,'_':0}
	with open(book) as text:
		txt_string = text.read()
	for char in txt_string:
		lower_case = char.lower()

