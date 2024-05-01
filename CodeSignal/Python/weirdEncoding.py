# You've been actively exchanging email with one of your colleagues and noticed that you can't open his attachments. Unfortunately, he's just went on a vacation and you need these attached files right now.

# You've spent some time studying his emails and discovered that your colleague used the buggy email client which instead of using proper MIME Base64 encoding for the attachments used other variants differing in characters that represent values 62 and 63.
# Furthermore, different versions of this email client used different variations of the encoding!

# Given the encoding of the email client which was used to send attachment,
# decode it.

# Here is the default Base64 encoding table:

# Value	Char	Value	Char	Value	Char	Value	Char
# 0	A	16	Q	32	g	48	w
# 1	B	17	R	33	h	49	x
# 2	C	18	S	34	i	50	y
# 3	D	19	T	35	j	51	z
# 4	E	20	U	36	k	52	0
# 5	F	21	V	37	l	53	1
# 6	G	22	W	38	m	54	2
# 7	H	23	X	39	n	55	3
# 8	I	24	Y	40	o	56	4
# 9	J	25	Z	41	p	57	5
# 10	K	26	a	42	q	58	6
# 11	L	27	b	43	r	59	7
# 12	M	28	c	44	s	60	8
# 13	N	29	d	45	t	61	9
# 14	O	30	e	46	u	62	+
# 15	P	31	f	47	v	63	/
# Example

# For encoding = "-_" and message = "Q29kZVNpZ25hbA==", the output should be
# solution(encoding, message) = "CodeSignal".


import base64

def solution(encoding, message):
    # Create a translation table
    trans = str.maketrans(encoding, '+/')

    # Translate the message
    message = message.translate(trans)

    # Decode the message
    message = base64.b64decode(message).decode()

    return message
