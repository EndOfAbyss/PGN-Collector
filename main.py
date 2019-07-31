import requests
import time

def run():
    print("PGN COLLECTOR")
    print("-------------")
    username = "asdf"
    pgn_groups = []
    r1 = None
    pgn_text_list = []

    while username != "0":
        username = input("Ingrese nick del jugador: ")

        if username == "0":
            exit(0)
        
        r1 = requests.get(f"https://api.chess.com/pub/player/{username}/games/archives")

        if r1.status_code == 404:
            print(f"No existe usuario con nick {username}. Vuelva a ingresar otro nick o ingrese 0 para salir.")
        
        if r1.status_code == 200:
            print(f"Obteniendo datos de {username}...")
            break
    
    data1 = r1.json()

    for item in data1['archives']:
        pgn_groups.append(item)

    archivo = open(f"games_{username}.pgn", "w", encoding="utf-8")

    for group_url in pgn_groups:

        print(f"Almacenando datos del {group_url[-7:]}")

        r2 = requests.get(group_url)
        data2 = r2.json()

        for item in data2['games']:
            if "pgn" in item.keys():
                pgn_text_list.append(item['pgn'])
    
    archivo.write("\n\n".join(pgn_text_list))

    archivo.close()

if __name__ == "__main__":
    run()
