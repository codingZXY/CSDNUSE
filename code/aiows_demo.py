import asyncio
import aiohttp

url = "wss://echo.websocket.org"


async def main():
    session = aiohttp.ClientSession()
    async with session.ws_connect(url) as ws:

        await prompt_and_send(ws)
        async for msg in ws:
            print('来自服务的信息:', msg)
            # await prompt_and_send(ws)

            if msg.type in (aiohttp.WSMsgType.CLOSED,
                            aiohttp.WSMsgType.ERROR):
                break
            else:
                print("接到数据", msg.data)


async def prompt_and_send(ws):
    new_msg_to_send = input('请输入往服务器发送的信息内容: ')
    if new_msg_to_send == 'exit':
        print('Exiting!')
        raise SystemExit(0)
    await ws.send_str(new_msg_to_send)


if __name__ == '__main__':
    print('输入 "exit" 退出')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
