import urllib
import argparse


W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

alldorks=["wp-login.php","phpmyadmin","robots.txt","htaccess.txt","wp-admin/post.php?post=","phpinfo.php","includes/config.php.new","configuration.php-dist","app_dev.php/login","dbman/default.pass","wp-content/w3tc/dbcache","voice/advanced/",
"manager/media/editor/plugins/ImageManager/manager.php","gadmin/index.php","vb/install/upgrade.php","vb/install/install.php","configuration.php-dist","logs/access.log","log/access.log","access.log","index.php?option=com_jeajaxeventcalendar","jscripts/tiny_mce/plugins/tinybrowser","modules/rmgallery","modules/debaser","phpwcms/index.php?id=","modules/lykos_reviews/","webquest/soporte_derecha_w.php?","modules/articles/index.php?cat_id=","index.php?option=com_jombib",
"modules/wfsection/","wp-content/plugins/age-verification/age-verification.php","includes/config.php","private_files","dbg-wizard.php","wp-admin/admin-ajax.php?action=revslider_ajax_action","plugins/wp-backitup/","security/xamppdirpasswd.txt","cacti/graph_view.php","cacti/graph.php?","backup","sql/backup","reports/rwservlet","administrator/index.php?autologin=1&passwd=[password]&username=[username]","data/nanoadmin.php","jenkins/login","module.php/core/loginuserpass.php",
"wp-content/uploads/ ","wp-config.txt","secure/login.aspx","wp-content/uploads/dump.sql","root/etc/passwd"]

Wordpress=['wordpress.php','hello-wordpress.php','hi-wordpress']
Joomla=['joomla.php','hello-joomla.php','hi-joomla']
Panel=['admin.php','admin/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','joomla/administrator','login.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']



parser=argparse.ArgumentParser(description="Select an Option")
parser.add_argument('-A','--juicy',help='Use Juicy Files',action='store_true',default=True)
parser.add_argument('-W','--wordpress',help='Use Wordpress Dorks',action='store_true',default=False)
parser.add_argument('-J','--joomla', help='Use Joomla Dorks',action='store_true',default=False)
parser.add_argument('-P','--panel',help='Find Admin Panel',action='store_true',default=False)
parser.add_argument('-V','--verbose',help='Muestra mas informacion',action='store_true',default=False)

parser.add_argument('Target',help="Target",type=str)
args=parser.parse_args()


def fix_url(url):
	url_out=""
	if url[:7]  == "http://"           : url_out = url
	if url[:8]  == "https://"          : url_out = url
	if url[:7]  != "http://" and  url[:8]  != "https://"         : url_out = "http://" + url
	if url[(len(url)-1):] != "/"       : url_out = url_out + "/"
	return url_out
	
url=fix_url(args.Target)

if args.juicy:
	print O + "Finding Juicy Files!"
	for test_dork in alldorks:
		if urllib.urlopen(url+test_dork).getcode() == 200:
			print G + "[+]" + url+test_dork + test_dork
		else:
			if args.verbose:print R + "[-]" + url+test_dork + test_dork

elif args.juicy:
	print O + "Finding Juicy Files!"
	for test_dork in alldorks:
		if urllib.urlopen(url+test_dork).getcode() == 200:
			print G + "[+]" + url+test_dork + test_dork
		else:
			if args.verbose:print R + "[-]" + url+test_dork + test_dork


if args.panel:
	print O + "Finding Admin Panel!"
	for test_panel in Panel:
		if urllib.urlopen(url+test_panel).getcode() == 200:
			print G + "[+]" + url+test_dork + test_panel
		else:
			if args.verbose:print R + "[-]" + url+test_dork + test_panel


elif args.wordpress:
	print O + "Finding Wordpress Juicy Files!"
	for test_wordpress in Panel:
		if urllib.urlopen(url+test_wordpress).getcode() == 200:
			print G + "[+]" + url+test_dork + test_wordpress
		else:
			if args.verbose:print R + "[-]" + url+test_dork + test_wordpress


elif args.joomla:
	print O + "Finding Joomla Juicy Files!"
	for test_joomla in Panel:
		if urllib.urlopen(url+test_joomla).getcode() == 200:
			print G + "[+]" + url+test_dork + test_joomla
		else:
			if args.verbose:print R + "[-]" + url+test_dork + test_joomla
