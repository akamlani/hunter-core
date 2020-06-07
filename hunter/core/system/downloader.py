from   pathlib import Path
import requests
import io 

import tarfile
import zipfile

read_io = lambda raw_bytes: io.BytesIO(raw_bytes)      # read_io(response.content)       


def download(url:str, dest_dir:str, force_dwld:bool=False, 
             chunk_size:int=1024*1024, timeout:int=5, retries:int=5) -> None:
    """Download Source File from Url"""
    filename = Path(url).name
    filename = Path(dest_dir)/filename
    filename.parent.mkdir(parents=True, exist_ok=True)
    # perform download
    if not filename.exists() or force_dwld: 
        session  = requests.Session()
        session.mount('http://', requests.adapters.HTTPAdapter(max_retries=retries))
        session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0'})
        response  = session.get(url, stream=False)
        file_size = int(response.headers["Content-Length"])

        with open(filename, 'wb') as f:
            num_bytes = 0
            try:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    num_bytes += len(chunk)
                    f.write(chunk)
            except requests.exceptions.ConnectionError as e:
                print(f'download failure for {url} and dest dir {dest_dir} with bytes downloaded {num_bytes}')
            print(f"Source: {filename}, # Bytes downloaded: {num_bytes}, # Bytes Expected {file_size}")
            assert(num_bytes == file_size)
    print(f"downloaded Source: {filename}")


def file_extract(fname:str, dest:str=None) -> None:
    "Extract `fname` to `dest` using `tarfile` or `zipfile`."
    if   fname.endswith('gz'):  tarfile.open(fname, 'r:gz').extractall(dest)
    elif fname.endswith('zip'): zipfile.ZipFile(fname     ).extractall(dest)
    else: raise Exception(f'Unrecognized archive: {fname}')


