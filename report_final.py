import os
import sys
import time

screenshot_path = "glove_test/screenshots";
check = open(screenshot_path+'/check.txt', 'r')
report = open(screenshot_path+'/report.html', 'w')

if len(sys.argv) != 2:
	print "[report_final] Incorrect argument"
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
body{
	text-align: center;
}
table,th, td{
	border: 1px solid black;
	text-align:center;
}
table{
	margin-left:auto; 
    margin-right:auto;
}
tr:hover{
	background-color: rgb(230,230,230);
}
a{
	text-decoration: none;
	font-weight: bold;
}
.r{
	background-color: rgb(255,70,70)
}
.o{
	background-color: rgb(255,160,0)
}
.y{
	background-color: rgb(255,244,119)
}
.g{
	background-color: rgb(67,214,109)
}
.n{
	background-color: rgb(164,164,164)
}
</style>
</head>
	<body>
		<h1 style="color:rgb(110,215,172); text-align:center;">Glove UI Testing Report</h1>
		<p>'''+time.strftime("%A, %d %b, %Y %H:%M:%S")+'''</p>
		<table>
			<tr><th>dpi</th><th>resolution</th>'''
for ss in screenshots:
	beginning += "<th>"+ss+"</th>"
beginning += '''</tr> '''
report.write(beginning)


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

statistics = [0, 0, 0, 0, 0, 0]

def color(r):
	r = r[0]
	if r == '#':
		statistics[0] += 1
		return ""
	elif r == '0':
		statistics[1] += 1
		return "class='g'"
	elif r == '1':
		statistics[2] += 1
		return "class='y'"
	elif r == '2':
		statistics[3] += 1
		return "class='o'"
	elif r == '3':
		statistics[4] += 1
		return "class='r'"
	else:
		statistics[5] += 1
		return "class='n'"


for dirname, dirnames, filenames in os.walk(screenshot_path):
	for subdirname in sorted(dirnames, key=compare):
		check.readline()
		report.write('<tr><td> '+getdpi(str(subdirname))+' </td><td>'+subdirname+'</td>')
		for screenshotname in screenshots:
			rate = str(check.readline()).split('=')[1]
			if rate == '\n':
				rate = '#';
			report.write('<td '+color(rate)+'><a href="'+str(subdirname)+'/'+screenshotname+'.png">'+rate+'</a></td>')
		check.readline()

report.write('</table>')


#statistics table
report.write('<h3>Statistics</h3>')
sta_table = '''<table>
	<tr><td class="g">'''+str(statistics[1])+'''</td></tr>
	<tr><td class="y">'''+str(statistics[2])+'''</td></tr>
	<tr><td class="o">'''+str(statistics[3])+'''</td></tr>
	<tr><td class="r">'''+str(statistics[4])+'''</td></tr>
	<tr><td class="n">'''+str(statistics[5])+'''</td></tr>
	<tr><td>'''+str(statistics[0])+'''</td></tr>
	<tr><th>Total: '''+str(sum(statistics))+'''</th></tr>
	<tr><th>Percentage: '''+str(round(float(statistics[1])*100/float(sum(statistics)), 2))+'''%</th></tr>
</table> '''

report.write(sta_table)

end='</body></html>'
report.write(end)
report.closed