from flet import *
def main(page:Page):
    page.title='Flash'
    page.scroll='auto'
    page.window.width=390
    page.window.height=740
    page.window.top=20
    page.bgcolor="#ffffff"
    page.theme_mode=ThemeMode.LIGHT

    flashlight=Flashlight()
    page.overlay.append(flashlight)

    ph=PermissionHandler()
    page.overlay.append(ph)
    def open(e):
        ph.open_app_settings()

    page.add(
        AppBar(
            bgcolor='#ff2482',
            title=Text('Torch [DJ]',weight=FontWeight.W_500), 
            leading=Icon(Icons.FLASHLIGHT_ON,color="white"),
            color='white',
            actions=[
                IconButton(Icons.SETTINGS,on_click=open)

            ]
            
        ),
        Row([
            Text("\nTorch App",size=37,color='#ff2482'),
            
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Image(src='light.png')
            
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            ElevatedButton('ON',bgcolor='#ff2482',color='white',width=100,
                           icon=Icons.PLAY_ARROW,
                           style=ButtonStyle(padding=15, shape=ContinuousRectangleBorder(radius=200)),
                           on_click=lambda _: flashlight.turn_on),
             ElevatedButton('OFF',bgcolor='#ff2482',color='white',width=100,
                           icon=Icons.PLAY_DISABLED_SHARP,
                           style=ButtonStyle(padding=15, shape=ContinuousRectangleBorder(radius=200)),
                           on_click=lambda _: flashlight.turn_off),
             
                           
            
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Text('\n\n\nDjoumana python app 2025',size=16)
        ],alignment=MainAxisAlignment.CENTER)

    )








    page.update()
app(main)
