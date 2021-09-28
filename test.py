from utils import utils_image as util

def main():
    src = r'C:\StudyData\Jupyter\Untitled Folder\64ori.yuv'
    img = util.imread_uint(src, 64, 64)
if __name__ == "__main__":
    main()