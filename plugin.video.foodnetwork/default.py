import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon
from BeautifulSoup import BeautifulSoup

__settings__ = xbmcaddon.Addon(id='plugin.video.foodnetwork')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )


def getShows():
		req = urllib2.Request('http://www.foodnetwork.com/food-network-full-episodes/videos/index.html')
		req.addheaders = [('Referer', 'http://www.foodnetwork.com'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		shows = soup.find('ul', attrs={'class' : "playlists"})('li')
		for show in shows:
				name = show('a')[0].string
				url = show['data-channel']
				addDir(name,url,1,icon)
		addDir(__language__(30000),'',4,icon)
		addDir(__language__(30001),'',2,icon)
		
		
def getTopVideos():
		req = urllib2.Request('http://www.foodnetwork.com/food-network-top-food-videos/videos/index.html')
		req.addheaders = [('Referer', 'http://www.foodnetwork.com'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		shows = soup.find('ul', attrs={'class' : "playlists"})('li')
		for show in shows:
				name = show('a')[0].string
				url = show['data-channel']
				addDir(name,url,1,icon)

def getShowClips():
        addDir(__language__(30002), 'http://www.foodnetwork.com/40-a-day/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-40-Dollars-Day.jpg')
        addDir(__language__(30003), 'http://www.foodnetwork.com/30-minute-meals/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp200-show-30-Minute-Meals.jpg')
        addDir(__language__(30004), 'http://www.foodnetwork.com/ask-aida/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Ask-Aida.jpg')
        addDir(__language__(30005), 'http://www.foodnetwork.com/barefoot-contessa/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp200-show-Barefoot-Contessa.jpg')
        addDir(__language__(30006), 'http://www.foodnetwork.com/big-daddys-house/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Big-Daddys-House.jpg')
        addDir(__language__(30007), 'http://www.foodnetwork.com/boy-meets-grill/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Boy-Meets-Grill.jpg')
        addDir(__language__(30008), 'http://www.foodnetwork.com/chefs-vs-city/index.html', 3, 'http://img.foodnetwork.com/FOOD/2009/06/01/spShow_chefs-vs-city_s994x100.jpg')
        addDir(__language__(30009), 'http://www.foodnetwork.com/chic-easy/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/12/sp100-Chic-and-Easy.jpg')
        addDir(__language__(30010), 'http://www.foodnetwork.com/chopped/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/11/13/sp100-Chopped.jpg')
        #addDir(__language__(30011), 'http://www.foodnetwork.com/crave/index.html', 3, '')
        addDir(__language__(30012), 'http://www.foodnetwork.com/dear-food-network/index.html', 3, '')
        addDir(__language__(30013), 'http://www.foodnetwork.com/diners-drive-ins-and-dives/index.html', 3, 'http://img.foodnetwork.com/FOOD/2011/04/12/FN_Show-DDD-Header_s994x200.jpg')
        addDir(__language__(30014), 'http://www.foodnetwork.com/dinner-impossible/index.html', 3, 'http://img.foodnetwork.com/FOOD/2009/01/22/sp100-Dinner-Impossible-Irvine.jpg')
        addDir(__language__(30015), 'http://www.foodnetwork.com/down-home-with-the-neelys/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/26/sp200-down-home-neelys.jpg')
        addDir(__language__(30016), 'http://www.foodnetwork.com/easy-entertaining-with-michael-chiarello/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Easy-Entertaining.jpg')
        addDir(__language__(30017), 'http://www.foodnetwork.com/everyday-italian/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/29/sp200-show-Everyday-Italian-rev1.jpg')
        addDir(__language__(30018), 'http://www.foodnetwork.com/extreme-chef/index.html', 3, 'http://img.foodnetwork.com/FOOD/2011/06/22/FN_ExtremeChef_Showpg-hdr_994x100.jpg')
        addDir(__language__(30019), 'http://www.foodnetwork.com/extreme-cuisine-with-jeff-corwin/index.html', 3, 'http://img.foodnetwork.com/FOOD/2009/02/04/sp200-extreme-cuisine.jpg')
        addDir(__language__(30020), 'http://www.foodnetwork.com/feasting-on-waves/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/12/sp100-Feasting-on-Waves.jpg')
        addDir(__language__(30021), 'http://www.foodnetwork.com/food-detectives/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Food-Detectives.jpg')
        addDir(__language__(30022), 'http://www.foodnetwork.com/giada-at-home/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/10/09/sp100-Giada-at-Home.jpg')
        addDir(__language__(30023), 'http://www.foodnetwork.com/guy-off-the-hook/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/09/04/sp200-Guy-Off-Hook_2.jpg')
        addDir(__language__(30024), 'http://www.foodnetwork.com/healthy-appetite-with-ellie-krieger/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Healthy-Appetite.jpg')
        addDir(__language__(30025), 'http://www.foodnetwork.com/howd-that-get-on-my-plate/index.html', 3, 'http://img.foodnetwork.com/FOOD/2010/02/12/sp100_Howd-That-Get-Plate_s994x100.jpg')
        addDir(__language__(30026), 'http://www.foodnetwork.com/jamie-at-home/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Jamie-at-Home.jpg')
        addDir(__language__(30027), 'http://www.foodnetwork.com/paulas-best-dishes/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/12/sp100-Paulas-Best-Dishes.jpg')
        addDir(__language__(30028), 'http://www.foodnetwork.com/paulas-home-cooking/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp200-show-Paulas-Home-Cooking.jpg')
        addDir(__language__(30029), 'http://www.foodnetwork.com/paulas-party/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/12/sp100-Paulas-Party.jpg')
        addDir(__language__(30030), 'http://www.foodnetwork.com/quick-fix-meals-with-robin-miller/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Quick-Fix-Meals.jpg')
        addDir(__language__(30031), 'http://www.foodnetwork.com/rescue-chef/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Rescue-Chef.jpg')
        addDir(__language__(30032), 'http://www.foodnetwork.com/road-tasted-with-the-neelys/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/12/sp100-Road-Tasted-Neelys.jpg')
        addDir(__language__(30033), 'http://www.foodnetwork.com/simply-delicioso-with-ingrid-hoffmann/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Simply-Delicioso.jpg')
        addDir(__language__(30034), 'http://www.foodnetwork.com/the-best-thing-i-ever-ate/index.html', 3, 'http://img.foodnetwork.com/FOOD/2009/05/14/spShow_the-best-thing-i-ever-ate_s994x100.jpg')
        addDir(__language__(30035), 'http://www.foodnetwork.com/the-chef-jeff-project/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/09/04/sp100-Cheff-Jeff-Project.jpg')
        addDir(__language__(30036), 'http://www.foodnetwork.com/the-cooking-loft/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Cooking-Loft.jpg')
        #addDir(__language__(30037), 'http://www.foodnetwork.com/tough-cookies/index.html', 3, '')
        addDir(__language__(30038), 'http://www.foodnetwork.com/tylers-ultimate/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Tylers-Ultimate.jpg')
        addDir(__language__(30039), 'http://www.foodnetwork.com/ultimate-recipe-showdown/index.html', 3, 'http://img.foodnetwork.com/FOOD/2010/02/04/URS_banner_s994x200.jpg')
        addDir(__language__(30040), 'http://www.foodnetwork.com/unwrapped/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/08/08/sp100-Unwrapped.jpg')
        addDir(__language__(30041), 'http://www.foodnetwork.com/viva-daisy/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/12/23/sp100-viva-daisy.jpg')
        addDir(__language__(30042), 'http://www.foodnetwork.com/what-would-brian-boitano-make/index.html', 3, 'http://img.foodnetwork.com/FOOD/2009/06/01/spShow_WWBBM_s994x100.jpg')
        addDir(__language__(30043), 'http://www.foodnetwork.com/will-work-for-food/index.html', 3, 'http://img.foodnetwork.com/FOOD/2008/11/14/sp100-Will-Work-For-Food.jpg')

		
def index(url):
		req = urllib2.Request('http://www.foodnetwork.com/food/channel/xml/0,,'+url+',00.xml')
		req.addheaders = [('Referer', 'http://www.hgtv.com'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		videos = soup('video')
		for video in videos:
				name = video('clipname')[0].string
				length = video('length')[0].string
				thumb = video('thumbnailurl')[0].string
				description = video('abstract')[0].string
				link = video('videourl')[0].string
				playpath = link.replace('http://wms.scrippsnetworks.com','').replace('.wmv','')
				url = 'rtmp://flash.scrippsnetworks.com:1935/ondemand?ovpfv=1.1 swfUrl="http://common.scrippsnetworks.com/common/snap/snap-3.0.3.swf" playpath='+playpath
				addLink(name,url,description,length,thumb)


def indexShowClips(url):
		req = urllib2.Request(url)
		req.addheaders = [('Referer', 'http://www.foodnetwork.com'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		showID=re.compile("snap = new SNI.Food.Player.FullSize\(\\'vplayer-1\\',\\'(.+?)\\'\)").findall(link)
		if len(showID)<1:
				showID=re.compile("snap = new SNI.Food.Player.FullSize\(\\'vid-player\\', (.+?)\)").findall(link)
		if len(showID)<1:
				try:
						url = soup.findAll('ul', attrs={'class' : "tabnav clrfix"})[0]('a')[-1]['href']
				except:
						print '-------->video not found'
						return
				url='http://www.foodnetwork.com'+url
				req = urllib2.Request(url)
				req.addheaders = [('Referer', 'http://www.foodnetwork.com'),
						('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
				response = urllib2.urlopen(req)
				link=response.read()
				response.close()
				showID=re.compile("snap = new SNI.Food.Player.FullSize\(\\'vplayer-1\\',\\'(.+?)\\'\)").findall(link)
				if len(showID)<1:
						showID=re.compile("snap = new SNI.Food.Player.FullSize\(\\'vid-player\\', (.+?)\)").findall(link)
				if len(showID)<1:
						print '--------->video not found'
						return
		print'--------> '+showID[0]
		req = urllib2.Request('http://www.foodnetwork.com/food/channel/xml/0,,'+showID[0]+',00.xml')
		req.addheaders = [('Referer', 'http://www.hgtv.com'),
				('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0) Gecko/20100101 Firefox/4.0')]
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		soup = BeautifulSoup(link)
		videos = soup('video')
		for video in videos:
				name = video('clipname')[0].string
				length = video('length')[0].string
				thumb = video('thumbnailurl')[0].string
				description = video('abstract')[0].string
				link = video('videourl')[0].string
				playpath = link.replace('http://wms.scrippsnetworks.com','').replace('.wmv','')
				url = 'rtmp://flash.scrippsnetworks.com:1935/ondemand?ovpfv=1.1 swfUrl="http://common.scrippsnetworks.com/common/snap/snap-3.0.3.swf" playpath='+playpath
				addLink(name,url,description,length,thumb)
		

def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				params=sys.argv[2]
				cleanedparams=params.replace('?','')
				if (params[len(params)-1]=='/'):
						params=params[0:len(params)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]
								
		return param


def addLink(name,url,description,length,iconimage):
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name , "Plot":description, "Duration":length } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
		return ok


def addDir(name,url,mode,iconimage):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
		ok=True
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name } )
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
		return ok
		
			
params=get_params()
url=None
name=None
mode=None

try:
		url=urllib.unquote_plus(params["url"])
except:
		pass
try:
		name=urllib.unquote_plus(params["name"])
except:
		pass
try:
		mode=int(params["mode"])
except:
		pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None:
		print ""
		getShows()
	
elif mode==1:
		print ""+url
		index(url)

elif mode==2:
		print ""+url
		getShowClips()

elif mode==3:
		print ""+url
		indexShowClips(url)

elif mode==4:
		print ""+url
		getTopVideos()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
