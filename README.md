# libgen-search

A python library for Libgen.rs to search books.\
This is the synchronous version of this [library](https://github.com/Samfun75/libgenesis) but without the download feature.

## How to install

Run this command in your terminal :

```bash
pip install git+https://github.com/krishna2206/libgen-search.git
```

## Importing libgensearch

```python
from libgensearch import Libgen
```

## Creating libgensearch object

```python
libgen = Libgen()
```

or

```python
libgen = Libgen(sort='year', sort_mode='ASC', result_limit='50')
```

When creating an instance of LibGen, you can set 3 option.

- **sort**: You can use this to choose a sorting method from allowed fields ( 'id', 'author', 'title', 'publisher', 'year', 'pages', 'language', 'size', 'extension'). Defaults to 'def'.
- **sort_mode**: Pick the order of the sort ascending or decending ('ASC', 'DESC'). Defaults to 'DESC'.
- **result_limit**: Limit the number of results based on the allowed limit (25, 50, 100). Defaults to 25.

## Searching for a book

```python
query = 'japan history'
result = await libgen.search(query)
for item in result:
    print('id = ' + item)
    print('title = ' + result[item]['title'])
    print('md5 = ' + result[item]['md5'])
```

The returned data looks like this: (The dict key is the Libgen id of the book)

```python
{
    '881061':{
        'title': 'The Japanese Experience: A Short History of Japan (History of Civilisation)',
        'volumeinfo': '',
        'series': '',
        'periodical': '',
        'author': 'W. G. Beasley',
        'year': '1999',
        'edition': '',
        'publisher': 'University of California Press',
        'city': '',
        'pages': '331',
        'language': 'English',
        'topic': '',
        'library': '',
        'issue': '0',
        'identifier': '0520220501, 9780520220508',
        'issn': '',
        'asin': '',
        'udc': '',
        'lbc': '',
        'ddc': '',
        'lcc': '',
        'doi': '',
        'googlebookid': '',
        'openlibraryid': '',
        'commentary': '',
        'dpi': '0',
        'color': '',
        'cleaned': '',
        'orientation': '',
        'paginated': '',
        'scanned': '',
        'bookmarked': '',
        'searchable': '1',
        'filesize': '29750320',
        'extension': 'pdf',
        'md5': 'a382109f7fdde3be5b2cb4f82d97443b',
        'generic': '',
        'visible': '',
        'local': '0',
        'timeadded': '2013-02-15 18:40:21',
        'timelastmodified': '2019-12-21 21:23:21',
        'coverurl': 'http://libgen.rs/covers/881000/a382109f7fdde3be5b2cb4f82d97443b-g.jpg',
        'identifierwodash': '0520220501,9780520220508',
        'tags': '',
        'pagesinfile': '331',
        'descr': '',
        'toc': '',
        'sha1': 'ZZYRRG56BOX3XAQ5D2IWAV2FUUC35ELG',
        'sha256': '3B40D6524409A18573900B729AB1BFB872E26CF111A4845F375A84BD0CB12460',
        'crc32': '3DB84D01',
        'edonkey': 'A63EEBB71C46DAE130725C07F2CDC67C',
        'aich': '733CLKTMCYOGD4W5PIG2GMA7CMLAFN2V',
        'tth': 'O4O5Z7UL2YAOUG57PINCLOAN63HVZPCSDYACT6Q',
        'btih': '84195af51fa738cb232297dd1376df6d8b8313be',
        'mirrors':
            {
                'main': 'http://library.lol/main/a382109f7fdde3be5b2cb4f82d97443b',
                'libgen.lc': 'http://libgen.lc/ads.php?md5=a382109f7fdde3be5b2cb4f82d97443b',
                'z-library': 'http://b-ok.cc/md5/a382109f7fdde3be5b2cb4f82d97443b',
                'libgen.pw': 'https://libgen.pw/item?id=881061',
                'bookfi': 'http://bookfi.net/md5/a382109f7fdde3be5b2cb4f82d97443b',
                'torrent': 'http://libgen.rs/book/index.php?md5=a382109f7fdde3be5b2cb4f82d97443b&oftorrent=',
                'torrent_1k': 'http://libgen.rs/repository_torrent/r_881000.torrent',
                'gnutella': 'magnet:?xt=urn:sha1:ZZYRRG56BOX3XAQ5D2IWAV2FUUC35ELG&xl=29750320&dn=a382109f7fdde3be5b2cb4f82d97443b.pdf',
                'ed2k': 'ed2k://|file|A382109F7FDDE3BE5B2CB4F82D97443B.pdf|29750320|A63EEBB71C46DAE130725C07F2CDC67C|h=733CLKTMCYOGD4W5PIG2GMA7CMLAFN2V|/',
                'dc++': 'magnet:?xt=urn:tree:tiger:O4O5Z7UL2YAOUG57PINCLOAN63HVZPCSDYACT6Q&xl=29750320&dn=a382109f7fdde3be5b2cb4f82d97443b.pdf'
            }
    },
    'id_of_book':{
        ...
        ...
        ...
    },
    'id_of_book':{
        ...
        ...
        ...
    },
}
```
