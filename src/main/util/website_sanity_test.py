from urllib.request import urlopen
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from bs4 import BeautifulSoup


# download a file from a URL, returns content of downloaded file
def download_url(urlpath):
    try:
        # open a connection to the server
        with urlopen(urlpath, timeout=5) as connection:
            # read the contents of the url as bytes and return it
            return connection.read()
    except:
        return None


# decode downloaded html and extract all <a href=""> links
def get_urls_from_html(content):
    # decode the provided content as ascii text
    html = content.decode('utf-8')
    # parse the document as best we can
    soup = BeautifulSoup(html, 'html.parser')
    # find all the <a href=""> tags in the document
    atags = soup.find_all('a')
    # get all links from a tags
    return [tag.get('href') for tag in atags]


# filter out bad urls, convert relative to absolute if needed
def filter_urls(base, urls):
    filtered = set()
    for url in urls:
        # skip missing or bad urls
        if url is None or url.strip() is None:
            continue
        # skip other protocols
        if url.startswith('javascript'):
            continue
        # check if the url is relative
        if not url.startswith('http'):
            # join the base url with the absolute fragment
            url = urljoin(base, url)
        # store in the filtered set
        filtered.add(url)
    return filtered


# validate a list of urls, report all broken urls
def validate(filtered_links):
    # select the number of workers, no more than 1,000
    n_threads = min(1000, len(filtered_links))
    # validate each link
    with ThreadPoolExecutor(n_threads) as executor:
        # validate each url
        futures_to_data = {executor.submit(download_url, link): link for link in filtered_links}
        # report results as they are available
        for future in as_completed(futures_to_data):
            # get result from the download
            data = future.result()
            # check for broken url
            if data is None:
                print(f'.broken: {futures_to_data[future]}')


def test_site():
    url = 'https://acchakannada.com/posts.html'
    content = download_url(url)
    if content is None:
        print(f'\n Failed to download: {url}')
        return
    print(f'\n Downloaded: {url}')
    # extract all the links
    raw_links = get_urls_from_html(content)
    print(raw_links)
    print(f'\n found {len(raw_links)} raw links')
    # filter links
    filtered_links = filter_urls(url, raw_links)
    print(f'.found {len(filtered_links)} unique links')
    # validate all links
    validate(filtered_links)
    print('Done')
