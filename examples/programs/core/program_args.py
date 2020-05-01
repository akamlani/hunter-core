import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-port', 	dest='port', 	type=int,	default='9997')
    parser.add_argument('-src', 	dest='src_file', 		    default='./ppdb/xxxl_clusters.txt')
    args = parser.parse_args()
