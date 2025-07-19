import flet as ft

def main(page: ft.Page):
    # Adicionando titulo a página
    page.title = "Contador"
    # Alinhando os itens da pagina verticalmente
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # criando um elemento dentro de uma variavel
    caixa_txt = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    

    def funçao_menos(event):
        caixa_txt.value = str(int(caixa_txt.value) - 1)
        page.update()
    
    def funçao_adicionar(event):
        caixa_txt.value = str(int(caixa_txt.value) + 1)
        page.update()

    btn_adicionar = ft.IconButton(ft.Icons.ADD, on_click=funçao_adicionar)
    btn_menos = ft.IconButton(ft.Icons.REMOVE, on_click=funçao_menos)

    page.add(
        ft.Row(
            [
                btn_adicionar,
                caixa_txt,
                btn_menos,
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)