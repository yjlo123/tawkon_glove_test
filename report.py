import os
import sys

screenshot_path = "glove_test/screenshots";
raw = open(screenshot_path+'/report_raw.html', 'w')
check = open(screenshot_path+'/check.txt', 'w')

if len(sys.argv) != 2:
	print "[report_raw] Incorrect argument"
	exit()
country = sys.argv[1]

if country == "IL":
	screenshots = ['tut_0', 'tut_1', 'tut_2', 'tut_3', 'tut_4', 'tut_5', 'nap_email_0', 'nap_email_1', 'nap_num_0', 'nap_num_1', 'result_1', 'result_5', 'info', 'price', 'result_offer', 'result_offer_disabled', 'how']
elif country == "US":
	screenshots = ['tut_0', 'tut_1', 'tut_2', 'tut_3', 'tut_4', 'tut_5', 'nap_email_0', 'nap_email_1', 'result_1', 'result_4', 'info', 'how']
else:
	print "Invalid country"
	exit()

beginning = '''<html>
<head>
<title>Result</title>
<style>
table,th, td{
	border: 1px solid black;
	text-align:center;
}
tr:hover{
	background-color: rgb(110,215,172);
}
a{
	text-decoration: none;
	font-weight: bold;
}
</style>
</head>
	<body>
		<h1 style="color:rgb(110,215,172); text-align:center;">Glove UI Testing Report</h1>
		<table>
			<tr><th>dpi</th><th>resolution</th>'''
for ss in screenshots:
	beginning += "<th>"+ss+"</th>"
beginning += '''</tr> '''
raw.write(beginning)

def getdpi(reso):
	r = int(reso.split(' ')[0])
	if r < 400:
		return "mdpi"
	elif r < 600:
		return "hdpi"
	elif r < 900:
		return "xhdpi"
	else:
		return "xxhdpi"

def compare(reso):
	return int(reso.split(' ')[0])

for dirname, dirnames, filenames in os.walk(screenshot_path):
	for subdirname in sorted(dirnames, key=compare):
		check.write('['+str(subdirname)+']'+"\n")
		raw.write('<tr><td> '+getdpi(str(subdirname))+' </td><td>'+subdirname+'</td>')
		for screenshotname in screenshots:
			raw.write('<td><a href="'+str(subdirname)+'/'+screenshotname+'.png">#</a></td>')
			check.write(screenshotname+'=0\n')
		check.write('\n')

end='''</table></body></html>'''
raw.write(end)
raw.closed
check.closed