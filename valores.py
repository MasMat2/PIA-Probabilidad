datos = []
with open("valores_pia.txt", "r") as f:
    while(num:=f.readline()):
        datos.append(int(num))