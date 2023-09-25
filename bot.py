import discord
import requests
import asyncio

# Configura el bot
bot_token = '8f660268c830b7a8de52c1bc4cdf4ce9d8cbf540a565b4f9582c8c58fca16217'
server_ip_url = 'URL_PARA_OBTENER_LA_IP'  # Aquí debes colocar la URL que proporciona la IP dinámica.

client = discord.Client()

@client.event
async def on_ready():
    print(f'Conectado como {client.user.name}')
    await check_server_status()

async def check_server_status():
    while True:
        try:
            # Realiza una solicitud HTTP para obtener la IP del servidor de juego
            response = requests.get(server_ip_url)

            if response.status_code == 200:
                server_ip = response.text.strip()
                status_message = f"ON : IP {server_ip}"
            else:
                status_message = "OFF : IP Desconocida"

            # Busca el canal donde quieres enviar el mensaje
            channel = client.get_channel(TU_ID_DE_CANAL)
            await channel.send(status_message)

        except Exception as e:
            print(f"Error: {str(e)}")

        # Espera un tiempo antes de verificar de nuevo (por ejemplo, cada 5 minutos)
        await asyncio.sleep(300)

client.run(bot_token)
