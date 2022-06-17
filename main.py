from tap import Tap
from app.execute import execute


class ArgumentParser(Tap):
    files: str
      
    
if __name__ == "__main__":

    args = ArgumentParser().parse_args()
    files = [file.strip() for file in args.files.split(",")]
    
    execute(files)