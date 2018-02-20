def centre_text(*args,seps=' ',end='\n',file=None,flush=False):
    text=""
    for arg in args:
        text+=str(arg)+seps
    print(text,end=end,file=file,flush=flush)

centre_text("dave is ", 5, " years old",seps=' * ')     