import flet as ft

def main(page: ft.Page):
    page.title = "Login com Flet"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.SYSTEM


    def funcao_fazer_login(e):
        valor_usuario = input_usuario.value
        valor_senha = input_senha.value
        if valor_usuario == "Diego":
            if valor_senha == "123":
                modal = ft.AlertDialog(
                    title=ft.Text("Login"),
                    content=ft.Text("Login feito com sucesso !"),
                    alignment=ft.alignment.center,
                    title_padding=ft.padding.all(25),
                )
                page.open(modal)
                page.update()
            else:
                modal = ft.AlertDialog(
                    title=ft.Text("Login"),
                    content=ft.Text("Senha incorreta !"),
                    alignment=ft.alignment.center,
                    title_padding=ft.padding.all(25),
                )
                page.open(modal)
                page.update()
        else:
            modal = ft.AlertDialog(
                    title=ft.Text("Login"),
                    content=ft.Text("Usuário incorreto !"),
                    alignment=ft.alignment.center,
                    title_padding=ft.padding.all(25),
                )
            page.open(modal)
            page.update()
        

    # DEFININDO IMAGEM E TEXTO PRINCIPAL
    imagem_login = ft.Image(
        src="imagem_login_usuario.png",
        height=100,
        width=100,
    )
    txt_login = ft.Text("LOGIN", size=50)

    # DEFININDO ELEMENTOS USUARIO
    image_login_usuario = ft.Image(src="imagem_login_usuario.png",fit=ft.ImageFit.CONTAIN, height=50,width=50)
    input_usuario = ft.TextField(
        label="Usuário",
        hint_text="Digite seu usuário...",
        border=ft.InputBorder.UNDERLINE,
        filled=True
        )
    
    botao_login = ft.ElevatedButton("Fazer Login", on_click=funcao_fazer_login)
    

    # DEFININDO ELEMENTOS SENHA
    image_login_senha = ft.Image(src="imagem_login_senha.png",fit=ft.ImageFit.CONTAIN, height=50,width=50)
    input_senha = ft.TextField(
                                label="Senha",
                                hint_text="Digite sua senha...", 
                                password=True, 
                                can_reveal_password=True,
                                border=ft.InputBorder.UNDERLINE,
                                filled=True
                            )


    inputs = ft.Column(
        controls=[
                    ft.Row([
                                image_login_usuario,
                                input_usuario
                            ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                                image_login_senha,
                                input_senha
                            ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        botao_login
                    ], alignment=ft.MainAxisAlignment.CENTER)
                ]
                        )
    
    titulo = ft.Column(
            controls=
        [
            imagem_login,
            txt_login,
        ]
        )
    

    pagina = ft.Column(controls=[
        titulo,inputs
    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER )


    page.add(pagina)

   
ft.app(target=main, assets_dir="assets")