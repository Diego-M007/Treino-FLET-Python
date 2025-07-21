import flet as ft
import pandas as pd

def main(page: ft.Page):
        page.title = "Recebimentos Rocha Forti"
        page.theme_mode = ft.ThemeMode.DARK

        numero_embalagem = 0
        recebimentos_df = pd.DataFrame(columns=[
            "N° Embalagem",
            "Peso Bruto (g)",
            "Produto",
            "Unidades Embalagem",
            "Peso s/Embalagem (g)",
            "Peso Ideal (g)",
            "Diferença de Peso (g)",
            "Diferença em Unidades do Produto"
        ])
        

        # FUNÇÕES


        def atualizando_tabela_visual():
            previa_tabela.rows.clear()
            for index, linha_dados in recebimentos_df.iterrows():
                adicionando_linha_tabela_visual = ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(linha_dados["N° Embalagem"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Peso Bruto (g)"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Produto"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Unidades Embalagem"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Peso s/Embalagem (g)"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Peso Ideal (g)"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Diferença de Peso (g)"]))),
                        ft.DataCell(ft.Text(str(linha_dados["Diferença em Unidades do Produto"])))
                    ]
                )
                previa_tabela.rows.append(adicionando_linha_tabela_visual)

        
        def adicionando_embalagem(e):
            nonlocal numero_embalagem
            numero_embalagem = numero_embalagem + 1

            try:
                peso = float(input_peso.value)
            except( ValueError, TypeError):
                page.add(ft.SnackBar(content=ft.Text("Erro: O valor do campo 'Peso' é inválido!", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            except Exception as erro:
                print(erro.__class__)
                return

            try:
                produto = str(input_produto.value).lower
                if not produto:
                    raise ValueError
            except( ValueError, TypeError):
                page.add(ft.SnackBar(content=ft.Text("Erro: O valor do campo 'Produto' é inválido!", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            except Exception as erro:
                print(erro.__class__)
                return
            
            try:
                peso_unitario = float(input_peso_unitario.value)
            except( ValueError, TypeError):
                page.add(ft.SnackBar(content=ft.Text("Erro: O valor do campo 'Peso Unitário' é inválido!", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            except Exception as erro:
                print(erro.__class__)
                return

            try:
                peso_embalagem_vazia = float(input_peso_embalagem_vazia.value)
            except( ValueError, TypeError):
                page.add(ft.SnackBar(content=ft.Text("Erro: O valor do campo 'Embalagem Vazia' é inválido!", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            except Exception as erro:
                print(erro.__class__)
                return

            try:
                unidades_por_embalagem = float(input_unidades_por_embalagem.value)
            except( ValueError, TypeError):
                page.add(ft.SnackBar(content=ft.Text("Erro: O valor do campo 'Quantidade por Embalagem' é inválido!", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            except Exception as erro:
                print(erro.__class__)
                return

            peso_sem_embalagem = peso - peso_embalagem_vazia
            peso_ideal = unidades_por_embalagem * peso_unitario
            diferença_peso = peso_ideal - peso_sem_embalagem
            diferença_em_unidades = diferença_peso / peso_unitario

            nova_embalagem = pd.DataFrame(
                    [
                        {
                            "N° Embalagem": f"Embalagem {numero_embalagem}",
                            "Peso Bruto (g)": peso,
                            "Produto": produto,
                            "Unidades Embalagem":unidades_por_embalagem,
                            "Peso s/Embalagem (g)": peso_sem_embalagem,
                            "Peso Ideal (g)": peso_ideal,
                            "Diferença de Peso (g)": diferença_peso,
                            "Diferença em Unidades do Produto": diferença_em_unidades
                        }
                    ]
                )

            nonlocal recebimentos_df
            try:
                recebimentos_df = pd.concat([recebimentos_df, nova_embalagem], ignore_index=True)
                page.add(ft.SnackBar(content=ft.Text("Embalagem adicionada com sucesso !", color="White"), open=True, bgcolor="green"))
                print(recebimentos_df)
                try:
                    atualizando_tabela_visual()
                    page.update()
                except Exception as erro:
                    page.add(ft.SnackBar(content=ft.Text("Erro ao atuaizar tabela visual", color="White"), open=True, bgcolor="Red"))
                    page.update()
                    print(erro.__cause__)
                    print(erro.__class__)
                    print(erro.__context__)

            except:
                page.add(ft.SnackBar(content=ft.Text("Erro ao adicionar Embalagem", color="White"), open=True, bgcolor="Red"))
                page.update()
                return
            
        def gerar_relatorio_excel():
            pass
                    

        
                

        


        # ELEMENTOS

        input_peso = ft.TextField(
            label="Peso (g)",
            hint_text="Digite qual o peso da embalagem em gramas...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        input_produto = ft.TextField(
            label="Produto",
            hint_text="Digite qual o produto...",
            border=ft.InputBorder.OUTLINE,
            filled=True
        )
        input_peso_unitario = ft.TextField(
            label="Peso Unitário (g)",
            hint_text="Digite o peso unitário do produto...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        input_peso_embalagem_vazia = ft.TextField(
            label="Embalagem Vazia (g)",
            hint_text="Digite o peso da embalagem vazia...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        input_unidades_por_embalagem = ft.TextField(
            label="Quantidade por Embalagem",
            hint_text="Digite a quantidade por embalagem...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        input_peso_total = ft.TextField(
            label="Peso Nota Fiscal (g)",
            hint_text="Digite o peso informado na Nota Fiscal...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.NUMBER
            ),

        input_nome_Fornecedor = ft.TextField(
            label="Nome empresa fornecedora",
            hint_text="Digite o nome da Empresa fornecedora...",
            border=ft.InputBorder.OUTLINE,
            filled=True,
            keyboard_type=ft.KeyboardType.TEXT
            ),

        modal_gerar_tabela = ft.AlertDialog(
                modal=True,
                title="Informações para Gerar Tabela",
                content= ft.Row(
                    controls=[
                        input_peso_total,
                        input_nome_Fornecedor
                    ]
                )
            )


        # MODAL TABELA


        previa_tabela = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("N° Embalagem")),
                ft.DataColumn(ft.Text("Peso Bruto (g)"),numeric=True),
                ft.DataColumn(ft.Text("Produto")),
                ft.DataColumn(ft.Text("Unidades Embalagem"),numeric=True),
                ft.DataColumn(ft.Text("Peso s/Embalagem (g)"),numeric=True),
                ft.DataColumn(ft.Text("Peso Ideal (g)"),numeric=True),
                ft.DataColumn(ft.Text("Diferença de Peso (g)"),numeric=True),
                ft.DataColumn(ft.Text("Diferença em Unidades do Produto"),numeric=True)
            ],
            
        )


        modal_previa_tabela = ft.AlertDialog(
            modal=True,
            title="Prévia da tabela",
            content= ft.Row(
                controls=[
                    previa_tabela
                ],scroll=ft.ScrollMode.ADAPTIVE
            ),
            actions=[
                ft.ElevatedButton("Fechar Tabela", on_click=lambda e: page.close(modal_previa_tabela),height=30,)
            ],
            actions_alignment=ft.MainAxisAlignment.END,

            
            
            

        )

        conteudo_btn_add = ft.Container(
            content= ft.Column(
                controls=[
                    ft.Text(value="Adicionar Embalagem")
                ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER
            ),padding=5
        )
        btn_add_linha = ft.ElevatedButton(content=conteudo_btn_add, on_click=adicionando_embalagem)
        btn_ver_tabela = ft.ElevatedButton("Ver Prévia da Tabela", on_click=lambda e: page.open(modal_previa_tabela),)
        btn_gerar_relatorio = ft.ElevatedButton("Gerar Relatório Excel")
        



        # ADICIONANDO ELEMENTOS NA TELA

        header = ft.Container(
            content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Recebimento Rocha Forti",size=100)
                    ],alignment=ft.MainAxisAlignment.CENTER
                )
            ],height=100,alignment=ft.MainAxisAlignment.CENTER
        )
        )
        
        inputs = ft.Container(
            content =  ft.Column(
            controls=[
                input_peso,input_produto,input_peso_unitario,input_peso_embalagem_vazia, input_unidades_por_embalagem
        ],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),expand=True,padding=10
        )

        buttons = ft.Container(
            content= ft.Column(
            controls=[
                btn_add_linha,
                btn_ver_tabela,
                btn_gerar_relatorio
            ],width=200,alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        )



        layout_principal = ft.Row(controls=[
            inputs, buttons
        ],expand=1)

        page.add(header,layout_principal)


ft.app(target=main, assets_dir="assets")