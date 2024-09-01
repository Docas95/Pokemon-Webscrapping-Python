import requests
import urllib3
from bs4 import BeautifulSoup

URL = "https://pokemondb.net/pokedex/"
JPEG_URL = "https://img.pokemondb.net/artwork/large/"
SAVE_DIR = "data/"

def scrap_pokemon(pokemonnum, save):
    totaldata = [0] * pokemonnum
    for i in range(1, pokemonnum + 1):
        # get pokemon data
        data = ""

        url = URL + str(i)
        ourUrl = urllib3.PoolManager().request('GET', url).data
        soup = BeautifulSoup(ourUrl, "lxml")     

        # number
        number = str(i)
        data += number + '\n'

        # name
        name = soup.find('h1').text
        data += name + "\n"
        
        # type
        types = soup.find_all('a', attrs={'class': 'itype'})
        data += types[0].text

        if(len(types) > 1):
            if(types[0] != types[1]):
                data += "|" + types[1].text

        data += "\n"   

        # description
        description = soup.find('td', attrs={'class': 'cell-med-text'}).text
        data += description + "\n"

        # abilities
        abilities = soup.find_all('span', attrs={'class': 'text-muted'})
        data += abilities[0].text
        if(len(abilities) > 1):
            if(abilities[1].text[0] == "2"):
                data += "|" + abilities[1].text

        hidden_abilities = soup.find_all('small', attrs={'class': 'text-muted'})
        if(len(hidden_abilities) > 0 and hidden_abilities[0].text[0] != "("):
            data += "|" + hidden_abilities[0].text
        if(len(hidden_abilities) > 1 and hidden_abilities[1].text[0] != "("):
            data += "|" + hidden_abilities[1].text
        data += "\n"

        # stats
        stats = soup.find_all('td', attrs={'class': 'cell-num'});
        data += stats[0].text

        data += "|" + stats[3].text

        data += "|" + stats[6].text

        data += "|" + stats[9].text

        data += "|" + stats[12].text

        data += "|" + stats[15].text + "\n"

        # jpeg
        jpegurl = JPEG_URL + name.lower() + ".jpg"
        data += jpegurl

        # upload data to file

        print("##########################")
        print(data)
        print("##########################")

        totaldata[i-1] = data

        if(save == 1):
            store_data(number, data, jpegurl)

    return totaldata    

        
def store_data(number, data, url):
    # store written data
    filename = SAVE_DIR + number + ".txt"
    print("Creating file " + filename + "...")
    file = open(filename, "w")

    print("Saving data to file...")
    file.write(data)
    print("Saved data!")

    file.close();

    # download and store jpeg
    print("Downloading image...")
    jpegfilename = SAVE_DIR + number + ".jpg"
    response = requests.get(url)
    if response.status_code == 200:
        with open(jpegfilename, "wb") as jpegfile:
            jpegfile.write(response.content)
        print("Downloaded image successfully!")
    else:
        print("Could not download image! Status code:" + str(response.status_code))
        